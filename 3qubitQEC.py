from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# 1. Setup Registers
# We use 3 qubits for the code and 1 classical bit for the result
q = QuantumRegister(3, 'qubit')
c = ClassicalRegister(1, 'bit')
qc = QuantumCircuit(q, c)

# --- STEP 1: ENCODING ---
# We want to protect the state |1>. 
# First, we put qubit 0 into the |1> state.
qc.x(q[0]) 

# Spread the state to qubit 1 and 2 (Encoding |1> into |111>)
qc.cx(q[0], q[1])
qc.cx(q[0], q[2])
qc.barrier()

# --- STEP 2: INTRODUCE ERROR ---
# We simulate an error by flipping qubit 1. 
# You can change this to q[0] or q[2] and the code will still work!
qc.x(q[1]) 
qc.barrier()

# --- STEP 3: DETECTION & CORRECTION ---
# We use CNOTs to check the parity between qubits.
qc.cx(q[0], q[1])
qc.cx(q[0], q[2])

# The Toffoli gate (CCX) flips qubit 0 back if BOTH q1 and q2 are 1.
# This effectively performs a "majority vote" correction.
qc.ccx(q[2], q[1], q[0])
qc.barrier()

# --- STEP 4: MEASUREMENT ---
# We measure the corrected logical qubit (q0)
qc.measure(q[0], c[0])

# --- EXECUTION ---
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts()

print("Circuit Summary:")
print(qc.draw(output='text'))
print(f"\nResults (Target state was 1): {counts}")