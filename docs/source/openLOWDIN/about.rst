=====
About
=====

openLOWDIN is FORTRAN quantum chemistry code that implements the Any Particle Molecular Orbital (APMO) method to study systems containing any type and number of quantum species, such as electrons, positrons, quantum nuclei, muons, or drude oscillators. It's parallelized with OMP paradigm. 

At present, openLOWDIN code is publicly available at https://github.com/efposadac/openLOWDIN

Capabilities
============

What can we do in Lowdin? The current version of the code encompasses the following quantum chemistry methods extended for any quantum species:

* HF
* DFT
* MP2
* CI (CIS, CISD, CIST, CISDTQ, FCI, CIPSI)
* PT (PT2, PT3, PP3, RENPP3, OVGF)
* NOCI

Check more details in the :ref:`Code` and :ref:`Tutorials`

Documentation
=============

The online manual of openLOWDIN is available at https://github.com/openLOWDIN/openLOWDIN_manual.
A compiled pdf version of the manual can be found here :download:`openlowdin.pdf<../../../openlowdin.pdf>`

How to cite:
============

Please cite the code as:

`R.i Flores-Moreno, E. Posada, F. Moncada, J. Romero, J. Charry, M. Díaz-Tinoco, S.A. González, N.F. Aguirre, A. Reyes, LOWDIN: The any particle molecular orbital code. Int. J. Quantum Chem.. 114. (1), 50–56 (2014). <https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24500>`_

History
=======

openLOWDIN is the open-source version of LOWDIN code, which is the evolution of merging in 2010 two independent quantum chemistry codes and their projects. On one side, Andres Reyes’ group developed the Any Particle Molecular Orbital code known as APMO, and Roberto Flores-Moreno led the development of the electronic structure package named PARAKATA (Butterfly in Purepecha, a native language of central-west Mexico). The resulting code has been named LOWDIN as a tribute to professor Per-Olov L\"owdin for his dedication to create a global community in quantum chemistry, initiating many young Latin American scientists into this area. In the 1960, professor Löwdin founded the "International Winter Institutes" and their associated Sanibel Symposia, which were held annually at Sanibel Island, Florida, as an educational component to his renowned Summer Institutes in Uppsala, Sweden. These events provided intensive training for hundreds of scientists in the foundational principles of quantum chemistry, solid-state theory, and quantum biology, thereby significantly contributing to the international spread of quantum chemistry and inspiring generations of researchers, including the developers of this code. 


Acknowledgements
================

This code results from an evolution of the APMO and LOWDIN software packages, both mainly developed at the Universidad Nacional de Colombia. Currently, the code is under an open-source initiative thanks to the support of some developers, who are presently spread around the world!
