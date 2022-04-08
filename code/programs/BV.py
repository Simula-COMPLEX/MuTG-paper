import math

from qiskit import (
    # IBMQ,
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)


def dec2bin(n):
    a = 1
    list = []
    while a > 0:
        a, b = divmod(n, 2)
        list.append(str(b))
        n = a
    s = ""
    for i in range(len(list) - 1, -1, -1):
        s += str(list[i])
    s = s.zfill(8)
    return s


def inverse(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '0':
            s_list[i] = '1'
        else:
            s_list[i] = '0'
    s = "".join(s_list)
    return s


def BV(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_easy_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(8):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)

    for i in range(4):
        qc.cz(oracle[i], register[i])

    qc.cz(oracle[3], register[3])  # M1 0.5

    for i in range(4, 8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_easy_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(8):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.cnot(oracle[6], oracle[0])  # M2 0.5

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_easy_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.cz(oracle[2], register[2]) # M3 0.5

    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_easy_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.cswap(oracle[2], oracle[1], oracle[6])  # M4 0.25

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_easy_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.cnot(oracle[0], oracle[7])  # M5 0.5

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_easy_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.x(oracle[4])  # M6 1

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M6_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_easy_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.x(register[3]) # M7 1

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M7_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_easy_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.cswap(register[5], register[7], register[1]) # M8 0.25

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M8_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_easy_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.cnot(oracle[2], oracle[7]) # M9 0.5

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M9_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_easy_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.ccx(oracle[0], oracle[3], oracle[2]) # M10 0.25

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_easy_M10_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_medium_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[5], oracle[1], oracle[7]], oracle[6]) # M1 0.125

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([oracle[1], oracle[4], oracle[7]], register[0]) # M2 0.125

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.mct([oracle[2], oracle[3], register[6]], register[5])  # M3 0.125

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[3], oracle[5], oracle[2], oracle[7]], oracle[4]) # M4 0.0625

    qc.barrier(oracle)

    qc.h(register)

    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[6], oracle[4], oracle[7], oracle[3]], oracle[0])  # M5 0.0625

    qc.barrier(oracle)

    qc.h(register)

    for i in range(8):
        qc.cz(oracle[i], register[i])



    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[4], oracle[3], oracle[0], oracle[2], oracle[7]], oracle[5])  # M6 0.03125

    qc.barrier(oracle)

    qc.h(register)

    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M8_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)

    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[6], register[5], register[0], register[3], register[7]], register[2])  # M7 0.03125

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M9_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_medium_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[2], oracle[1], oracle[5], oracle[4], oracle[3]], oracle[7])  # M8 0.03125

    qc.barrier(oracle)

    qc.h(register)

    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M10_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_medium_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)

    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    
    qc.mct([register[0], register[1], register[4], register[5], register[7], register[2]], register[3])  # M9 1.56%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M10_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_medium_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)

    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[6], register[5], register[0], register[3], register[7], register[1]], register[2])  # M10 1.56%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M9_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[3], oracle[7], oracle[2], oracle[1], oracle[5], oracle[0], oracle[4]], oracle[6]) # M1 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[0], oracle[5], oracle[7], oracle[6], oracle[4], oracle[1], oracle[2]], oracle[3])  # M2 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])


    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[4], register[3], register[2], register[6], register[7], register[1], register[5]], register[0])  # M3 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[1], register[0], register[7], register[4], register[2], register[3], register[5]], register[6])  # M4 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[2], register[1], register[6], register[7], register[0], register[3], register[5]], register[4])  # M5 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.p(math.pi / 6, oracle[3]) # M6 0

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.p(math.pi / 6, oracle[1]) # M7 0

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.p(math.pi / 6, oracle[7]) # M8 0

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.p(math.pi / 6, register[7]) # M9 0

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.p(math.pi / 6, register[2])  # M10 0

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[3], oracle[7], oracle[2], oracle[1], oracle[5], oracle[0], oracle[4]], oracle[6]) # M1 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult1_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[0], oracle[5], oracle[7], oracle[6], oracle[4], oracle[1], oracle[2]], oracle[3])  # M2 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])


    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[4], register[3], register[2], register[6], register[7], register[1], register[5]], register[0])  # M3 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult1_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[1], register[0], register[7], register[4], register[2], register[3], register[5]], register[6])  # M4 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[2], register[1], register[6], register[7], register[0], register[3], register[5]], register[4])  # M5 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.p(math.pi / 6, oracle[3]) # M6 0

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[2], oracle[4], oracle[3], oracle[1], oracle[6], oracle[0], oracle[7]], oracle[5])  # M7 0.78125%
    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[1], oracle[0], oracle[2], oracle[3], oracle[4], oracle[6], oracle[7]], oracle[5])  # M8 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[3], register[2], register[1], register[0], register[5], register[7], register[6]], register[4])  # M9 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult1_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[3], register[5], register[7], register[2], register[4], register[6], register[0]], register[1])  # M10 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[3], oracle[7], oracle[2], oracle[1], oracle[5], oracle[0], oracle[4]], oracle[6]) # M1 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.mct([oracle[0], oracle[5], oracle[7], oracle[6], oracle[4], oracle[1], oracle[2]], oracle[3])  # M2 0.78125%

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])


    qc.barrier(oracle)

    qc.h(register)
    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    #circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def BV_difficult3_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[4], register[3], register[2], register[6], register[7], register[1], register[5]], register[0])  # M3 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[1], register[0], register[7], register[4], register[2], register[3], register[5]], register[6])  # M4 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[2], register[1], register[6], register[7], register[0], register[3], register[5]], register[4])  # M5 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.p(math.pi / 6, oracle[3]) # M6 0

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)
    for i in range(4):
        qc.cz(oracle[i], register[i])
    qc.p(math.pi / 6, oracle[1])  # M7 0

    for i in range(4, 8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)
    qc.p(math.pi / 4, register[7])  # M8 0
    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])


    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[3], register[2], register[1], register[0], register[5], register[7], register[6]], register[4])  # M9 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_difficult3_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    c = ClassicalRegister(8)
    qc = QuantumCircuit(oracle, register, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(8):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    qc.mct([register[3], register[5], register[7], register[2], register[4], register[6], register[0]], register[1])  # M10 0.78125%

    qc.measure(register, c)

    from qiskit.tools.visualization import circuit_drawer

    # circuit_drawer(qc, filename='./BV_medium_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def BV_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    oracle = QuantumRegister(8)
    register = QuantumRegister(8)
    qc = QuantumCircuit(oracle, register)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[7 - i] == '1':
            qc.x(oracle[i])

    qc.barrier(oracle)

    qc.h(register)
    for i in range(len(input_string)):
        qc.cz(oracle[i], register[i])

    qc.barrier(oracle)

    qc.h(register)

    # from qiskit.tools.visualization import circuit_drawer
    #
    # circuit_drawer(qc, filename='./BV_circuit')

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = BV_specification(input)
    for i in range(256):
        temp = 0
        for j in range(256):
            temp += abs(t[i * 256 + j]) ** 2
        pt.append(temp)
    return pt


