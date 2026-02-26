import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def half_adder(a: int, b: int):
    # Input encoding
    if a == 1:
        qml.PauliX(wires=0)  # q0 = a
    if b == 1:
        qml.PauliX(wires=1)  # q1 = b

    # Carry first: q2 = a AND b
    qml.Toffoli(wires=[0, 1, 2])

    # Sum second: q1 = a XOR b
    qml.CNOT(wires=[0, 1])

    # Read SUM on q1, CARRY on q2
    return qml.probs(wires=[1, 2])

def decode_sum_carry(probs):
    # Basis order for wires [1,2]: |00>, |01>, |10>, |11>
    idx = int(np.argmax(probs))
    sum_bit = idx // 2
    carry_bit = idx % 2
    return sum_bit, carry_bit

def run_tests():
    print("a b | SUM CARRY")
    print("----+----------")
    for a in [0, 1]:
        for b in [0, 1]:
            probs = half_adder(a, b)
            s, c = decode_sum_carry(probs)
            print(f"{a} {b} |  {s}    {c}")

if __name__ == "__main__":
    run_tests()

    # Optional bonus: circuit visualization
    print("\nCircuit (example a=1, b=1):")
    print(qml.draw(half_adder)(1, 1))