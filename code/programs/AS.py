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
    s = s.zfill(10)
    return s


def AS(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.h(a[2])
    qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.x(a[7]) #M1 difficult: 100%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.x(a[8]) #M2 difficult:100%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.x(a[4]) #M3 difficult:100%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.cx(a[3], a[6]) #M4 difficult:50%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.cx(a[7], a[6])  # M5 difficult:50%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.cx(a[5], a[0])  # M6 difficult:50%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.cx(a[3], a[2])  # M7 difficult:50%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.ccx(a[7], a[4], a[8]) # M8 difficult:25%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.ccx(a[2], a[8], a[6])  # M9 difficult:25%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_easy_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.ccx(a[7], a[3], a[0])  # M10 difficult:25%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AS_medium_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[6], a[7], a[3]], a[9]) # M1 difficult:12.5%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[9], a[8], a[2]], a[0])  # M2 difficult:12.5%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[7], a[2], a[5]], a[4])  # M3 difficult:12.5%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[3], a[8], a[2], a[4]], a[7]) #M4 difficult:6.25

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[6], a[7], a[8], a[0]], a[4])  # M5 difficult:6.25

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[2], a[8], a[1], a[4], a[5]], a[6]) #M6 difficult:3.125

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[7], a[6], a[8], a[3], a[9]], a[1])  # M7 difficult:3.125

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[3], a[2], a[9], a[4], a[1], a[8]], a[5]) #M8 difficult:1.56%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[4], a[8], a[9], a[7], a[5], a[0]], a[3])  # M9 difficult:1.56%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_medium_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[9], a[1], a[4], a[2], a[0], a[3]], a[5])  # M10 difficult:1.56%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def AS_difficult3_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[4], a[5], a[9], a[2], a[1], a[0], a[8]], a[6])  # M1 difficult:0.78%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[3], a[7], a[9], a[6], a[0], a[5], a[4]], a[8])  # M2 difficult:0.78%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[1], a[7], a[4], a[9], a[8], a[2], a[5]], a[0])  # M3 difficult:0.78%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[8], a[9], a[4], a[0], a[7], a[3], a[2], a[1]], a[6])  # M4 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[3], a[5], a[4], a[1], a[8], a[0], a[2], a[6]], a[7])  # M5 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[9], a[7], a[3], a[8], a[0], a[6], a[5], a[4]], a[2])  # M6 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[4], a[9], a[6], a[2], a[8], a[1], a[0], a[5]], a[7])  # M7 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.p(math.pi / 6, a[5])  # M8 difficult:0

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.p(math.pi / 6, a[1]) #M9 difficult:0

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult3_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.p(math.pi/6, a[3]) #M10

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[4], a[5], a[9], a[2], a[1], a[0], a[8]], a[6])  # M1 difficult:0.78%

    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[3], a[7], a[9], a[6], a[0], a[5], a[4]], a[8])  # M2 difficult:0.78%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[1], a[7], a[4], a[9], a[8], a[2], a[5]], a[0])  # M3 difficult:0.78%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[8], a[9], a[4], a[0], a[7], a[3], a[2], a[1]], a[6])  # M4 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[3], a[5], a[4], a[1], a[8], a[0], a[2], a[6]], a[7])  # M5 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[9], a[7], a[3], a[8], a[0], a[6], a[5], a[4]], a[2])  # M6 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[4], a[9], a[6], a[2], a[8], a[1], a[0], a[5]], a[7])  # M7 difficult:0.39%

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[2], a[3], a[4], a[5], a[6], a[7], a[8]], a[1]) #M8

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.mct([a[0], a[1], a[2], a[4], a[5], a[6], a[7], a[8]], a[3])  # M9

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_difficult1_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    qc.p(math.pi/6, a[3]) #M10

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    qc.barrier(a)

    qc.measure(a, c)

    # circuit_drawer(qc, filename='./AS_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def AS_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    a = QuantumRegister(10)
    b = QuantumRegister(2)
    c = ClassicalRegister(10)
    qc = QuantumCircuit(a, b, c)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(a[i])

    qc.barrier(a)

    # qc.h(a[2])
    # qc.p(math.pi / 4, a[2])

    qc.x(b[0])
    qc.h(b[1])
    qc.p(math.pi / 2, b[1])

    for i in range(9):
        control = []
        control.append(b[0])
        for j in range(9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[0], a[0])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(8):
        control = []
        control.append(b[0])
        control.append(b[1])
        for j in range(1, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.ccx(b[0], b[1], a[1])

    qc.barrier(a)

    for i in range(7):
        control = []
        control.append(b[1])
        for j in range(2, 9 - i):
            control.append(a[j])
        qc.mct(control, a[9 - i])
    qc.cnot(b[1], a[2])

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = AS_specification(input)
    for i in range(1024):
        temp = 0
        for j in range(4):
            temp += abs(t[j * 1024 + i]) ** 2
        pt.append(temp)
    return pt
