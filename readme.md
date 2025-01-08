# Quantum Information Portfolio

This repository showcases personal projects in quantum computing and quantum information, developed using Python, and Qiskit. It explores foundational quantum protocols, algorithms, and related computational tasks, with an emphasis on quantum key distribution (QKD) and quantum algorithms.

---

## Current Content

### 1. BB84 Quantum Key Distribution Simulation
Simulates the BB84 protocol for quantum key distribution, including:
- Qubit preparation based on Alice's random bits and bases.
- Measurement by Bob using randomly chosen bases.
- Key sifting to establish a shared secret key.
- Quantum Bit Error Rate (QBER) metric.
- Analysis of the presence of an eavesdropper (Eve) and its effect on QBER.

### 2. Deutsch's Algorithm
Implements Deutsch's algorithm using Qiskit, with detailed exploration of:
- Classical and Quantum Oracles.
- Phase oracles.
- Quantum advantage.
- etc.

### 3. Superdense Coding
Explores superdense coding through implementation and theoretical analysis.
---

## Repository Structure
Most folders are currently empty, but as the project develops, the structure will follow this schema:

```plaintext
quantum-information/
│
├── src/                             # Python source code
│   ├── Q_Communication/             # Quantum Key Distribution modules
│   │   ├── qkd_errors.py            # Functions for BB84 protocol
│   │   ├── qkd.py                   # Functions for BB84 protocol
│   │   └── __init__.py              # Module initializer
│   └── __init__.py                  # Main package initializer
│
├── notebooks/                       # Jupyter notebooks for interactive exploration
│   ├── bb84_protocol.ipynb          # BB84 simulation notebook
│   ├── superdense_coding.ipynb      # Superdense coding exploration
│   └── q_algorithms/                # Notebooks exploring quantum algorithms
│       ├── deutsch.ipynb            # Deutsch algorithm implementation
│
├── tests/                           # Unit tests for key functionality
│   └── test_bb84.py                 # Unit tests for the BB84 protocol
│
├── docs/                            # Additional documentation and references
│   └── overview.md                  # Project overview and theory
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files to exclude from Git
├── LICENSE                          # License file
└── README.md                        # Project overview and instructions
```

## Installation and Usage

### Prerequisites
Described in requirements, installation instructions in installation section below

### Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/armandoperezg/quantum-information-projects
cd quantum-information-projects
pip install -r requirements.txt
```

### Running the Notebook
Open the Jupyter Notebook server and navigate to the BB84 notebook:
```bash
jupyter notebook notebooks/bb84_protocol.ipynb
jupyter notebook notebooks/bb84_protocol.ipynb
```

### Planned Features
- Add Quantum Fourier Transform, Grover's and Shor's algorithm simulations.
- Explore Quantum Error Correction
- Introduce error correction and noise models for QKD.
- Explore hardware related projects, such as:
    - Quantum Dot Simulation
    - Noise and decoherence in quantum systems simulator
    - Trapped Ion Dynamics
    - etc.
- Gradually combine them into larger systems (e.g., a quantum internet with error correction).
- Develop projects aligned with real-world experiments or research problems
- Explore Rust-Python integration for high-performance classical tasks, where relevant/needed.

### Contributing 
This repository is primarily a personal portfolio for academic and professional growth. However, contributions are welcomed! If you have any ideas for improvements or want to add features, feel free to fork the repository and submit a pull request. 

Feel free to email me at armando.perezg05@outlook.com if you have any questions or would like to discuss your ideas before contributing

## Recent Updates

- **Added Features**:
  - Deutsch's Algorithm implementation.
  - Superdense Coding exploration.
- **Utility Functions**:
  - `transpile_qc`: Transpiles a quantum circuit for a specified backend.
  - `run_circuit`: Executes a quantum circuit on a specified backend.
  - `create_noise_model`: Simulates depolarizing error based on error probabilities of single-qubit gates (`p_depol`).



## License
The project is licensed under the MIT License. See LICENSE file for details.
