# QuSing
## Teaching Qubits to Sing

This is the repository for accompanying materials for the paper ***Teaching Qubits to Sing: Mission Impossible?***, by Eduardo Reck Miranda and Brian N. Siegelwax. https://arxiv.org/abs/2207.08225

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

## Contents:
* `QuSing_Code`: contains the Jupyter Notebook code, examples of input and 2 Python programs. All these need to be in the same folder. (`midi2code.py` and `code2midi.py` are just Python functions that are called in to translate MIDI data into the bespoke representation used by the system.)

* `Audio_Examples_MP3`: Audio renderings in MP3 format of the examples in the paper.

* `Audio_Examples_WAV`: Audio renderings in WAVE format of the example in the paper.

## To run the code with Jupyter notebook
For running the code, you will need Python 3.8 or later.

This demonstration does not include vocal synthesis. The system reads a MIDI file to learn the rules, and generates a MIDI file with the new composition. There are many MIDI file players freely avaible. We like `MuseScore`, because it also shows musical notes:  https://musescore.org/en

**Packages and dependencies:**

* `qiskit`: https://qiskit.org/
* `pytket`: https://cqcl.github.io/tket/pytket/api/
* `matplotlib`: https://matplotlib.org/
* `numpy`: https://numpy.org/
* `mapomatic`: https://github.com/Qiskit-Partners/mapomatic
* `mthree`: https://github.com/Qiskit-Partners/mthree
* `mido`: https://mido.readthedocs.io/en/latest/

**Note: It suggested to open your Jupyter notebook using the following line:**

`jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000`
