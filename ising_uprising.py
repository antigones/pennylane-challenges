import json
import pennylane as qp
import pennylane.numpy as np

def create_Hamiltonian(h):
    """
    Function in charge of generating the Hamiltonian of the statement.

    Args:
        h (float): magnetic field strength

    Returns:
        (qp.Hamiltonian): Hamiltonian of the statement associated to h
    """
    # Put your code here #

    return qp.spin.transverse_ising("chain", [4], coupling=1, h=h, boundary_condition=True)

dev = qp.device("default.qubit", wires=4)

@qp.qnode(dev)
def model(params, H):
    """
    To implement VQE you need an ansatz for the candidate ground state!
    Define here the VQE ansatz in terms of some parameters (params) that
    create the candidate ground state. These parameters will
    be optimized later.

    Args:
        params (numpy.array): parameters to be used in the variational circuit
        H (qp.Hamiltonian): Hamiltonian used to calculate the expected value

    Returns:
        (float): Expected value with respect to the Hamiltonian H
    """

    # Put your code here #
    qp.RY(params[0], wires=0)
    qp.RY(params[1], wires=1)
    qp.RY(params[2], wires=2)
    qp.RY(params[3], wires=3)

    qp.CZ(wires=[0, 1])
    qp.CZ(wires=[1, 2])
    qp.CZ(wires=[2, 3])
    qp.CZ(wires=[3, 0])

    # Second layer of RY rotations
    qp.RY(params[4], wires=0)
    qp.RY(params[5], wires=1)
    qp.RY(params[6], wires=2)
    qp.RY(params[7], wires=3)

    # Second layer of CZ entangling gates
    qp.CZ(wires=[0, 1])
    qp.CZ(wires=[1, 2])
    qp.CZ(wires=[2, 3])
    qp.CZ(wires=[3, 0])

    return qp.expval(H)

def train(h):
    """
    In this function you must design a subroutine that returns the
    parameters that best approximate the ground state.

    Args:
        h (float): magnetic field strength

    Returns:
        (numpy.array): parameters that best approximate the ground state.
    """

    # Put your code here #

    H = create_Hamiltonian(h)

    # Initialize parameters randomly
    params = np.random.rand(8, requires_grad=True)

    # Define optimizer
    opt = qp.GradientDescentOptimizer(stepsize=0.1)

    # Number of optimization steps
    steps = 100

    # Optimization loop
    for _ in range(steps):
        params = opt.step(model, params, H=H)

    return params


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    params = train(ins)
    return str(model(params, create_Hamiltonian(ins)))


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    print(solution_output)
    print(expected_output)
    assert np.allclose(
        solution_output, expected_output, rtol=1e-1
    ), "The expected value is not correct."

# These are the public test cases
test_cases = [
    ('1.0', '-5.226251859505506'),
    ('2.3', '-9.66382463698038')
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
