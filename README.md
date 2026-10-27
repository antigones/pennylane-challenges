# PennyLane Challenges

A collection of quantum computing challenges from the [PennyLane website](https://pennylane.ai/). These challenges cover various quantum algorithms and techniques using the PennyLane framework.

## Challenges

### 1. **Don't Hit the Ground** (`dont_hit_the_ground.py`)
Calculates the relaxation half-life of a quantum system that exchanges energy with its environment. The challenge uses Generalized Amplitude Damping (GAD) to model energy loss to the environment and determines the time at which the probability of measuring the |1⟩ state drops to 25%.

**Key Concepts:**
- Generalized Amplitude Damping channel
- Quantum decoherence
- Mixed state evolution

### 2. **Ising Uprising** (`ising_uprising.py`)
Implements a Variational Quantum Eigensolver (VQE) to find the ground state of a transverse Ising model. The challenge involves:
- Creating a Hamiltonian for a transverse Ising model on a chain with 4 qubits
- Designing a VQE ansatz with parameterized gates
- Optimizing the circuit parameters to find the minimum eigenvalue

**Key Concepts:**
- Variational Quantum Eigensolver (VQE)
- Transverse Ising model
- Quantum circuit optimization
- Parameter optimization

### 3. **Keep Expectations Low** (`keep_expectations_low.py`)
Optimizes a variational quantum circuit to minimize the expectation value of a given Hamiltonian. The circuit uses strongly entangling layers with parameterized single-qubit and two-qubit gates.

**Key Concepts:**
- Variational quantum circuits
- Strongly entangling layers
- Gradient-based optimization
- Hamiltonian expectation values

### 4. **Hydro Bonding** (`hydro_bonding.py`)
Uses the Variational Quantum Eigensolver (VQE) to estimate the ground-state energy of a hydrogen molecule at different atomic separations. The circuit is prepared from a Hartree-Fock state and optimized with single and double excitations.

**Key Concepts:**
- Molecular Hamiltonians and quantum chemistry
- Hartree-Fock state preparation
- VQE and excitation-based ansätze

### 5. **Simple Trotterization** (`simple_trotterization.py`)
Simulates time evolution under a Hamiltonian composed of XX and ZZ interactions by applying a first-order Trotter step repeatedly, then returns the computational-basis probabilities.

**Key Concepts:**
- Hamiltonian time evolution
- Trotter-Suzuki approximation
- IsingXX and IsingZZ gates

### 6. **Returning Probabilities** (`returning_probabilities.py`)
Applies an RX rotation to an initial qubit state and returns the probabilities of the computational-basis outcomes.

**Key Concepts:**
- PennyLane QNodes
- Parameterized rotation gates
- Probability measurements

### 7. **Undo That Computation** (`undo_that_computation.py`)
Implements a reversible quantum circuit for the classical AND operation using phase kickback and measures the result.

**Key Concepts:**
- Reversible logic
- Controlled operations
- Phase kickback

### 8. **States and Probabilities** (`states_and_probabilities.py`)
Builds a single-qubit state-vector simulation: initialize the |0⟩ state, apply a unitary, and sample computational-basis measurements.

**Key Concepts:**
- State-vector representation
- Unitary operations
- Sampling and measurement

### 9. **My First Quantum Simulation** (`my_first_quantum_simulation.py`)
Creates a two-qubit circuit with RX rotations and returns the probabilities of the computational-basis states.

**Key Concepts:**
- Quantum circuit construction
- RX rotations
- Multi-qubit probability measurements

### 10. **Universality of Quantum Gates** (`universality_of_quantum_gates.py`)
Trains parameters for a sequence of single-qubit rotations and a global phase to reproduce a target unitary matrix.

**Key Concepts:**
- Single-qubit gate decompositions
- Matrix representation of quantum circuits
- Gradient-based parameter optimization

## Requirements

- Python 3.7+
- PennyLane

## Installation

Install the required packages:

```bash
pip install pennylane
```

## Running the Challenges

Each challenge can be run as a standalone script:

```bash
python3 dont_hit_the_ground.py
python3 ising_uprising.py
python3 keep_expectations_low.py
python3 hydro_bonding.py
python3 simple_trotterization.py
python3 returning_probabilities.py
python3 undo_that_computation.py
python3 states_and_probabilities.py
python3 my_first_quantum_simulation.py
python3 universality_of_quantum_gates.py
```
