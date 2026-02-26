import pennylane as qml

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def h_then_x():
    qml.Hadamard(wires=0)
    qml.PauliX(wires=0)
    return qml.probs(wires=[0, 1])

@qml.qnode(dev)
def x_then_h():
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    return qml.probs(wires=[0, 1])

@qml.qnode(dev)
def h_cnot_x():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    qml.PauliX(wires=0)
    return qml.probs(wires=[0, 1])


@qml.qnode(dev)
def x_h_cnot():
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

@qml.qnode(dev)
def create_bell_state():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0])


def print_distribution(title, probs):
    basis_states = ["00", "01", "10", "11"]
    print(f"\n{title}")
    for state, probability in zip(basis_states, probs):
        print(f"P(|{state}⟩) = {probability:.6f}")


if __name__ == "__main__":
    distributions = {
        "H → X": h_then_x(),
        "X → H": x_then_h(),
        "H → CNOT → X": h_cnot_x(),
        "X → H → CNOT": x_h_cnot(),
    }

    for name, probs in distributions.items():
        print_distribution(name, probs)

    bell_state_probs = create_bell_state()
    print_distribution("Bell State (H → CNOT)", bell_state_probs)