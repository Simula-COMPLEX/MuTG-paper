import numpy as np
from jmetal.core.problem import IntegerProblem
from jmetal.core.solution import IntegerSolution
from testing_int import fitness


class TestingProblem(IntegerProblem):
    def __init__(self, k, program_name, difficult_level, program_input_num, program_output_num, mutant_num, test_sheet1, test_sheet5):
        super(IntegerProblem).__init__()
        self.number_of_variables = k
        self.number_of_objectives = 2
        self.number_of_constraints = 0

        # self.obj_directions = [self.MAXIMIZE]
        self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
        self.lower_bound = self.number_of_variables * [0]
        self.upper_bound = self.number_of_variables * [pow(2, program_input_num)*2]

        self.program_output_num = program_output_num
        self.program_input_num = program_input_num
        self.mutant_num = mutant_num
        self.test_sheet1 = test_sheet1
        self.test_sheet5 = test_sheet5
        self.program_name = program_name
        self.difficult_level = difficult_level

    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:
        variables = np.array(solution.variables)
        print(variables)
        count = 0
        for i in range(len(variables)):
            if variables[i] < pow(2,self.program_input_num):
                count += 1
        solution.objectives[0] = count

        solution.objectives[1] = fitness(variables, self.program_name, self.difficult_level, self.program_input_num, self.program_output_num, self.mutant_num, self.test_sheet1, self.test_sheet5)

        print(count)
        print(solution.objectives[1])

        return solution



    def get_name(self) -> str:
        return 'TestingProblem'
