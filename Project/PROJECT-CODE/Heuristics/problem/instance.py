"""
AMMM Lab Heuristics
Representation of a problem instance
Copyright 2020 Luis Velasco.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from Heuristics.problem.solution import Solution


class Instance(object):
    def __init__(self, config, inputData):
        self.config = config
        self.inputData = inputData
        self.n = inputData.n     # n = number of numbers

        self.numbers = [None]                           # vector with numbers
        self.diffMatrix = [[None] * self.n] * self.n    # matrix with differences between numbers
        # self.diffCounters = [0]                         # vector with number of differences between numbers
        self.diffCounters = [0] * self.n**3             # vector with number of differences between numbers

    def getN(self):
        return self.n
    
    def getNumbers(self):
        return self.numbers

    def createSolution(self):
        solution = Solution(self.numbers, self.diffMatrix, self.diffCounters)
        solution.setVerbose(self.config.verbose)
        return solution
    
    def checkInstance(self):
        return True