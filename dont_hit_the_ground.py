import json
import pennylane as qp
import pennylane.numpy as np



def half_life(gamma, p):
    """Calculates the relaxation half-life of a quantum system that exchanges energy with its environment.
    This process is modeled via Generalized Amplitude Damping.

    Args:
        gamma (float): 
            The probability per unit time of the system losing a quantum of energy
            to the environment.
        p (float): The de-excitation probability due to environmental effect

    Returns:
        (float): The relaxation haf-life of the system, as explained in the problem statement.
    """

    num_wires = 1

    dev = qp.device("default.mixed", wires=num_wires)

    # Put your code here
    # Calculate the time t when the probability of measuring |1> is 1/4
    # Apply GAD a number of times while looking at qp.state() diagonal for |1> state to check if it's less than 1/4
    step = 0.503
    @qp.qnode(dev)
    def circuit(times_to_damp=0):
        
        qp.Hadamard(wires=0)
        for _ in range(times_to_damp):
            qp.GeneralizedAmplitudeDamping(gamma*step, p, 0, id=None)
        return qp.state()
    
    t = 0
    s = circuit(times_to_damp=t)
    while s[1][1] > 0.25:
        t+=1
        s = circuit(times_to_damp=t)   
    return t*step

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:

    ins = json.loads(test_case_input)
    output = half_life(*ins)

    return str(output)

def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.allclose(
        solution_output, expected_output, atol=2e-1
    ), "The relaxation half-life is not quite right."

# These are the public test cases
test_cases = [
    ('[0.1,0.08]', '9.00'),
    ('[0.2,0.17]', '7.05')
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