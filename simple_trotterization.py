import json
import pennylane as qp
import pennylane.numpy as np
dev = qp.device('default.qubit', wires = 2)

@qp.qnode(dev)
def trotterize(alpha, beta, time, depth):
    """This quantum circuit implements the Trotterization of a Hamiltonian given by a linear combination
    of tensor products of X and Z Pauli gates.

    Args:
        alpha (float): The coefficient of the XX term in the Hamiltonian, as in the statement of the problem.
        beta (float): The coefficient of the ZZ term in the Hamiltonian, as in the statement of the problem.
        time (float): Time interval during which the quantum state evolves under the interactions specified by the Hamiltonian.
        depth (int): The Trotterization depth.

    Returns:
        (numpy.array): The probabilities of measuring each computational basis state.
    """

    delta_t = time / depth
    phi_xx = 2 * alpha * delta_t
    phi_zz = 2 * beta * delta_t
    for _ in range(depth):
        qp.IsingXX(phi=phi_xx, wires=[0,1])
        qp.IsingZZ(phi=phi_zz, wires=[0,1])
    
    # Return the probabilities
    return qp.probs(wires=[0,1])

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    dev = qp.device("default.qubit", wires=2)
    ins = json.loads(test_case_input)
    output = trotterize(*ins).tolist()

    return str(output)

def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.allclose(
        solution_output, expected_output, rtol=1e-4
    ), "Your circuit does not give the correct probabilities."

    names = list(qp.specs(trotterize)(0.5,0.8,0.2,1)['resources'].gate_types.keys())

    assert names.count('ApproxTimeEvolution') == 0, "Your circuit is using the built-in PennyLane Trotterization!"
    assert names.count('Evolve') == 0, "Your circuit is using the built-in PennyLane Trotterization!"
    assert names.count('QubitUnitary') == 0, "Can't use custom-built gates!"

# These are the public test cases
test_cases = [
    ('[0.5,0.8,0.2,1]', '[0.99003329, 0, 0, 0.00996671]'),
    ('[0.9,1.0,0.4,2]', '[0.87590286, 0, 0, 0.12409714]')
]
# This will run the public test cases locally
for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")