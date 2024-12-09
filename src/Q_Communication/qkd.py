"""
This library contains all of the functions used in the bb84_protocol.ipynb jupyter notebook in the notebooks folder. 


Some possible optimizations are: 
- In the function run_circuits, the circuits for each generated combination of bases and qubits are transpiled, simulated and measured. When the number of bits sent is large, it is likely that a lot of the individually prepared circuits are identical to another previously prepared. Thus, the program could potentially store the permutations, or even store this before the program is ran, to significantly reduce computational complexity. This would avoid unnecessary transpiling, simulating, and perhaps measurement of circuits, which should be the highest contributor of execution time, and thus could represent a bottleneck. 
"""


# Third-party imports
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator

from src.Q_Communication.qkd_errors import qber


def initialize(n_bits, Eve):
    """ 
    Randomly generates the qubits and the bases used by Alice and Bob, as well as the circuits where the different bases and bits will be simulated

    This function initializes the simulation by generating random bits for Alice and random bases for both Alice and Bob. 
    Bases are represented as integers, where '0' denotes the rectilinear basis and '1' denotes the diagonal (Hadamard) basis.

    """
    Alice_bits = np.random.randint(2,size=n_bits)
    Alice_bases = np.random.randint(2,size=n_bits)
    Bob_bases = np.random.randint(2,size=n_bits)
    
    circuits = []
    
    for i in range(n_bits):
        circuits.append(QuantumCircuit(1,1 + Eve))
        
    Bases = []
    Bases.append(Alice_bases)
    Bases.append(Bob_bases)
    
    if Eve == True:
        Eve_bases = np.random.randint(2,size=n_bits)
        Bases.append(Eve_bases)
    
    
    return Alice_bits, Bases, circuits

def Alice_qc(Alice_bits, Alice_bases, circuits):
    """ 
    Prepare quantum circuits for Alice based on her bits and chosen bases.

    Each circuit is prepared according to the value of the bit and the basis:
    - If the bit is 1, an X gate (Pauli-X) is applied to flip the qubit from 0 to 1.
    - If the basis is 1 (Hadamard basis), a Hadamard (H) gate is applied to put the qubit into superposition.
    Otherwise, the qubit is prepared in the standard basis without any additional gates for a bit of 0.
    This function edits the circuits in place.

    """

    for bit, Alice_basis, qc in zip(Alice_bits, Alice_bases, circuits):
        if bit == 1:
            qc.x(0)
        if Alice_basis == 1:
            qc.h(0)

        
    
    return None


def Eve_qc(circuits, Eve_bases):
    """
    This function uses Eve's randomly chosen measurement basis to eavesdrop on the transmitted bits. It attemps to minimize detection by sending out the bit that was measured given the measurement basis used. 

    Args:
        circuits (array): Reference to the circuits array that stores the circuits for each permutation of bases and bits. This is used to edit the array in place and add Eve's measurement (and hence collapse), as well as her choice of basis.
        Eve_bases (array): Determines if Eve chooses a rectilinear (0) or diagonal basis (1) for each circuit

    Returns:
        None: The circuits are edited in place, therefore there is no need to return them.
    """
    for qc, Eve_basis in zip(circuits, Eve_bases):
        if Eve_basis == 1:
            qc.h(0)
            qc.measure(0, 1)
            qc.h(0)
        else:
            qc.measure(0, 1)
    return None


def Bob_qc(circuits, Bob_bases):
    """ 
    Prepare and measure quantum circuits based on Bob's chosen measurement bases.

    This function processes a list of quantum circuits by applying the necessary basis transformation and measurement operations according to Bob's bases. For each circuit:
    - If Bob's basis is 1 (diagonal basis), a Hadamard gate (H) is applied to transform the basis from the computational (Z) to the diagonal (X) basis.
    - Every qubit is then measured in its respective basis, with the measurement result being stored in a classical bit.

    The function modifies the circuits in-place and does not return any value.

    """
    if len(circuits) != len(Bob_bases):
        raise RuntimeError("circuits and Bob_bases should have the same length")
    
    for qc, Bob_basis in zip(circuits, Bob_bases):
        # Bob prepares the measurement and basis
        if Bob_basis == 1:
            qc.h(0)
            
        qc.measure(0, 0) # Bob measures the qubit and stores the result in clbit  
          
    return None

        
