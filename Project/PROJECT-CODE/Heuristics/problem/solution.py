"""
AMMM Lab Heuristics
Representation of a solution instance
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

import copy
from Heuristics.solution import _Solution


# This class stores the load of the highest loaded CPU
# when a task is assigned to a CPU.
class Assignment(object):
    def __init__(self, taskId, cpuId, highestLoad):
        self.taskId = taskId
        self.cpuId = cpuId
        self.highestLoad = highestLoad

    def __str__(self):
        return "<t_%d, c_%d>: highestLoad: %.2f%%" % (self.taskId, self.cpuId, self.highestLoad*100)


# Solution includes functions to manage the solution, to perform feasibility
# checks and to dump the solution into a string or file.
class Solution(_Solution):
    def __init__(self, numbers, diffMatrix, diffCounters):
        # self.n = n
        self.numbers = numbers
        self.diffMatrix = diffMatrix
        self.diffCounters = diffCounters

        super().__init__()

    def updateFitnessScore(self):
        self.fitness = self.numbers[-1]

    def getSmallestUnsusedDifference(self, start_idx):
        return self.diffCounters.index(0, start_idx) + 1
    
    def isFeasibleToAdd(self, new_number):
        for i in range(len(self.numbers)):
            diff = new_number - self.numbers[i]
            if self.diffCounters[diff - 1] > 0:
                return False

        return True

        
    def addNumber(self, new_number):
        pointer = len(self.numbers)
        for i in range(pointer):
            diff = abs(new_number - self.numbers[i])
            self.diffMatrix[pointer][i] = diff  # add difference to only one side of the matrix
            self.diffCounters[diff - 1] += 1

        self.numbers.append(new_number)
        self.updateFitnessScore()

    def pruneDiffCounters(self):
        self.diffCounters = self.diffCounters[:self.numbers[-1]]

    # ==================================================================================================


    def __str__(self):

        strSolution = 'z = %d;\n' % self.fitness

        strSolution += 'numbers = [ '
        for number in self.numbers:
            strSolution += str(number) + ' '
        strSolution += '];\n'

        return strSolution

    def saveToFile(self, filePath):
        f = open(filePath, 'w')
        f.write(self.__str__())
        f.close()
