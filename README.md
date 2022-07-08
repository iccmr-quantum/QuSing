# QuSing
## Teaching Qubits to Sing

This is the repository for accompanying materials for the paper ***Teaching Qubits to Sing: Mission Impossible?***, by Eduardo Reck Miranda and Brian N. Siegelwax.

**Abstract:** This paper introduces QuSing, a system that learns to sing new tunes by listening to examples.
QuSing extracts sequencing rules from input music and uses these rules to generate
new tunes, which are sung by a vocal synthesiser. We developed a method to represent
rules for musical composition as quantum circuits, which demonstrates that such rules are
quantum native: they are naturally encodable in the amplitudes of quantum states. Each
time the system needs to evaluate a rule to generate a subsequent event, it builds the respective
quantum circuit dynamically and mesures it. After a brief discussion about the vocal
synthesis methods that we have been experimenting with, the paper introduces our novel
generative music method by means of a practical example. The paper shows some experiments
and concludes with a discussion.

## To run the code on Jupyter notebook
For running the code, you will need Python 3.8 or later.
**Packages and dependncies:**

* `Qiskit` (v0.3.7.1)

**Note: It suggested to open your Jupyter notebook using the following line:**

jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000
