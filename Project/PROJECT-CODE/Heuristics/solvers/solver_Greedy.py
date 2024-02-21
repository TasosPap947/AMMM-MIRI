'''
AMMM Lab Heuristics
Greedy solver
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
'''

import random, time, copy
from Heuristics.solver import _Solver
from Heuristics.solvers.localSearch import LocalSearch


# Inherits from the parent abstract solver.
class Solver_Greedy(_Solver):

    def _selectCandidate(self, candidateList):
        if self.config.solver == 'Greedy':
            # sort candidate assignments by highestLoad in ascending order
            sortedCandidateList = sorted(candidateList, key=lambda x: x.highestLoad)
            # choose assignment with minimum highest load
            return sortedCandidateList[0]
        return random.choice(candidateList)

    def construction(self):
        # get an empty solution for the problem
        solution = self.instance.createSolution()

        n = self.instance.getN()

        # IMPLEMENTATION 1: Exponential steps
        '''
        solution.numbers[0] = 0
        for i in range(0, n-1):
            solution.numbers[i+1] = solution.numbers[i] + 2**i

        solution.updateFitnessScore()
        '''

        # IMPLEMENTATION 2: Iterative approach
        solution.numbers[0] = 0
        smallestDiff = solution.getSmallestUnsusedDifference(0)
        pointer = len(solution.numbers) - 1 # pointer to the last element of the solution

        while(len(solution.numbers) < n):             # while the solution is not complete
            candidate_number = solution.numbers[pointer] + smallestDiff # candidate number to be added to the solution
            # print("Candidate: ", candidate_number)
            # print("Solution: ", solution.numbers)
            # print("Smallest diff: ", smallestDiff)
            if (solution.isFeasibleToAdd(candidate_number)):
                solution.addNumber(candidate_number)
                pointer += 1
            smallestDiff = solution.getSmallestUnsusedDifference(smallestDiff)        

        # Prune the DiffCounters List
        solution.pruneDiffCounters()

        return solution

    def solve(self, **kwargs):
        self.startTimeMeasure()

        solver = kwargs.get('solver', None)
        if solver is not None:
            self.config.solver = solver
        localSearch = kwargs.get('localSearch', None)
        if localSearch is not None:
            self.config.localSearch = localSearch

        self.writeLogLine(float('inf'), 0)

        solution = self.construction()
        if self.config.localSearch:
            localSearch = LocalSearch(self.config, None)
            endTime= self.startTime + self.config.maxExecTime
            solution = localSearch.solve(solution=solution, startTime=self.startTime, endTime=endTime)

        self.elapsedEvalTime = time.time() - self.startTime
        self.writeLogLine(solution.getFitness(), 1)
        self.numSolutionsConstructed = 1
        self.printPerformance()

        return solution


