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


def CE(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M1(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.x(b[0])#M1

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M2(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.h(b[0])  # M2

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M3(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.h(b[0])  # M3

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M4(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(3):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    qc.cx(b[0],b[2])#M4

    for i in range(3,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M5(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.swap(b[0],b[5])#M5

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M6(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.cswap(b[2],b[0],b[5])#M6

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M7(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.cswap(b[1], b[2], b[6])  # M7

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_easy_M8(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(5):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.cswap(b[0], b[3], b[7])  # M8

    for i in range(5,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts
    #
    # simulator = Aer.get_backend('qasm_simulator')
    #
    # a = QuantumRegister(3)
    # b = QuantumRegister(11)
    # c = ClassicalRegister(11)
    # qc = QuantumCircuit(a, b, c)
    #
    # # a
    # qc.x(a[0])
    # qc.h(a[2])
    #
    # qc.barrier(a)
    #
    # input_string = dec2bin(input)
    # for i in range(len(input_string)):
    #     if input_string[9 - i] == '1':
    #         qc.x(b[i])
    #
    # # b
    # qc.h(b[1])
    # qc.p(math.pi / 4, b[1])
    # qc.barrier(b)
    #
    # # a-=3
    # qc.x(a[1])
    # qc.cx(a[1], a[2])
    # qc.x(a[0])
    # qc.cx(a[0], a[1])
    # qc.mct([a[0], a[1]], a[2])
    # qc.barrier(a)
    #
    # # if a<0, b++
    # for i in range(5):
    #     control = []
    #     control.append(a[2])
    #     if i < 10:
    #         for j in range(10 - i):
    #             control.append(b[j])
    #     qc.mct(control, b[10 - i])
    # qc.barrier(a)
    #
    # qc.cswap(b[0], b[3], b[7])  # M8
    #
    # for i in range(5,11):
    #     control = []
    #     control.append(a[2])
    #     if i < 10:
    #         for j in range(10 - i):
    #             control.append(b[j])
    #     qc.mct(control, b[10 - i])
    # qc.barrier(a)
    #
    # # a+=3
    # qc.mct([a[0], a[1]], a[2])
    # qc.cx(a[0], a[1])
    # qc.x(a[0])
    # qc.cx(a[1], a[2])
    # qc.x(a[1])
    # qc.barrier(b)
    #
    # qc.measure(b, c)
    #
    # ##circuit_drawer(qc, filename='./CE_circuit')
    #
    # job = execute(qc, simulator, shots=count_number * 100)
    # result = job.result()
    # counts = result.get_counts(qc)
    #
    # return counts

def CE_easy_M9(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(3):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    qc.h(b[5])  # M9

    for i in range(3,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_easy_M10(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(4):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    qc.swap(b[3],b[6])#M10

    for i in range(4,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_medium_M1(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(6):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[4], b[5], b[6], b[7]], b[9])  # M1

    for i in range(6,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


# def CE_medium_M2(input, count_number):
#     simulator = Aer.get_backend('qasm_simulator')
#
#     a = QuantumRegister(3)
#     b = QuantumRegister(11)
#     c = ClassicalRegister(11)
#     qc = QuantumCircuit(a, b, c)
#
#
#     # a
#     qc.x(a[0])
#     qc.h(a[2])
#
#     qc.barrier(a)
#
#     input_string = dec2bin(input)
#     for i in range(len(input_string)):
#         if input_string[9 - i] == '1':
#             qc.x(b[i])
#
#     # b
#     qc.h(b[1])
#     qc.p(math.pi / 4, b[1])
#     qc.barrier(b)
#
#     # a-=3
#     qc.x(a[1])
#     qc.cx(a[1], a[2])
#     qc.x(a[0])
#     qc.cx(a[0], a[1])
#     qc.mct([a[0], a[1]], a[2])
#     qc.barrier(a)
#
#     # if a<0, b++
#     for i in range(6):
#         control = []
#         control.append(a[2])
#         if i < 10:
#             for j in range(10 - i):
#                 control.append(b[j])
#         qc.mct(control, b[10 - i])
#
#     qc.mct([b[1], a[1], b[4], b[5], b[6], b[7]], b[9])  # M2
#
#     for i in range(6, 11):
#         control = []
#         control.append(a[2])
#         if i < 10:
#             for j in range(10 - i):
#                 control.append(b[j])
#         qc.mct(control, b[10 - i])
#
#     qc.barrier(a)
#
#     # a+=3
#     qc.mct([a[0], a[1]], a[2])
#     qc.cx(a[0], a[1])
#     qc.x(a[0])
#     qc.cx(a[1], a[2])
#     qc.x(a[1])
#     qc.barrier(b)
#
#     qc.measure(b, c)
#
#     ##circuit_drawer(qc, filename='./CE_circuit')
#
#     job = execute(qc, simulator, shots=count_number * 100)
#     result = job.result()
#     counts = result.get_counts(qc)
#
#     return counts

def CE_medium_M2(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.mct([b[9],b[1],[2],b[3],b[4],b[5],b[6],b[7]],b[8])#M2

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts



def CE_medium_M3(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(4):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[0], b[5], b[9], b[7]], b[8])  # M3

    for i in range(4,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_medium_M4(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(3):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[0], b[9], b[7]], b[6])  # M4

    for i in range(3,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_medium_M5(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    qc.mct([b[1], a[2], b[0], b[9], b[7]], b[6])  # M5

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_medium_M6(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[6], b[7]], b[9])  # M6

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

# def CE_medium_M7(input, count_number):
#     simulator = Aer.get_backend('qasm_simulator')
#
#     a = QuantumRegister(3)
#     b = QuantumRegister(11)
#     c = ClassicalRegister(11)
#     qc = QuantumCircuit(a, b, c)
#
#     # a
#     qc.x(a[0])
#     qc.h(a[2])
#
#     qc.barrier(a)
#
#     input_string = dec2bin(input)
#     for i in range(len(input_string)):
#         if input_string[9 - i] == '1':
#             qc.x(b[i])
#
#     # b
#     qc.h(b[1])
#     qc.p(math.pi / 4, b[1])
#     qc.barrier(b)
#
#     # a-=3
#     qc.x(a[1])
#     qc.cx(a[1], a[2])
#     qc.x(a[0])
#     qc.cx(a[0], a[1])
#     qc.mct([a[0], a[1]], a[2])
#     qc.barrier(a)
#
#     # if a<0, b++
#     for i in range(11):
#         control = []
#         control.append(a[2])
#         if i < 10:
#             for j in range(10 - i):
#                 control.append(b[j])
#         qc.mct(control, b[10 - i])
#     qc.barrier(a)
#
#     #qc.mct([b[1], a[2], b[0], b[9], b[7]], b[6])  # M5
#     qc.mct([b[0],b[1],b[4],b[6],b[7],b[8]],b[2])#M7
#
#     # a+=3
#     qc.mct([a[0], a[1]], a[2])
#     qc.cx(a[0], a[1])
#     qc.x(a[0])
#     qc.cx(a[1], a[2])
#     qc.x(a[1])
#     qc.barrier(b)
#
#     qc.measure(b, c)
#
#     ##circuit_drawer(qc, filename='./CE_circuit')
#
#     job = execute(qc, simulator, shots=count_number * 100)
#     result = job.result()
#     counts = result.get_counts(qc)
#
#     return counts

def CE_medium_M7(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(9):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[0], b[1], a[2], b[3], b[4], b[5], b[6], b[7]], b[9])  # M7

    for i in range(9,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

# def CE_medium_M8(input, count_number):
#     simulator = Aer.get_backend('qasm_simulator')
#
#     a = QuantumRegister(3)
#     b = QuantumRegister(11)
#     c = ClassicalRegister(11)
#     qc = QuantumCircuit(a, b, c)
#
#     # a
#     qc.x(a[0])
#     qc.h(a[2])
#
#     qc.barrier(a)
#
#     input_string = dec2bin(input)
#     for i in range(len(input_string)):
#         if input_string[9 - i] == '1':
#             qc.x(b[i])
#
#     qc.mct([b[0],b[3],b[5],b[6],b[7]],b[2])#M8
#
#     # b
#     qc.h(b[1])
#     qc.p(math.pi / 4, b[1])
#     qc.barrier(b)
#
#     # a-=3
#     qc.x(a[1])
#     qc.cx(a[1], a[2])
#     qc.x(a[0])
#     qc.cx(a[0], a[1])
#     qc.mct([a[0], a[1]], a[2])
#     qc.barrier(a)
#
#     # if a<0, b++
#     for i in range(11):
#         control = []
#         control.append(a[2])
#         if i < 10:
#             for j in range(10 - i):
#                 control.append(b[j])
#         qc.mct(control, b[10 - i])
#     qc.barrier(a)
#
#     # a+=3
#     qc.mct([a[0], a[1]], a[2])
#     qc.cx(a[0], a[1])
#     qc.x(a[0])
#     qc.cx(a[1], a[2])
#     qc.x(a[1])
#     qc.barrier(b)
#
#     qc.measure(b, c)
#
#     ##circuit_drawer(qc, filename='./CE_circuit')
#
#     job = execute(qc, simulator, shots=count_number * 100)
#     result = job.result()
#     counts = result.get_counts(qc)
#
#     return counts


def CE_medium_M8(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)
    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7]], b[8])  # M8

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_medium_M9(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(5):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    qc.mct([b[0], b[2], b[5], b[6], b[7]], b[3])  # M9

    for i in range(5,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_medium_M10(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)


    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(2):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    qc.mct([b[0], b[2], b[6], b[9]], b[7])  # M10

    for i in range(2,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])
    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M1(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)
    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.mct([a[0],b[0],b[1],b[3],b[6],b[8],b[9],b[7]],b[2])#M1

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M2(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.mct([b[0],b[9],b[1],[2],b[3],b[4],b[5],b[6],b[7]],b[8])#M2

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M3(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(9):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[0], b[1], a[2], b[3], b[4], b[5], b[6], b[7], b[8]], b[9])  # M3

    for i in range(9,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M4(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7],b[9]], b[8])  # M4

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M5(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[6], b[0], b[9], b[2]], b[7])  # M5

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M6(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(5):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[8], b[9], b[7], b[0]], b[6])  # M6

    for i in range(5,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M7(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[8], b[9], b[0], b[2], b[7]], b[6])  # M7

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M8(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.p(math.pi/6,b[1])#M8

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M9(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.x(a[1])#M9

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult3_M10(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(6):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.cswap(a[0],b[0],b[1])#M10

    for i in range(6,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_difficult1_M1(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)
    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.mct([a[0],b[0],b[1],b[3],b[6],b[8],b[9],b[7]],b[2])#M1

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M2(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.mct([b[0],b[9],b[1],[2],b[3],b[4],b[5],b[6],b[7]],b[8])#M2

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M3(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(9):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[0], b[1], a[2], b[3], b[4], b[5], b[6], b[7], b[8]], b[9])  # M3

    for i in range(9,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M4(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7],b[9]], b[8])  # M4

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M5(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[6], b[0], b[9], b[2]], b[7])  # M5

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M6(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(5):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[8], b[9], b[7], b[0]], b[6])  # M6

    for i in range(5,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M7(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(7):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.mct([b[1], a[2], b[3], b[4], b[5], b[8], b[9], b[0], b[2], b[7]], b[6])  # M7

    for i in range(7,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M8(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.mct([b[1], a[2], b[6], b[4], b[5], b[8], b[9], b[0], b[2], b[7]], b[3])  # M8

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M9(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])

    qc.mct([b[1], a[2], b[6], b[4], b[5], b[8], b[9], b[3], b[2], b[7]], b[0])  # M8

    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def CE_difficult1_M10(input, count_number):
    simulator = Aer.get_backend('qasm_simulator')

    a = QuantumRegister(3)
    b = QuantumRegister(11)
    c = ClassicalRegister(11)
    qc = QuantumCircuit(a, b, c)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    # b
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(6):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.cswap(a[0],b[0],b[1])#M10

    for i in range(6,11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    qc.measure(b, c)

    ##circuit_drawer(qc, filename='./CE_circuit')

    job = execute(qc, simulator, shots=count_number * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def CE_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    a = QuantumRegister(3)
    b = QuantumRegister(11)
    qc = QuantumCircuit(a, b)

    # a
    qc.x(a[0])
    qc.h(a[2])

    qc.barrier(a)

    # b
    input_string = dec2bin(input)
    for i in range(len(input_string)):
        if input_string[9 - i] == '1':
            qc.x(b[i])
    qc.h(b[1])
    qc.p(math.pi / 4, b[1])
    qc.barrier(b)

    # a-=3
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.x(a[0])
    qc.cx(a[0], a[1])
    qc.mct([a[0], a[1]], a[2])
    qc.barrier(a)

    # if a<0, b++
    for i in range(11):
        control = []
        control.append(a[2])
        if i < 10:
            for j in range(10 - i):
                control.append(b[j])
        qc.mct(control, b[10 - i])

    qc.barrier(a)

    # a+=3
    qc.mct([a[0], a[1]], a[2])
    qc.cx(a[0], a[1])
    qc.x(a[0])
    qc.cx(a[1], a[2])
    qc.x(a[1])
    qc.barrier(b)

    vector = execute(qc, simulator).result().get_statevector()

    return vector


def probabilityComputing(input):
    pt = []
    t = CE_specification(input)
    for i in range(2048):
        temp = 0
        for j in range(8):
            temp += abs(t[i * 8 + j]) ** 2
        pt.append(temp)
    return pt


