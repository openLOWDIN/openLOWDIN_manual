===
Lib
===

openLOWDIN employs external files to obtain information regarding particles properties, basis sets, and potential basis. Those files are located in the folder ``openLOWDIN/lib`` under the following tree structure:
.. code ::

  ├── basis
  ├── dataBases
  ├── libjadamilu.a
  ├── libmolden2aim.a
  ├── libtransform.a
  ├── lowdincore.a
  └── potentials

Notice that all \*.a files corresponds to static external libraries compiled during openLOWDIN installation. 


DataBases
=========

Information regarding particle properties are stored in three differents files, while ``uffParameters.lib`` contains the Universal Force Field (UFF) parameters

.. code ::

  ├── atomicElements.lib
  ├── constantsOfCoupling.lib
  ├── elementalParticles.lib
  └── uffParameters.lib

atomicElements.lib
------------------

This file stores some physicochemical for all elements in the periodic table in a Fortran namelist format.
This information is mostly used to get the charge of classical particles and number of electrons from the given atomic element, as well as the mass of quantum nuclei 

.. code :: 

  &ELEMENT
  	NAME = "HYDROGEN"
  	SYMBOL = "H"
  	ATOMICNUMBER = 1
  	MASS = 1.00794
  	MELTINGPOINT = 13.81
  	BOILINGPOINT = 20.28
  	DENSITY = 0.084
  	ELECTRONAFFINITY = -73
  	IONIZATIONENERGY1 = 1312
  	ELECTRONEGATIVITY = 2.1
  	COVALENT = 0.30
  	ATOMIC = 0.25
    KLAMT = 0.00
  	VANDERWAALS = 1.2
  	ISOTOPES = 1, 1.0078250321, 99.9885, 0.5, 
  		2, 2.0141017780, 0.0115, 1, 
  		3, 3.0160492675, 0.0, 0.5, 
  		4, 4.02783, , -2.0, 
  		5, 5.03954, , , 
  		6, 6.04494, , , 
  		7, 3.1289311806, , 1, 
  /

constantsOfCoupling.lib
-----------------------

``lambda``, ``eta``, and ``particlesFraction`` are related to the occupation of quantum species (number of particles) per orbital, this variable is used in post-HF methods and nuclear gradients. ``kappa`` is used to change the sign of the exchange integrals. See :ref:`HF`

.. code ::

  &SPECIE
  	NAME = "ELECTRON"
  	SYMBOL = "E-"
  	KAPPA = -1.0
  	ETA = 2.0
  	LAMBDA = 2.0
  	PARTICLESFRACTION = 0.5
  /

elementalParticles.lib
----------------------

this namelist defines the elemental properties of quantum particles: charge, mass, and spin

.. code ::

  &PARTICLE
  	NAME = "ELECTRON"
  	SYMBOL = "E-"
  	CATEGORY = "LEPTON"
  	CHARGE = -1
  	MASS = 1.0
  	SPIN = 0.5
  /

.. Note::
  To create a new unique (distinguishable) quantum species is necessary to add a new entry into both namelist on constantsOfCoupling.lib and elementalParticles.lib which an unique SYMBOL not used by another other quantum species

.. Note::
  openLOWDIN has three exceptions for quantum species. 
  Electrons, defined by ``"E-"``, in which the number of particles and basis set are defined by adding the atomic symbol in parenthesis, e.g. ``E-(N)`` will declare to add 7 electrons to the quantum species ``"E-"`` and to add a set of Gaussian type functions identifed by the name ``"NITROGEN"`` from the basis set requested. 
  The quantum species ``E-ALPHA`` and ``E-BETA`` are automatically created when requesting and ``UHF`` calculation.

.. Note::
  The mass of quantum nuclei can be selected by adding to the species symbol the isotope number followed by "_" e.g. ``H_3`` will define a Tritium nucleus.  


Basis
=====

openLOWDIN constructs the spatial part of spin-molecular orbitals, :math:`\varphi` as a linear combination of Gaussian type functions (GTFs), :math:`\chi_{\mu}^{\alpha}`:

.. math::
  :nowrap:

  \begin{equation}
  \varphi_i^{\alpha}(\mathbf{r}_i) = \sum_{\mu}^{N_{bas}^{\alpha}} C_{\mu}^{\alpha} \chi_{\mu}^{\alpha}(\mathbf{r}_i;\mathbf{R}_{\mu})
  \end{equation}

where :math:`C_{\mu}^{\alpha}` is a combination coefficient for species :math:`\alpha`, and the atomic orbital :math:`\chi_{\mu}^{\alpha}(\mathbf{r}_i;\mathbf{R}_{\mu})` is built as a sum of primitive functions forming a contracted orbital