def run_circuits(circuits, Eve):
    """ 
    Simulate a quantum circuit and return the measurement outcome.

    This function takes a quantum circuit, transpiles it for optimal performance on a simulator, and then runs the simulation to measure the state of the qubit. It returns the outcome of this measurement. The simulation is run with only one measurement shot to directly observe the state of the qubit.
    """
    
    # Simulate the circuit
    simulator = AerSimulator()
    
    measurements = [[]]
    if Eve == True:
        measurements.append([])
    for qc in circuits:
        transpiled_qc = transpile(qc) # Transpile optimizes circuits, adapts it to real world devices
        result = simulator.run(transpiled_qc, shots=1).result()
        counts = result.get_counts()
        measured_bits = list(counts.keys())[0]  # Get the measurement outcome, returns an str
        
  
        measurements[0].append(int(measured_bits[0]))
        if Eve == True:
            measurements[1].append(int(measured_bits[1]))
            
    # print(measured_bits)
    
    return measurements


def sift_key(Alice_bits, Alice_bases, Bob_bases, measured_bits):
    ''' 
    Generate the secret key from matched bases between Alice and Bob.

    This function compares the bases used by Alice and Bob to determine where they match. If the bases match, it means that the corresponding bits (from Alice's original bits and Bob's measured bits) are used to form part of the secret key. This sifting process is crucial in quantum key distribution (QKD) to ensure that both parties have identical keys formed from bits that were reliably transmitted and measured under the same basis.
    
    It is important to return both Alice's key and Bob's key, as errors or Eve can introduce differences in the bits sent by Alice, and the bits recieved or measured by Bob. It allows us to perform more realistic analysis and simulation, as well as integrate better with future functionality. 

    '''
    Alices_key = []
    Bobs_key = [] 
    matching_indices = []
    for i in range(len(Alice_bits)):
        if Alice_bases[i] == Bob_bases[i]:
            Alices_key.append(Alice_bits[i])
            Bobs_key.append(measured_bits[i])
            matching_indices.append(i)
            
    return Alices_key, Bobs_key, matching_indices



def bb84_qkd(n_bits, Eve=False):
    """ 
    Simulate the BB84 quantum key distribution protocol to generate a shared secret key.

    This function simulates the BB84 protocol by:
    1. Initializing random bits and bases for Alice and random bases for Bob.
    2. Creating quantum circuits based on Alice's bits and bases, which are then sent to Bob.
    3. Adding the eavesdropper (Eve) to the circuit, her random basis, and her measurement.
    4. Bob measures the received qubits using his bases.
    5. Both Alice and Bob use the sifting process to extract a shared secret key from bits measured under matching bases.

    The simulation prints each step, showing the bit sent by Alice, the bases used by both, and the bit measured by Bob. This allows for tracing the protocol's progress and understanding how mismatches and errors affect the final key.

    """
    
    Alice_bits, Bases, circuits = initialize(n_bits, Eve)
    
    Alice_qc(Alice_bits, Bases[0], circuits)
    if Eve == True:
        Eve_qc(circuits, Bases[2])
    Bob_qc(circuits, Bases[1])
    
    
    measured_bits = []
    Alice_bases = Bases[0]; Bob_bases = Bases[1]
    measurements = run_circuits(circuits, Eve)
    # for bit, Alice_basis, Bob_basis, qc in zip(Alice_bits, Alice_bases, Bob_bases, circuits):
    #     measured_bit = run_circuits(qc)
    #     measured_bits.append(measured_bit)
    #     print(f"The bit sent by Alice was: {bit}")
    #     print(f"The basis used by Alice was: {Alice_basis}")
    #     print(f"The basis used by Bob was: {Bob_basis}")
    #     print(f"The measured bit was: {measured_bit} \n")
        
    Alice_key, Bob_key, matching_indices = sift_key(Alice_bits, Bases[0], Bases[1], measurements[0])
    Alice_key = list(map(int, Alice_key))
    
    print(f"The QBER metric is: {qber(Alice_key, Bob_key)}")

    return Alice_key, Bob_key, matching_indices



if __name__ == "__main__":
    Alice_key, Bob_key, matching_indices = bb84_qkd(Eve=True)
    print(list(map(int, Alice_key)))
    print(Bob_key)
    print(f"The matching indices were: {matching_indices}")