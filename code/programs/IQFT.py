import numpy as np
from qiskit import (
    #IBMQ,
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)
from math import pi
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import circuit_drawer
from rpy2 import robjects as robjects

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
    s = s.zfill(10)#input的位数
    return s

# def inverse(s):
#     s_list = list(s)
#     for i in range(len(s_list)):
#         if s_list[i] == '0':
#             s_lmediumist[i] = '1'
#         else:
#             s_list[i] ='0'
#     s = "".join(s_list)
#     return s

def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft_rotations(circuit, qubit, p):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    # if n == 0:
    #     return circuit
    # n -= 1
    # circuit.h(9-n)
    # for qubit in range(n):
    #     circuit.cu1(pi/2**(n-qubit), qubit, n)
    # # At the end of our function, we call the same function again on
    # # the next qubits (we reduced n by one earlier in the function)
    # qft_rotations(circuit, n)

    # for qubit in range(n):
    #     circuit.h(qubit)
    #     p = 1
    #     for j in range(qubit + 1, 10):
    #         circuit.cu1(pi/2**(p), qubit, j)
    #         p += 1
    #     circuit.barrier()
    # return circuit

    # for qubit in range(n):
    #     circuit.h(qubit)
    #     p = 1
    for j in range(qubit + 1, 10):
        circuit.cu1(pi/2**(p), qubit, j)
        p += 1
    circuit.barrier()
    return circuit

def mch(qc, c_q, t_q):
    qc.ry(pi/4,t_q)
    qc.mct(c_q,t_q)
    qc.ry(-pi/4,t_q)
    return qc

def IQFT(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc,10)
    #qft_rotations(qc,10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    qc.measure(q,c)

    circuit_drawer(qc, filename='./IQFT_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])
    mch(qc, [q[1], q[3]], q[2])  # M1 0.25
    qc.barrier()

    swap_registers(qc,10)
    #qft_rotations(qc,10)
    for qubit in range(10):
        qc.h(qubit)
        qft_rotations(qc,qubit,1)

    qc.barrier()

    qc.measure(q,c)

    #circuit_drawer(qc, filename='./IQFT_M1_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc,10)
    for qubit in range(3):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    for qubit in range(3,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)
    mch(qc, [q[1], q[3]], q[2])  # M2 0.9921875
    qc.barrier()

    qc.measure(q,c)

    #circuit_drawer(qc, filename='./IQFT_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def IQFT_easy_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(3):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    mch(qc, [q[2], q[5]], q[3])  # M3 0.5
    for qubit in range(3,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M3_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    qc.h(q[0])  # M4 1

    swap_registers(qc, 10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.ch(q[8],q[3])  # M5 0.5

    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)
    qc.ch(q[8], q[3])  # M6 0.984375
    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    mch(qc, [q[1], q[2], q[3]], q[5])  # M7 0.9375

    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    mch(qc, [q[1], q[2], q[4], q[3]], q[5])  # M8 0.9375

    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[1], q[7]], q[5])  # M9 0.25

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_easy_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    mch(qc, [q[6], q[4]], q[3])  # M10 0.5

    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])
    mch(qc, [q[0], q[3], q[5], q[2], q[8]], q[4]) # M1 0.03125
    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])
    mch(qc, [q[0], q[3], q[2], q[8]], q[4])  # M2 0.0625
    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def IQFT_medium_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])
    mch(qc, [q[0], q[3], q[8]], q[4])  # M3 0.125
    qc.barrier()

    swap_registers(qc, 10)
    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def IQFT_medium_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[0], q[1], q[2]], q[3])  # M4 0.125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[0], q[1], q[2]], q[5])  # M5 0.125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[3], q[4], q[5], q[6], q[7]], q[8])  # M6 0.3125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[1], q[4], q[5], q[6], q[7]], q[9])  # M7 0.3125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[4], q[5], q[6], q[7], q[8]], q[9])  # M8 0.0015625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[1], q[4], q[5], q[6], q[7], q[8]], q[0])  # M9 0.0015625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_medium_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[3], q[5], q[6], q[7], q[8]], q[0])  # M9 0.0015625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[2], q[3], q[5], q[6], q[7], q[8]], q[0])  # M9 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[2], q[3], q[5], q[6], q[7], q[9]], q[0])  # M2 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[9]], q[0])  # M3 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[2], q[3], q[5], q[6], q[7], q[8], q[9]], q[1])  # M4 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[3], q[5], q[6], q[7], q[8], q[9]], q[2])  # M5 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[4], q[5], q[6], q[7], q[8], q[9]], q[3])  # M6 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[4], q[5], q[6], q[7], q[8]], q[3])  # M7 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.x(q[0]) #M8 0
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult3_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.p(pi/2, q[0])#M9 0
    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def IQFT_difficult3_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    for qubit in range(6, 10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.cz(q[0], q[1])  # M10 0

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[2], q[3], q[5], q[6], q[7], q[8]], q[0])  # M9 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[2], q[3], q[5], q[6], q[7], q[9]], q[0])  # M2 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[9]], q[0])  # M3 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[2], q[3], q[5], q[6], q[7], q[8], q[9]], q[1])  # M4 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[3], q[5], q[6], q[7], q[8], q[9]], q[2])  # M5 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[4], q[5], q[6], q[7], q[8], q[9]], q[3])  # M6 0.00390625
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[4], q[5], q[6], q[7], q[8]], q[3])  # M7 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc,[q[0], q[1], q[4], q[3], q[6], q[7], q[8]], q[2])  # M8 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def IQFT_difficult1_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    mch(qc, [q[0], q[1], q[4], q[3], q[6], q[7], q[2]], q[8])  # M8 0.0078125
    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)


    for qubit in range(6,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.measure(q, c)

    #circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def IQFT_difficult1_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q, c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9 - i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc, 10)

    for qubit in range(6):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    for qubit in range(6, 10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc, qubit, p)

    qc.barrier()

    qc.cz(q[0], q[1])  # M10 0

    qc.measure(q, c)

    # circuit_drawer(qc, filename='./IQFT_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts




def IQFT_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    q = QuantumRegister(10)
    c = ClassicalRegister(10)

    qc = QuantumCircuit(q,c)

    input_string = dec2bin(input)
    for i in range(10):
        if input_string[9-i] == '1':
            qc.x(q[i])

    qc.barrier()

    swap_registers(qc,10)
    #qft_rotations(qc,10)
    for qubit in range(10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.barrier()

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = IQFT_specification(input)
    for i in range(1024):
        pt.append(abs(t[i])**2)
    return pt