.. math::
  :nowrap:

  \begin{equation}
  \chi_{\mu}^{\alpha}(\mathbf{r}_i;\mathbf{R}_{\mu}) = \sum_{s} b_{s\mu}^{\alpha} N_{s\mu}^{\alpha}
  			(x_i-X_{\mu})^{l_{\mu}^{\alpha}}(y_i-Y_{\mu})^{m_{\mu}^{\alpha}}(z_i-Z_{\mu})^{n_{\mu}^{\alpha}}
  			\times \text{exp}[ -a_s^{\alpha} (\mathbf{r}_i - \mathbf{R}_{\mu})^2 ]
  \end{equation}

here, :math:`b_{s\mu}^{\alpha}` are the primitive coefficients, :math:`N_{s\mu}^{\alpha}` is a normalization constant, :math:`\{x_i,y_i,z_i\}` are the spatial coordinates of the position vector :math:`\mathbf{r}` for the :math:`i` particle of the quantum species :math:`\alpha`, the set :math:`\{l,m.n\}` are the angular momemtum components, :math:`a_s` is the exponent, and :math:`\mathbf{R}` is the GTF center, which is independent of nuclei positions.

openLOWDIN has a collection of built-in basis stored in ``lib/basis/``. 
Please note that all filenames should be written in capital letters. 
The code employs the same basis set format of deMon2k, That is to say

.. code::  

  O-ELEMENT_NAME ELEMENT_SYMBOL_OR_SPECIES_SYMBOL (BASIS_NAME) BASIS TYPE: 1
  #
  NUMBER_OF_CONTRACTED_ORBITALS
  ID  ANGULAR_MOMEMTUM  NUMBER_OF_PRIMITIVES
  EXPONENT  COEFFICIENT

For example, for a Hydrogen atom center with aug-cc-pVDZ basis

.. code::

  O-HYDROGEN H (AUG-CC-PVDZ) BASIS TYPE: 1
  #
  5
  1 0 3
  13.01000000 0.01968500
  1.96200000 0.13797700
  0.44460000 0.47814800
  2 0 1
  0.12200000 1.00000000
  3 0 1
  0.02974000 1.00000000
  4 1 1
  0.72700000 1.00000000
  5 1 1
  0.14100000 1.00000000

Alternatively, it's possible to define the basis set of a quantum species within the ``.lowdin`` input file by creating a ``BASIS BASIS_NAME`` - ``END BASIS`` block section, where ``BASIS_NAME`` should be a basis name defined within the ``GEOMETRY`` block. For example

.. code::

  GEOMETRY
          e-[H]  cc-pvtz     0.0000  0.0000  0.00000
          e-[H]  CUSTOM_1    0.0000  0.0000  0.74144
          H_1    CUSTOM_2    0.0000  0.0000  0.00000 m=1836.1527
          U-     CUSTOM_3    0.0000  0.0000  0.74144 m=206.7683
          He_4   CUSTOM_3    0.0000  0.0000  0.74144 m=7349.6727
  END GEOMETRY
  
  BASIS CUSTOM_1
  O-HYDROGEN H (CC-PVTZ+LOCAL) BASIS TYPE: 1
  #
  9
  1 0 1
  103.8700000 1.00000000
  2 0 1
  33.8700000 1.00000000
  3 0 1
  5.09500000 1.00000000
  4 0 1
  1.15900000 1.00000000
  5 0 1
  0.32580000 1.00000000
  6 0 1
  0.10270000 1.00000000
  7 1 1
  1.40700000 1.00000000
  8 1 1
  0.38800000 1.00000000
  9 2 1
  1.05700000 1.00000000
  END BASIS

If the basis set is not provided within the input file, then the code will look in the ``lib/basis`` folder for a basis set file under the name defined in the ``GEOMETRY`` block, e.g. a file ``lib/basis/CUSTOM_1`` in the above example.

A more extensive collection of updated basis set can be found `<https://www.basissetexchange.org/>`_ or `<https://github.com/MolSSI-BSE/basis_set_exchange>`_  

Potential Basis
===============

openLOWDIN has the capabilities of computing additional one-body external potential, as well as replacing the standard two-particles Coulomb potential by a general two-body intraspecies and interspecies potentials based on sum Gaussian-Type functions (GTFs).

External potential
------------------

This potential is built as a sum of uncontracted and unnormalized GTFs 

