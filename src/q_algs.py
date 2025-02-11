import numpy as np

def qft(qc, n_qubits):
    '''
    Description: Circuit implementation of the quantum fourier transform. This adds the QFT circuit into an existing circuit, facilitating or enabling its use in other quantum algorithms, such as phase estimation, Shor's, etc. 
    
    Inputs:
    - qc: Quantum Circuit that the QFT is going to be appended to
    - n_qubits: Number of qubits in the qc
    
    '''
    for qubit in range(n_qubits):
        qc.h(qubit)
    
        for otherqubit in range(qubit + 1, n_qubits):
            qc.cp( np.pi / (2**(otherqubit-qubit)), otherqubit, qubit)
        
    # Now reversing the order of the output to match conventions
    for qubit in range(n_qubits // 2):
        qc.swap(qubit, n_qubits - qubit - 1)
        
    return qc


def iqft(qc, n_qubits):
    '''
    Description: Circuit implementation of the inverse quantum fourier transform. This adds the iQFT circuit into an existing circuit, facilitating or enabling its use in other quantum algorithms. 
    
    Inputs:
    - qc: Quantum Circuit that the QFT is going to be appended to
    - n_qubits: Number of qubits in the qc
    '''
    for qubit in reversed(range(n_qubits)):
        # qc.h(qubit)
    
        for otherqubit in reversed(range(qubit + 1, n_qubits)):
            qc.cp(-1*np.pi / (2**(otherqubit-qubit)), otherqubit, qubit)
        # qc.barrier()
        
        qc.h(qubit)
    
        
    # Now reversing the order of the output to match conventions
    for qubit in range(n_qubits // 2):
        qc.swap(qubit, n_qubits - qubit - 1)
        
    return qc