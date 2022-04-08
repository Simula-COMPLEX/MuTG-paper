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
    s = s.zfill(9)#input的位数
    return s

def inverse(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '0':
            s_list[i] = '1'
        else:
            s_list[i] ='0'
    s = "".join(s_list)
    return s

def QRAM(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])

    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M1(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])

    #qc.mcp(pi/6,[qram0[0],qram0[1]],addr[0])#M1

    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(2):
        qc.swap(qreg[i],qram0[i])
    qc.swap(qreg[2], qram0[2]) #M1
    for i in range(2, 4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_M1_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M2(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.cswap(qram0[1], qram1[2], addr[0])  # M2
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    #qc.ch(qram1[1],addr[0])#M2

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_M2_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_easy_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.swap(qram0[1], qram1[1])  # M3

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()


    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.cswap(qram0[1], qram1[1], qram1[2])  # M4 0.25
    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    #qc.mcp(pi/6, [qram0[1], qram1[0]], addr[0]) #M4
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()


    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    #qc.mcp(pi/6, [qram0[3], qram1[2]], addr[0]) #M5
    qc.h(addr[0])

    # qc.ch(qram1[1],addr[0])#M2

    for i in range(2):
        qc.cswap(addr[0], qram0[i], qram1[i])
    qc.cswap(qram0[1], qram1[1], qram1[2])  # M5
    for i in range(2, 4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_M2_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M6(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.cswap(qram0[2], qram1[1], qram1[3])  # M6

    qc.barrier()


    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])


    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])


    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_M3_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_easy_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(2):
        qc.swap(qreg[i], qram0[i])
    qc.swap(qreg[1], qram1[2]) #M7
    for i in range(2, 4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M4_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()
    qc.h(qreg[1])#M8 1

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_M8_circuit.txt')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.cx(qram0[0],qram0[1])  # M9

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_easy_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.cp(pi/6, qram0[0], addr[0])#M10 0.46875
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])
    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_medium_M1(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.mct([qram0[0], qram0[1], qram1[1]], qram1[2])  # M1 0.125

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_medium_M2(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.mct([qram0[1], qram0[2], qram1[1]], qram1[2])  # M2 0.125

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts



def QRAM_medium_M3(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi/6, [qram0[0], qram0[1], qram0[2], qram1[1]], addr[0]) #M3 0.0546875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])


    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_medium_M4(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi/6, [qram0[1], qram0[2], qram1[0]], addr[0]) #M4 0.1171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_medium_M5(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram1[0], qram1[3], qram0[2]], addr[0])  # M5 0.1171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_medium_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.mct([addr[0], qram0[0], qram0[1], qram0[2]], qram1[1])  # M6 0.0625
    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_medium_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram1[0], qram1[3], qram0[2], qram1[1], qram0[1]], addr[0])  # M7 0.02734375

    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_medium_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 4, [qram1[0], qram1[3], qram0[2], qram1[1], qram0[1], qram0[3]], addr[0])  # M8 0.02734375

    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_medium_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])
    qc.mct([qram0[0], qram0[1], qram1[1], qram1[3]], qram1[2])  # M9 0.0625
    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_medium_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:' + str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            #print('input ' + str(7 - i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])
    qc.mct([qram0[0], qram0[1], qram1[3], qram0[3], qram1[1]], qram1[2])  # M10 0.03125
    qc.barrier()

    qc.h(addr[0])

    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(2):
        qc.cswap(addr[0], qram0[i], qram1[i])

    for i in range(2, 4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    #circuit_drawer(qc, filename='./QRAM_M5_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M1(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[0], qram0[1], qram0[2], qram0[3], qram1[0], qram1[1], qram1[2]], addr[0])  # M1 0.00390625
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M2(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    qc.mct([addr[0], qram0[0], qram0[2], qram0[1], qram0[3], qram1[1], qram1[2], qram1[3]], qreg[1]) #M2 0

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M3(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    qc.mct([addr[0], qram0[0], qram0[2], qram0[1], qram0[3], qram1[1], qram1[2], qram1[3]], qreg[1])  # M3 0

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M4(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()



    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M5(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.h(qram0[2]) #M5 0

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.mct([qram0[0], qram0[1], qram0[2], qram0[3], qram1[0], qram1[1], qram1[2]], qram1[3])  # M6 0.0078125

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[2], qram0[1], qram0[0], qram0[3], qram1[3], qram1[1]], addr[0])  # M7 0.01171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[2], qram0[1], qram0[0], qram0[3], qram1[3], qram1[1], qram1[2]], addr[0])  # M8 0.00390625
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 4, [qram0[2], qram0[0], qram0[3], qram1[3], qram1[1], qram1[2]], addr[0])  # M9 0.01171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.swap(qreg[0], qreg[1])  # M10 0

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_difficult1_M1(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[0], qram0[1], qram0[2], qram0[3], qram1[0], qram1[1], qram1[2]], addr[0])  # M1 0.00390625
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M2(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.mct([qram0[3], qram0[2], qram0[1], qram0[0], qram1[3], qram1[1], qram1[2]], qram1[0])  # M2 0.0078125
    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])



    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M3(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    qc.mct([qram0[2], qram0[1], qram0[3], qram0[0], qram1[3], qram1[0], qram1[1]], qram1[2])  # M3 0.0078125
    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M4(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])
    qc.mct([qram0[3], qram0[1], qram1[1], qram0[0], qram1[3], qram1[0], qram1[2]], qram0[2])  # M4 0.0078125
    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M5(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 4, [qram0[1], qram0[2], qram0[3], qram0[0], qram1[0], qram1[1], qram1[2]], addr[0])  # M5 0.00390625
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])


    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.mct([qram0[0], qram0[1], qram0[2], qram0[3], qram1[0], qram1[1], qram1[2]], qram1[3])  # M6 0.0078125

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[2], qram0[1], qram0[0], qram0[3], qram1[3], qram1[1]], addr[0])  # M7 0.01171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[2], qram0[1], qram0[0], qram0[3], qram1[3], qram1[1], qram1[2]], addr[0])  # M8 0.00390625
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 4, [qram0[2], qram0[0], qram0[3], qram1[3], qram1[1], qram1[2]], addr[0])  # M9 0.01171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult1_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.swap(qreg[0], qreg[1])  # M10 0

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts


