import warnings
from decouple import config
import qiskit as qk

#Load your account if running locally
### Register on IBM Quantum computing lab and there you will get your API key.
api_key = config("API_KEY")
qk.IBMQ.save_account(api_key)
#Used to ignore the Numpy deprecated warnings for the qiskit package
warnings.filterwarnings("ignore")

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
circ.measure(q, c)
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

def main():
    print(rand_int())

if __name__ == "__main__":
    main()
