=======
CONTROL
=======

Dummy variables
===============

For debugging purposes

* ``dummyReal(:)=`` *[float]*
  Dummy real array(10).  *Default* ``0.0_8``

* ``dummyInteger(:)=`` *[integer]*
  Dummy integer array(10). *Default* ``0``

* ``dummyLogical(:)=`` *[logical]*
  Dummy logical array(10). *Default* ``.false.``

* ``dummyCharacter(:)=`` *[character]*
  Dummy character array(10). *Default* ``""``

Geometry optimization
=====================

Currenly unsupported

* ``numericalDerivativeDelta=`` *[float]*
  *Default* ``1.0E-3``

* ``minimizationInitialStepSize=`` *[float]*
  *Default* ``0.5_8``

* ``minimizationLineTolerance=`` *[float]*
  *Default* ``0.001_8``

* ``minimizationToleranceGradient=`` *[float]*
  *Default* ``0.00001_8``

* ``minimizationMaxIteration=`` *[integer]*
  *Default* ``200``

* ``minimizationMethod=`` *[integer]*
  *Default* ``4``

* ``minimizationLibrary=`` *[character]*
  *Default* ``"GENERIC"``

* ``coordinates=`` *[character]*
  *Default* ``"CARTESIAN"``

* ``energyCalculator=`` *[character]*
  *Default* ``"INTERNAL"``

* ``analyticGradient=`` *[logical]*
  *Default* ``.true.``

* ``minimizationWithSinglePoint=`` *[logical]*
  *Default* ``.true.``

* ``useSymmetryInMatrices=`` *[logical]*
  *Default* ``.false.``

* ``restartOptimization=`` *[logical]*
  *Default* ``.false.``

* ``firstStep=`` *[logical]*
  *Default* ``.true.``

* ``lastStep=`` *[logical]*
  *Default* ``.true.``

* ``optimizeWithCpCorrection=`` *[logical]*
  *Default* ``.false.``

* ``cpCorrection=`` *[logical]*
  *Default* ``.false.``

* ``TDHF=`` *[logical]*
  *Default* ``.false.``

* ``optimize=`` *[logical]*
  *Default* ``.false.``

* ``optimizeGeometryWithMP=`` *[logical]*
  *Default* ``.false.``

* ``projectHessiane=`` *[logical]*
  *Default* ``.true.``

Atomic connectivity
===================

Currenly unsupported

* ``bondDistanceFactor=`` *[float]*
  *Default* ``1.3_8``

* ``bondAngleThreshold=`` *[float]*
  *Default* ``170.0_8``

* ``dihedralAngleThreshold=`` *[float]*
  *Default* ``170.0_8``

COSMO
=====

Currenly unsupported

* ``cosmo=`` *[logical]*
  *Default* ``.false.``

* ``cosmo_solvent_dielectric=`` *[character]*
  *Default* ``78.3553d+00``

* ``cosmo_scaling=`` *[character]*
  *Default* ``0.0d+00``

Info and units
==============
    
* ``formatNumberOfColumns=`` *[integer]*
  *Default* ``5``

* ``unitForOutputFile=`` *[integer]*
  *Default* ``6``

* ``unitForMolecularOrbitalsFile=`` *[integer]*
  *Default* ``8``

* ``unitForMP2IntegralsFile=`` *[integer]*
  *Default* ``7``

* ``printLevel=`` *[integer]*

  .. list-table::
    :widths: 10 75
    :header-rows: 0

    * - ``0``
      - No output
    * - ``1``
      - Normal. *Default*
    * - ``5``
      - Method 
    * - ``6``
      - Method and wave function
    * - ``7``
      - Method, wave function, global
    * - ``8``
      - Method, wave function, global, SCF

* ``units=`` *[character]*
  *Default* ``"ANGS"``

* ``doubleZeroThreshold=`` *[float]*
  *Default* ``1.0E-12``

General
=======

* ``method=`` *[character]*
  *Default* ``"NONE"``

* ``transformToCenterOfMass=`` *[logical]*
  *Default* ``.false.``

* ``areThereDummyAtoms=`` *[logical]*
  *Default* ``.false.``

* ``areThereQDOPotentials=`` *[logical]*
  *Default* ``.false.``

* ``setQDOEnergyZero=`` *[logical]*
  *Default* ``.false.``

* ``isThereExternalPotential=`` *[logical]*
  *Default* ``.false.``

* ``isThereInterparticlePotential=`` *[logical]*
  *Default* ``.false.``

* ``isThereOutput=`` *[logical]*
  *Default* ``.false.``

* ``isThereFrozenParticle=`` *[logical]*
  *Default* ``.false.``

* ``dimensionality=`` *[integer]*
  *Default* ``3``

Molecular Mechanics
===================

Currenly unsupported

* ``forceField=`` *[character]*
  *Default* ``"UFF"``

* ``electrostaticMM=`` *[logical]*
  *Default* ``.false.``

* ``chargesMM=`` *[logical]*
  *Default* ``.false.``

* ``printMM=`` *[logical]*
  *Default* ``.false.``

Miscelaneous options
====================

* ``MOFractionOccupation=`` *[float]*
  *Default* ``1.0_8``

* ``ionizeMO=`` *[integer]*
  *Default* ``0``

* ``ionizeSpecies=`` *[character]*
  *Default* ``"NONE"``

* ``exciteSpecies=`` *[character]*
  *Default* ``"NONE"``

Integrals transformation
========================

* ``integralsTransformationMethod=`` *[character]*
  *Default* ``"C"``

* ``ITBuffersize=`` *[integer]*
  *Default* ``1024``

Libraries
=========

* ``uffParametersDataBase=`` *[character]*
  *Default* ``"/dataBases/uffParameters.lib"``

* ``atomicElementsDataBase=`` *[character]*
  *Default* ``"/dataBases/atomicElements.lib"``

* ``basisSetDataBase=`` *[character]*
  *Default* ``"/basis/"``

* ``potentialsDataBase=`` *[character]*
  *Default* ``"/potentials/"``

* ``elementalParticlesDataBase=`` *[character]*
  *Default* ``"/dataBases/elementalParticles.lib"``

