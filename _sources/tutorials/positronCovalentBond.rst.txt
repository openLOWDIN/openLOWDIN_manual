.. _positronBond:

======================
Positron covalent bond
======================

This is an example on how to compute the binding energy of a dihydride positron-bound system, using :ref:`CI` calculations, as was done in https://doi.org/10.1002/anie.201800914

.. math:: [\mathrm{H}^-\mathrm{e}^+\mathrm{H}^-] \longrightarrow \mathrm{PsH} + \mathrm{H}^-	  

This input computes the energy of the dihydride system

.. literalinclude:: inputs/e+H-H-.CISDTQ-DZ.lowdin

Then, we have to subtract the energy obtained from calculations of the dissociated species
		    
.. literalinclude:: inputs/PsH.FCI-DZ.lowdin

.. literalinclude:: inputs/H-.FCI-DZ.lowdin
