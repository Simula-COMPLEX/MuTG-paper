import sys

import search_int

if __name__ == '__main__':
    program_name = sys.argv[1]
    difficult_level = sys.argv[2]
    input_bit = int(sys.argv[3])
    output_bit = int(sys.argv[4])
    mutant_num = int(sys.argv[5])
    k = int(sys.argv[6])
    file_name = sys.argv[7]
    alg = sys.argv[8] # "Search" or "RS"
    search_int.search_int(program_name, difficult_level, input_bit, output_bit, mutant_num, k, file_name, alg)
