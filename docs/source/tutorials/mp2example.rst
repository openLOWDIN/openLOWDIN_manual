.. _MP2 example:

========================
MP2 with quantum nucleus
========================

A MP2 (second order :ref:`MBPT`) input on the hydrogen fluoride molecule, where the electrons and hydrogen nucleus are treated as quantum particles should be like this

.. literalinclude:: inputs/HF.MP2.lowdin

Here, APMO-MP2 calculations are performed when the option "mollerPlessetCorrection=2" is present in the "TASKS" block. MP2 calculations may use RHF or UHF as reference.

The CONTROL option mpFrozenCoreBoundary: Omits this number of occupied electronic molecular orbitals in the MP2 calculations (core electrons). Default 0.

For other species, the number of core orbitals along with the number of active virtuals, can be controlled with the "INPUT_CI" block in the input.

A MP2 output will include the summary of the MP2 results

.. literalinclude:: out_highlights/HF.MP2.out

Where the E(2) is the second order correction to the energy, and the E(MP2) is the Hartree-Fock energy plus E(2). This summary also includes the intraspecies and interspecies contributions to E(2).		   

