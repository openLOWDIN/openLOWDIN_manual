.. _PT2 example:

========================
PT2 with quantum nucleus
========================

This is a minimal input for a second order propagator theory (:ref:`PT`) calculation to obtain the electronic ionization energies and proton binding energies for a water molecule. The PT2 corrections are computed when "propagatorTheoryCorrection=2" is added to the input:

.. literalinclude:: inputs/H2O.PT2.lowdin

The PT2 output will include a summary of the Koopmans' (KT) and self-energy corrected (EP2) results for the highest occupied and lowest unoccupied orbital of each species, 

.. literalinclude:: out_highlights/H2O.PT2.out

For the occupied orbitals, KT and EP2 results are estimates of the energy requiered to remove a particle from the corresponding orbital (ionization potential).
For the unoccupied ones, KT and EP2 results are estimates of the energy gained by adding a particle to the orbital (electron affinity).
Here, the Pole Strength (P.S) serves as a quantity that validates the diagonal (pseudoparticle) approximation employed. A P.S value below 0.85 usually indicates that the diagonal approximation is not reliable.

