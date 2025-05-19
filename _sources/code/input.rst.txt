=====
Input
=====

General structure
=================

openLOWDIN input file consists on a plain text file with extension ``.lowdin`` which will be internally processed by a bash script to generate a Fortran namelist, creating the true input file for the code.
The input file consists of different blocks enclosed by the lines ``BLOCK`` and ``END BLOCK``, where "BLOCK" is one of the following sections:

* ``GEOMETRY``: define the position of the basis set centers, position of point charges, number and properties of quantum species.
* ``TASKS`` : select the type of calculation to be performed by the code.
* ``CONTROL``: contains all general input parameters to control the behavior of the program, such as thresholds, maximum number of SCF cycles. See :ref:`CONTROL` for a full of keywords. 
* ``OUTPUT``: request the calculation of other molecular property to visualize the molecular wave function or density. See :ref:`Outputs`
* ``BASIS`` : declare a user defined basis. This can be alternatively defined in an external file. See :ref:`Basis`
* ``INTERPOTENTIAL`` define an internal potential between pairs of quantum species. See :ref:`Potentials`
* ``EXTERPOTENTIAL`` define an external potential for a quantum species. See :ref:`Potentials`
* ``POTENTIAL`` declare a user defined potential built on gaussian type orbitals.  See :ref:`Potential Basis`
* ``INPUT_CI`` define the active space for each quantum species for CI calculations. See :ref:`CI`

GEOMETRY block
==============

The ``GEOMETRY`` block provides the information needed to build the molecular system as: ::

    GEOMETRY
    SPECIES_SYMBOL    BASIS_NAME  X_COORD Y_COORD Z_COORD 
    END GEOMETRY.

each line define either a new particle (quantum or point charge), or a new basis center (quantum particles only).

* ``SPECIES_SYMBOL`` **[character]**: It's the symbol quantum particle as defined in the ``lib/dataBases/elementalParticles.lib`` and ``lib/dataBases/constantsOfCoupling.lib`` files, or the symbol of point charges defined in ``lib/dataBases/atomicElements.lib``. See :ref:`DataBases` to define or redefine particles.
* ``BASIS_NAME`` **[character]**: For quantum particles, this corresponds to the name of the basis set, the code will look in the ``BASIS`` block or in the folder ``lib/basis``. For point charge simply use ``dirac```
* ``X_COORD``, ``Y_COORD``, ``Z_COORD`` **[real]**: Coordinates of the basis set center origin or position of the point charge. 

Besides the above mandatory elements, the following flags can be added to modify the properties of the particles declared within the same line. 

* ``addParticles=`` **[integer]** is used to modify the number of particles of a quantum species. Positive values increase number of particles, negative values decrease the number of particles. To not be confused with total charge. Default ``0``
* ``multiplicity=`` **[integer]** declare the multiplicity of the quantum species as :math:`2S+1`, where :math:`S` is the total spin within the quantum species. Default ``1``
* ``q=`` **[real]** charge of the particle, quantum or point charge. Default defined in ``lib/dataBases/elementalParticles.lib``
* ``m=`` **[real]** mass of the particle, quantum only. Default defined in ``lib/dataBases/elementalParticles.lib``
* ``omega=`` **[real]** frequency of the harmonic potential of the particle, quantum only. Default ``0.0`` See :ref:`Potentials`
* ``qdoCenterOf=`` **[character]** declare this particle as the point charge center of the quantum species in **[character]** within the QDO formalism. See :ref:`QDO`

Note that a duplicate of one of the above keywords will overwrite the previous values for particles defined with the same name.


TASKS block
===========

This block control the method to be computed

* ``method=`` **[character]** Type of Hartree-Fock method. Values: ``RHF``, ``UHF``.  Default ``"NONE"`` See :ref:`HF`
* ``optimizeGeometry=`` **[logical]** Activates geometry optimization. Default ``False``
* ``mollerPlessetCorrection=`` **[integer]** Order of Möller-Plesset Perturbation correction. Values: ``2``. Default ``0`` See :ref:`MBPT`
* ``epsteinNesbetCorrection=`` **[integer]** Order of Epstein-Nesbet correction. Values: ``2``, ``3``. Default ``0`` See :ref:`MBPT`
* ``propagatorTheoryCorrection=`` **[integer]** Order of propagator theory correction. Values: ``2``, ``3``. Default ``0`` See :ref:`PT`
* ``nonOrthogonalConfigurationInteraction=`` **[logical]** Performs non-Orthogonal Configuration Interaction calculation See :ref:`NOCI`
* ``configurationInteractionLevel=`` **[character]** Select Configuration Interaction level. Values: ``CIS``, ``CISD``, ``CISD-``, ``CISD+``, ``CISDT``, ``CISDTQ``, ``SCI``, ``FCI``. Default ``"NONE"`` See :ref:`CI`
* ``TDHF=`` **[logical]** Default ``False``
* ``cosmo=`` **[logical]** Performs an implicit solvent job using COSMO model. Default ``False``
* ``subsystemEmbedding=`` **[logical]** Default ``False``


