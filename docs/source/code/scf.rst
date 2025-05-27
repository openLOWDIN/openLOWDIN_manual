===
SCF
===

* ``nonElectronicEnergyTolerance=`` *[float]*
  *Default* ``1.0E-8`` 

* ``electronicEnergyTolerance=`` *[float]*
  *Default* ``1.0E-8`` 

* ``nonelectronicDensityMatrixTolerance=`` *[float]*
  *Default* ``1.0E-6`` 

* ``electronicDensityMatrixTolerance=`` *[float]*
  *Default* ``1.0E-6`` 

* ``totalEnergyTolerance=`` *[float]*
  *Default* ``1.0E-8`` 

* ``totalDensityMatrixTolerance=`` *[float]*
  *Default* ``1.0E-6`` 

* ``densityFactorThreshold=`` *[float]*
  *Default* ``1.0E-8`` 

* ``diisSwitchThreshold=`` *[float]*
  *Default* ``0.5`` 

* ``diisSwitchThreshold_bkp=`` *[float]*
  *Default* ``0.5`` 

* ``electronicLevelShifting=`` *[integer]*
  *Default* ``0.0`` 

* ``nonelectronicLevelShifting=`` *[integer]*
  *Default* ``0.0`` 

* ``exchangeOrbitalThreshold=`` *[float]*
  *Default* ``0.8`` 

* ``waveFunctionScale=`` *[integer]*
  *Default* ``1000.0`` 

* ``scfNonelectronicMaxIterations=`` *[integer]*
  *Default* ``50`` 

* ``scfElectronicMaxIterations=`` *[integer]*
  *Default* ``50`` 

* ``scfGlobalMaxIterations=`` *[integer]*
  *Default* ``200`` 

* ``listSize=`` *[integer]*
  *Default* ``-20`` 

* ``convergenceMethod=`` *[character]*
  *Default* ``1!!(0)NONE,(1)DAMPING,(2)DIIS,(3)LEVELSHIFTING(4)DAMPING/DIIS`` 

* ``diisDimensionality=`` *[integer]*
  *Default* ``10`` 

* ``iterationScheme=`` *[character]*
  *Default* ``3!!(0)NONELECRONICFULLY/e-(1)ELECTRONICFULLY(2)CONVERGEDINDIVIDIALLY(3)SCHEMESIMULTANEOUS`` 

* ``scfElectronicTypeGuess=`` *[character]*
  *Default* ``"HCORE"`` 

* ``scfNonelectronicTypeGuess=`` *[character]*
  *Default* ``"HCORE"`` 

* ``scfConvergenceCriterium=`` *[character]*
  *Default* ``"ENERGY"!ENERGY,DENSITY,BOTH`` 

* ``diisErrorInDamping=`` *[logical]*
  *Default* ``.false.`` 

* ``activateLevelShifting=`` *[logical]*
  *Default* ``.false.`` 

* ``exchangeOrbitalsInSCF=`` *[logical]*
  *Default* ``.false.`` 

* ``forceClosedShell=`` *[logical]*
  *Default* ``.false.`` 

* ``debugScfs=`` *[logical]*
  *Default* ``.false.`` 

* ``scfGhostSpecies=`` *[character]*
  *Default* ``"NONE"`` 



