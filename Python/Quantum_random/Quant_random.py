import qiskit as qk
import warnings
import os

#Load your account if running locally
# from qiskit import IBMQ
# IBMQ.save_account('YOUR_API_KEY')
### Register on IBM Quantum computing lab and there you will get your API key.

warnings.filterwarnings("ignore") #Used to ignore the Numpy deprecated warnings for the qiskit package

#Numbers are valid in range of 2^n - 1
n = 3   
q = qk.QuantumRegister(n)
c = qk.ClassicalRegister(n)
circ = qk.QuantumCircuit(q, c)
provider = qk.IBMQ.load_account()

# Circuit construction
for j in range(n):
    circ.h(q[j])

# Combining quantum and classical gates and printing it. 
circ.measure(q,c)
print(circ)

# Setting up a quantum simulator
backend = qk.BasicAer.get_backend('qasm_simulator') 

def rand_int():
    """
    Generates random number based on quantum computation.
    returns integer
    """
    new_job = qk.execute(circ, backend, shots=1)
    bitstring = new_job.result().get_counts()
    bitstring = list(bitstring.keys())[0]
    integer = int(bitstring, 2)
    return integer

print(rand_int())