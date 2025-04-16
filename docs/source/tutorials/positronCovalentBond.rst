======================
Positron covalent bond
======================

This is an example on how to compute the binding energy of a dihydride positron-bound system, using :ref:`CI` calculations, as was done in https://doi.org/10.1002/anie.201800914

.. math:: H^-e^+H^- --> PsH + H^-	  

This input computes the energy of the dihydride system

.. literalinclude:: inputs/e+H-H-.FCI-DZ.lowdin

Then, we have to subtract the energy obtained from calculations of the dissoc 	   
		    
.. literalinclude:: inputs/PsH.FCI-DZ.lowdin

.. literalinclude:: inputs/H-.FCI-DZ.lowdin
