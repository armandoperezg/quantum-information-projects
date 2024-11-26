""" 
Possible future implementations

1. Simulate Errors, which are relevant in real-world experiments

2. Implement Error Correction and Primary Amplification

3. Metrics Implementation
"""



# Metrics

def qber(Alice_bits, Bob_bits):
    """
    Quantum Bit Error Rate: This function is a metric for QKD, such as the BB84 notebook. It quantifies the number of erroneous bits recieved to the total of bits sent. It indicates how well the system can maintain the integrity of the quantum information transmitted against noise and eavesdropping. This metric characterizes the efficiency and security of the cryptographic protocol. This metric is applied before error correction, unlike KMR (Key Mismatch Rate). 

    Args:
        Alice_bits (_type_): List of the bits Alice sent, when the bases of Alice and Bob were the same
        Bob_bits (_type_): List of the bits Bob measured, when the bases of Alice and Bob were the same
    
    Returns: 
        Erroneous_bits/length of key
    """
    if len(Alice_bits) != len(Bob_bits):
        raise RuntimeError("The length of the inputs list differs")
    
    erroneous_bits = 0
    for a, b in zip(Alice_bits, Bob_bits):
        if a != b:
            erroneous_bits += 1
    
    return erroneous_bits/len(Alice_bits)