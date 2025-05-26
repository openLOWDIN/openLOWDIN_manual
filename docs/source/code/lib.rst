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
  The quantum species ``E-ALPHA`` and `È-BETA`` are automatically created when requesting and ``UHF`` calculation.

.. Note::
  The mass of quantum nuclei can be selected by adding to the species symbol the isotope number followed by "_" e.g. ``H_3`` will define a Tritium nucleus.  


Basis
=====

openLOWDIN built-in basis 


Potential Basis
===============

Potentials based on Gaussian-Type functions (GTFs)
