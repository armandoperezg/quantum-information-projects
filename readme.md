# Quantum Information Projects

This repository showcases personal projects in quantum computing and quantum information, developed using Python, and Qiskit. It explores foundational quantum protocols, algorithms, and related computational tasks, with an emphasis on quantum key distribution (QKD) and quantum algorithms.

---

## Current Content

### 1. BB84 Quantum Key Distribution Simulation
Simulates the BB84 protocol for quantum key distribution, including:
- Qubit preparation based on Alice's random bits and bases.
- Measurement by Bob using randomly chosen bases.
- Key sifting to establish a shared secret key.
- Quantum Bit Error Rate (QBER) metric
- Presence of an eavesdropper (Eve) and it's effect on QBER metric

---

## Repository Structure
Most folders are currently empty, but as the project develops, the structure will follow this schema:

```plaintext
quantum-information/
│
├── src/                             # Python source code
│   ├── qkd/                         # Quantum Key Distribution modules
│   │   ├── bb84.py                  # Functions for BB84 protocol
│   │   └── __init__.py              # Module initializer
│   └── __init__.py                  # Main package initializer
│
├── notebooks/                       # Jupyter notebooks for interactive exploration
│   └── bb84_protocol.ipynb        # BB84 simulation notebook
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
Described in requirements, installation instrutions in installation section below

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
- Introduce error correction and noise models for QKD.
- Add Grover's and Shor's algorithm simulations.
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


### License
The project is licensed under the MIT License. See LICENSE file for details.
