.. _TOEP2 example:

==========================
TOEP2 with quantum nucleus
==========================

Here, we compute the second order propagator theory (:ref:`PT`) corrections to a partially ionized water molecule electronic orbital (HOMO). The TOEP2 method requires a UHF reference. 

First, run a regular UHF calculation to generate the molecular orbitals, let's name it "H2O.UHF.lowdin". These molecular orbitals will be used as the guess for the partially ionized SCF.

.. literalinclude:: inputs/H2O.UHF.lowdin

Now, we generate the TOEP2 input, let's name it "H2O.TOEP2.lowdin". In addition to the PT2 flag, "propagatorTheoryCorrection=2", we add to the input the flag "ptTransitionOperator=T" along with "IonizeMO" and "ionizeSpecies" to select the orbital and the species, and "MOfractionOccupation" to select the occupation.

.. literalinclude:: inputs/H2O.TOEP2.lowdin

Before running this calculation, rename the molecular orbitals file "H2O.UHF.vec" to "H2O.TOEP2.vec"
		    
The output will include the summary of the P2 corrections to the partially ionized orbital

.. literalinclude:: out_highlights/H2O.TOEP2.out

This summary includes the Koopmans' (KT) and self-energy corrected (EP2) binding energy for the selected orbital. In addition, PT2 calculations with UHF reference include opposite-spin-scaled (SOS) and spin-component-scaled (SCS) results.

For the transition-operator results, the Pole Strength (P.S) value does not indicates the quality of the approximation.