.. math::
  :nowrap:

  \begin{equation}
  V_1^{\alpha}(\mathbf{r}_i) = \sum_{\mu}^{N_{bas}^{\alpha}} C_{\mu}^{\alpha} (x_i-X_{\mu})^{l_{\mu}^{\alpha}}(y_i-Y_{\mu})^{m_{\mu}^{\alpha}}(z_i-Z_{\mu})^{n_{\mu}^{\alpha}}
  			\times \text{exp}[ -a_{\mu}^{\alpha} (\mathbf{r}_i - \mathbf{R}_{\mu})^2 ]
  \end{equation}

where all parameters are defined in a similar fashion that the one defined for basis sets. The format of this potential basis corresponds to

.. code::  

  O-SPECIES_SYMBOL 
  #
  NUMBER_OF_FUNCTIONS
  ID  ANGULAR_MOMEMTUM
  EXPONENT  COEFFICIENT
  ORIGIN_X ORIGIN_Y ORIGIN_Z

For example, for a 4*s* potential felt by the species ``HEA3``

.. code::

  O-HEA3
  #
  25
  1 0
  0.00100000 -4.85267703e-04
  0.0 0.0 0.0
  2 0
  0.00200000 2.44420303e-03
  0.0 0.0 0.0
  3 0
  0.00400000 -7.54493346e-03
  0.0 0.0 0.0
  4 0
  0.00800000 1.57739046e-02
  0.0 0.0 0.0

In the input file, this potential is invoked by adding a new line in ``EXTERPOTENTIAL`` - ``END EXTERPOTENTIAL`` block section as

.. code::

  EXTERPOTENTIAL
         SPECIES_SYMBOL  POT_NAME
  END EXTERPOTENTIAL

where ``POT_NAME`` is the name of the potential file described above for the given species ``SPECIES_SYMBOL``. For example

.. code::

  EXTERPOTENTIAL
         HEA3   HE2C60-IH-1P
         HEB3   HE2C60-IH-1P
  END EXTERPOTENTIAL

.. note::

  Notice that it's possible to define a potential for different quantum species within the same file.


Internal potential
-------------------------------

This potential is also built as a sum of uncontracted and unnormalized geminal GTFs, but it is limited to *s*-type orbitals 

.. math::
  :nowrap:

  \begin{equation}
  V_2^{\alpha,\beta}(\mathbf{r}^{\alpha}_i,\mathbf{r}^{\beta}_j) = \sum_{\mu}^{N_{bas}^{\alpha\beta}} C_{\mu}^{\alpha\beta} \text{exp}[ -a_{\mu}^{\alpha\beta} (\mathbf{r}^{\alpha}_i - \mathbf{r}^{\beta}_{j})^2 ]
  \end{equation}

And the potential format is given by 

.. code::  

  O-SPECIES_SYMBOL_ALPHASPECIES_SYMBOL_BETA  
  #
  NUMBER_OF_FUNCTIONS
  ID  ANGULAR_MOMEMTUM
  EXPONENT  COEFFICIENT
  ORIGIN_X ORIGIN_Y ORIGIN_Z

For a 4*s* potential between two quantum species ``HEA3`` and ``HEB3``

.. code::

  O-HEA3HEB3
  4
  0 0
       10.000000000000      16.533492358000
  0.0 0.0 0.0
  1 0
        7.498942093300      -6.924850494800
  0.0 0.0 0.0
  2 0
        5.623413251900       5.780268985500
  0.0 0.0 0.0
  3 0
        4.216965034300       1.957403910100
  0.0 0.0 0.0
  4 0
        3.162277660200      -5.166130478700

In the input file, this potential is invoked by adding a new line in ``INTERPOTENTIAL`` - ``END INTERPOTENTIAL`` block section as

.. code::

  INTERPOTENTIAL
         SPECIES_SYMBOL_ALPHASPECIES_SYMBOL_BETA  POT_NAME
  END INTERPOTENTIAL

where ``POT_NAME`` is the name of the potential file described above between the species ``SPECIES_SYMBOL_ALPHA`` and ``SPECIES_SYMBOL_BETA``. For example

.. code::

  INTERPOTENTIAL
          HEA3 HEA3       HE2C60-IH-2P
          HEA3 HEB3       HE2C60-IH-2P
          HEB3 HEB3       HE2C60-IH-2P
  END INTERPOTENTIAL

.. note::

  Notice that it's possible to define a potential for different quantum species within the same file.

.. note::
  Notice that interspecies potentials can be simply declared by setting :math:`\alpha=\beta`, in other words, by setting the same quantum species symbol twice.

.. warning::
  For simplicity, openLOWDIN requires to read an angular momentum and origin for the two-body potentials, despite these are not used in the potential definition. 




