.. _PT3 example:

=========================
PT3 for a Ps-atom complex
=========================

A PT3 (third order :ref:`PT`) input on positronium chloride (PsCl), where the electrons and the positron are treated as quantum particles looks like this

.. literalinclude:: inputs/PsCl.PT3.lowdin

APMO-PT3 calculations are performed when the option "propagatorTheoryCorrection=3" is present in the "TASKS" block. PT3 calculations only work with UHF as reference.
Here, to save computational time, only the self-energy corrections to the positron occupied orbital will be performed. This is indicated by the "ionizeSpecies", "ionizeMO" and "ptJustOneOrbital" entries in the CONTROL block.

The corresponing PT3 output will include the following summary

.. literalinclude:: out_highlights/PsCl.PT3.out

In this summary, KT is the eigenvalue of the orbital, which is the reference approximation to the particle binding energy according to Koopmans' theorem.
The EP2 row corresponds to the second order propagator theory corrected binding energy.

Currently, openLowdin computes the third order corrections with six different formulas, denoted as P3, EP3, OVGF-A, OVGF-B, OVGF-C and REN-P3.
Check J. Chem. Phys. 141, 114103 (2014) https://doi.org/10.1063/1.4895043 for the full details.

P3 and EP3 refer to the partial and full third order propagator, respectively.
The OVGF-x are the multicomponent extensions of the outer valence Green function methods, which are renormalized EP3 results.
REN-P3 is the renormalized third order partial propagator (P3).

As in PT2 calculations, the Pole Strength serves as a quantity that validates the diagonal (pseudoparticle) approximation employed. A P.S value below 0.85 usually indicates that the diagonal approximation is not reliable.

If not all the corrections are desired, you can select in the "CONTROL" block the type of correction to be used by adding "ptP3Method=" with "P3","EP3","OVGF-A","OVGF-B","OVGF-C" or "REN-P3" as options.

As in MBPT calculations, the CONTROL option "mpFrozenCoreBoundary" allows the user to omits a number of occupied electronic molecular orbitals (core electrons). For other species, the number of core orbitals along with the number of active virtuals, can be controlled with the "INPUT_CI" block in the input.
