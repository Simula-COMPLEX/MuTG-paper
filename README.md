# Mutation-Based Test Generation for Quantum Programs with Multi-Objective Search
## Installation
* Install Anaconda3. You can download Anaconda for your OS from https://www.anaconda.com/
* Create an environment (e.g., with name "myenv")
    - conda create -n myenv python=3.7 scipy numpy rpy2
* Activate the environment, and install qiskit, jmetalpy and openpyxl
    - conda activate myenv
    - pip install qiskit
    - pip install jmetalpy
    - pip install openpyxl
* In your Anaconda installation, change the file envs/myenv/lib/python3.7/site-packages/jmetal/operator/init.py
    - "DifferentialEvolutionCrossover" must be changed in "DifferentialEvolutionCrossover, IntegerSBXCrossover"

## Running experiment
First, you need to activate the conda environment:\
```conda activate myenv```\
Then, you can start the program (from the 'code' root) as follows: 

### MutTG
```python main_int.py program_name difficult_level input_bit output_bit mutant_num k file_name algorithm``` \
where
* *program_name* is the name of the original program. Available program in the repository are: AS, BV, CE, IQ, and QR
* *difficult_level* can be easy, medium, difficult1, or difficult3 (that correspond to E, M, D1, and D3 in the paper)
* *input_bit* is the number of input qubits of the program.
* *output_bit* is the number of output qubits of the program.
* *mutant_num* is the number of mutants of the program.
* *k* is the maximum length k of an individual (that also identifies the maximum possible size of the test suite)
* *file_name* is the name of the generated excel file. Each excel workbook contains 5 sheets: gen_test, gen_test_count, FUN_test, VAR_test and objective log.
* *algorithm* is either 'Search' or 'RS' to run NSGA-II or random search.

### MutTG without discount
```python main_int_adj.py program_name difficult_level input_bit output_bit mutant_num k file_name algorithm``` 