def QRAM_difficult3_M1(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[0], qram0[1], qram0[2], qram0[3], qram1[0], qram1[1], qram1[2]], addr[0])  # M1 0.00390625
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M2(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.mct([qram0[3], qram0[2], qram0[1], qram0[0], qram1[3], qram1[1], qram1[2]], qram1[0])  # M2 0.0078125
    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])



    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M3(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    qc.mct([qram0[2], qram0[1], qram0[3], qram0[0], qram1[3], qram1[0], qram1[1]], qram1[2])  # M3 0.0078125
    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M4(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])
    qc.mct([qram0[3], qram0[1], qram1[1], qram0[0], qram1[3], qram1[0], qram1[2]], qram0[2])  # M4 0.0078125
    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M5(input,count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    #print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            #print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            #print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 4, [qram0[1], qram0[2], qram0[3], qram0[0], qram1[0], qram1[1], qram1[2]], addr[0])  # M5 0.00390625
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])
    qc.x(qreg[0])


    qc.barrier()

    qc.measure(qreg,c)


    #circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc,simulator,shots = count_times*100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M6(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])


    qc.barrier()

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    qc.mct([addr[0], qram0[0], qram0[2], qram0[1], qram0[3], qram1[1], qram1[2], qram1[3]], qreg[1])  # M6 0

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M7(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 6, [qram0[2], qram0[1], qram0[0], qram0[3], qram1[3], qram1[1]], addr[0])  # M7 0.01171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M8(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])

    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()
    qc.mct([addr[0], qram0[1], qram0[2], qram0[3], qram1[0], qram1[1], qram1[2], qram1[3]], qreg[1])  # M8 0
    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M9(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.mcp(pi / 4, [qram0[2], qram0[0], qram0[3], qram1[3], qram1[1], qram1[2]], addr[0])  # M9 0.01171875
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_difficult3_M10(input, count_times):
    simulator = Aer.get_backend('qasm_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    # print('input:'+str(input_string))
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7 - i] == '1':
            # print('input '+ str(7-i) + '=1')
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3 - i] == '1':
            # print('input ' + str(3 - i) + '=1')
            qc.x(qram1[i])

    qc.barrier()

    qc.swap(qreg[0], qreg[1])  # M10 0

    qc.h(addr[0])
    qc.p(pi / 3, addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0], qram0[i], qram1[i])

    qc.barrier()

    for i in range(4):
        qc.swap(qreg[i], qram0[i])

    qc.barrier()

    for i in range(3):
        control = []
        for j in range(3 - i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3 - i])
    qc.x(qreg[0])

    qc.barrier()

    qc.measure(qreg, c)

    # circuit_drawer(qc, filename='./QRAM_circuit')

    job = execute(qc, simulator, shots=count_times * 100)
    result = job.result()
    counts = result.get_counts(qc)

    return counts

def QRAM_specification(input):
    simulator = Aer.get_backend('statevector_simulator')
    qreg = QuantumRegister(4)
    addr = QuantumRegister(1)
    qram0 = QuantumRegister(4)
    qram1 = QuantumRegister(4)
    c = ClassicalRegister(4)

    qc = QuantumCircuit(qreg, addr, qram0, qram1, c)

    input_string = dec2bin(input)
    if input_string[8] == '1':
        qc.x(addr[0])
    for i in range(4):
        if input_string[7-i] == '1':
            qc.x(qram0[i])
    for i in range(4):
        if input_string[3-i] == '1':
            qc.x(qram1[i])

    qc.barrier()

    qc.h(addr[0])
    qc.p(pi/3,addr[0])
    qc.h(addr[0])

    for i in range(4):
        qc.cswap(addr[0],qram0[i],qram1[i])

    qc.barrier()


    for i in range(4):
        qc.swap(qreg[i],qram0[i])

    qc.barrier()


    for i in range(3):
        control = []
        for j in range(3-i):
            control.append(qreg[j])
        qc.mcx(control, qreg[3-i])

    qc.x(qreg[0])

    qc.barrier()

    vector = execute(qc, simulator).result().get_statevector()

    return vector




def probabilityComputing(input):
    pt = []
    t = QRAM_specification(input)
    for i in range(16):
        temp = 0
        for j in range(512):
            temp += abs(t[j*16+i])**2
        pt.append(temp)
    return pt



