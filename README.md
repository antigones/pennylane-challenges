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
```
