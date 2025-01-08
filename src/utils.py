from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

def create_noise_model(p_depol=0.01):
    """
    Creates and returns a simple noise model with depolarizing errors
    for single-qubit gates.

    Features:
    - Depolarizing Error: Models a probability `p` that a single-qubit gate
      will result in a completely random state.

    Possible improvements you might add over time:
    1. Add depolarizing errors for two or more qubit gates.
    2. Introduce readout (measurement) errors.
    3. Add amplitude damping or phase damping errors.
    4. Create custom gate-specific or qubit-specific error models.
    5. Enable reset errors or combine multiple error types.
    
    Parameters: 
    - p_depol: Define depolarizing error probability for single-qubit gates

    Returns:
        NoiseModel: A Qiskit NoiseModel instance with depolarizing errors.
    """
    # Initialize a noise model
    noise_model = NoiseModel()

    # Create depolarizing error for single-qubit gates
    single_qubit_depol_error = depolarizing_error(p_depol, 1)

    # Add the error to all common single-qubit gates
    for gate in ["x", "y", "z", "h", "s", "sdg", "t", "tdg", "rx", "ry", "rz"]:
        noise_model.add_quantum_error(single_qubit_depol_error, gate, [0])  # Applies to all qubits

    return noise_model

def transpile_qc(qc, backend=None, optimization_level=1, seed_transpiler=None):
    """
    Transpiles a quantum circuit for the specified backend.

    Parameters:
        qc (QuantumCircuit): The quantum circuit to be transpiled.
        backend (Backend, optional): The target backend for transpilation.
            Defaults to an AerSimulator instance if not provided.
        optimization_level (int, optional): The level of optimization
            (0, 1, 2, or 3). Defaults to 1.
        seed_transpiler (int, optional): Seed for deterministic transpilation.

    Returns:
        QuantumCircuit: The transpiled quantum circuit.
    """
    # Default to AerSimulator if no backend is specified
    if backend is None:
        backend = AerSimulator()

    transpiled_qc = transpile(
        qc,
        backend=backend,
        optimization_level=optimization_level,
        seed_transpiler=seed_transpiler
    )
    return transpiled_qc


def run_circuit(qc, backend=None, shots=1024, noise_model=None, seed_simulator=None):
    """
    Executes a (potentially already transpiled) quantum circuit on the specified backend.

    Parameters:
        qc (QuantumCircuit): The quantum circuit to execute.
            This could be a raw or a transpiled circuit.
        backend (Backend, optional): The backend on which to run. 
            Defaults to an AerSimulator instance if not provided.
        shots (int, optional): Number of shots for the execution. Defaults to 1024.
        noise_model (NoiseModel, optional): Noise model for simulation (only valid for simulators).
        seed_simulator (int, optional): Seed for deterministic simulation results.

    Returns:
        Result: The execution result, from which you can extract counts, statevectors, etc.
    """
    if backend is None:
        from qiskit_aer import AerSimulator
        backend = AerSimulator()

    # Submit the circuit for execution
    job = backend.run(qc, shots=shots, noise_model=noise_model, seed_simulator=seed_simulator)

    # Wait for the job to complete and return the result
    result = job.result()
    return result

