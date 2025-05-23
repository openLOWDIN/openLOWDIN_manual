.. _molden example:

===============
Molden examples
===============

Running the following input of positronic glycine

.. literalinclude:: inputs/Gly.e+-molden.lowdin

Produces two molden files, one for the electrons and one for the positron, their filenames are provided in the output.

.. literalinclude:: out_highlights/Gly.e+-molden.out

These files contain the the electronic and positronic orbitals. We can visualize these orbitals using the molden software (https://www.theochem.ru.nl/molden/ ), as observed in the following figure

.. image:: ../_static/images/positronicGlycineOrbitals.jpg
   :alt: Molden files from Gly.e+-molden.out
   :width: 600px

---------------------------------
Localized orbitals and fchk files
---------------------------------
		    
Localized orbitals are generated with the Erkale software (https://github.com/susilehtola/erkale ), adding the following lines in the CONTROL block 		    
		    
.. literalinclude:: inputs/Gly.e+-localize-molden.lowdin

Here with "MU" we selected the Pipek-Mozay localization scheme using Mulliken charges. Check Erkale manual for a full list of the localization procedures available.
To transfer the orbitals to Erkale, openLowdin generates fchk files. In the output, you will find the Erkale localization log.

.. literalinclude:: out_highlights/Gly.e+-localize-molden.out

For this example, the localization procedure only affects the electronic orbitals, because there is only a single positronic orbital.
When localized orbitals are requested, openlowdin will generate the molden files with them. Check in the following figure a comparison between the non-localized (right) and localized (left) HOMO of positronic glycine

.. image:: ../_static/images/positronicGlycineLocalizedOrbitals.jpg
   :alt: Molden files from Gly.e+-molden.out and Gly.e+-localize-molden.out
   :width: 600px

-----------------
CI excited states
-----------------
When we run a configuration interaction calculation we can generate molden files for the excited states. For example, in the :ref:`positronBond` (e+H-H-.CISDTQ-DZ.lowdin) example we added "state=2" to get the natural orbitals of the first excited state. In the output of that calculation we find

.. literalinclude:: out_highlights/e+H-H-.CISDTQ-DZ.out_MOLDEN

In the following figure we plot the positronic natural orbitals with the highest contributions to the ground (right) and first excited (left) states

.. image:: ../_static/images/positronBondNaturalOrbitals.jpg
   :alt: Molden files from e+H-H-.CISDTQ-DZ
   :width: 1000px






