    !!***************************************************************************
    !! Dummy variables, just for debugging. 
    !!
* ``dummyReal(:)=`` *[float]*
  *Default* ``0.0_8`` 

* ``dummyInteger(:)=`` *[integer]*
  *Default* ``0`` 

* ``dummyLogical(:)=`` *[logical]*
  *Default* ``.false.`` 

* ``dummyCharacter(:)=`` *[character]*
  *Default* ``""`` 


    !!***************************************************************************
    !! Parameter to control Integrals library
    !!  
* ``tv=`` *[float]*
  *Default* ``1.0E-6`` 

* ``integralThreshold=`` *[float]*
  *Default* ``1.0E-10`` 

* ``integralStackSize=`` *[integer]*
  *Default* ``30000`` 

* ``integralStorage=`` *[character]*
  *Default* ``"DISK"!!"MEMORY"or"DISK"or"DIRECT"`` 

* ``integralScheme=`` *[character]*
  *Default* ``"LIBINT"!!LIBINTorRYS`` 

* ``schwarzInequality=`` *[logical]*
  *Default* ``.false.`` 

* ``harmonicConstant=`` *[float]*
  *Default* ``0.0_8`` 


    !!***************************************************************************
    !! Parameter to control SCF program
    !!
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


    !!*****************************************************
    !! Hartree-Fock Options
    !!
* ``frozen=`` *[character]*
  *Default* ``"NONE"`` 

* ``freezeNonElectronicOrbitals=`` *[logical]*
  *Default* ``.false.`` 

* ``freezeElectronicOrbitals=`` *[logical]*
  *Default* ``.false.`` 

* ``hartreeProductGuess=`` *[logical]*
  *Default* ``.false.`` 

* ``readCoefficients=`` *[logical]*
  *Default* ``.true.`` 

* ``readFchk=`` *[logical]*
  *Default* ``.false.`` 

* ``writeCoefficientsInBinary=`` *[logical]*
  *Default* ``.true.`` 

* ``readEigenvalues=`` *[logical]*
  *Default* ``.false.`` 

* ``readEigenvaluesInBinary=`` *[logical]*
  *Default* ``.true.`` 

* ``writeEigenvaluesInBinary=`` *[logical]*
  *Default* ``.true.`` 

* ``noSCF=`` *[logical]*
  *Default* ``.false.`` 

* ``finiteMassCorrection=`` *[logical]*
  *Default* ``.false.`` 

* ``removeTranslationalContamination=`` *[logical]*
  *Default* ``.false.`` 

* ``buildTwoParticlesMatrixForOneParticle=`` *[logical]*
  *Default* ``.false.`` 

* ``buildMixedDensityMatrix=`` *[logical]*
  *Default* ``.false.`` 

* ``onlyElectronicEffect=`` *[logical]*
  *Default* ``.false.`` 

* ``electronicWaveFunctionAnalysis=`` *[logical]*
  *Default* ``.false.`` 

* ``isOpenShell=`` *[logical]*
  *Default* ``.false.`` 

* ``getGradients=`` *[logical]*
  *Default* ``.false.`` 

* ``HFprintEigenvalues=`` *[logical]*
  *Default* ``.true.`` 

* ``HFprintEigenvectors=`` *[character]*
  *Default* ``"OCCUPIED"`` 

* ``overlapEigenThreshold=`` *[float]*
  *Default* ``1.0E-8_8`` 

* ``electricField(:)=`` *[float]*
  *Default* ``0.0_8`` 

* ``multipoleOrder=`` *[integer]*
  *Default* ``0`` 


    !!***************************************************************************
    !! Parameter to control geometry optimization
    !!
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


    !!***************************************************************************
    !! Parameter of atomic conectivity
    !!
* ``bondDistanceFactor=`` *[float]*
  *Default* ``1.3_8`` 

* ``bondAngleThreshold=`` *[float]*
  *Default* ``170.0_8`` 

* ``dihedralAngleThreshold=`` *[float]*
  *Default* ``170.0_8`` 


    !!***************************************************************************
    !! Parameter to control MBPn theory
    !!
* ``mpCorrection=`` *[integer]*
  *Default* ``1`` 

* ``mpFrozenCoreBoundary=`` *[integer]*
  *Default* ``0`` 

* ``mpOnlyElectronicCorrection=`` *[logical]*
  *Default* ``.false.`` 

* ``epsteinNesbetCorrection=`` *[integer]*
  *Default* ``1`` 


    !!***************************************************************************
    !! Parameter to control cosmo theory
    !!
* ``cosmo=`` *[logical]*
  *Default* ``.false.`` 

* ``cosmo_solvent_dielectric=`` *[character]*
  *Default* ``78.3553d+00`` 

* ``cosmo_scaling=`` *[character]*
  *Default* ``0.0d+00`` 


    !!***************************************************************************
    !! Parameter to control the propagator theory module
    !!
* ``ptOnlyOneSpecieCorrection=`` *[logical]*
  *Default* ``.false.`` 

* ``selfEnergyScan=`` *[logical]*
  *Default* ``.false.`` 

* ``ptTransitionOperator=`` *[logical]*
  *Default* ``.false.`` 

* ``ptJustOneOrbital=`` *[logical]*
  *Default* ``.false.`` 

* ``selfEnergySpacing=`` *[float]*
  *Default* ``0.5_8`` 

* ``selfEnergyRange=`` *[float]*
  *Default* ``5.0_8`` 

* ``ptOrder=`` *[integer]*
  *Default* ``1`` 

* ``ptMaxIterations=`` *[integer]*
  *Default* ``50`` 

* ``ptIterationMethod2Limit=`` *[integer]*
  *Default* ``1`` 

* ``ptIterationScheme=`` *[integer]*
  *Default* ``1`` 

* ``ptMaxNumberOfPolesSearched=`` *[integer]*
  *Default* ``10`` 


* ``ptFactorSS=`` *[integer]*
  *Default* ``0`` 

* ``ptFactorOS=`` *[integer]*
  *Default* ``0`` 

* ``ptP3Method=`` *[character]*
  *Default* ``"NONE"`` 

* ``ptP3Method(1)=`` *[character]*
  *Default* ``"ALL"`` 


    !!***************************************************************************
    !! Control print level and units
    !!
* ``formatNumberOfColumns=`` *[integer]*
  *Default* ``5`` 

* ``unitForOutputFile=`` *[integer]*
  *Default* ``6`` 

* ``unitForMolecularOrbitalsFile=`` *[integer]*
  *Default* ``8`` 

* ``unitForMP2IntegralsFile=`` *[integer]*
  *Default* ``7`` 

* ``printLevel=`` *[character]*
  *Default* ``1!!(0)nooutput(1)normaloutput,(5)method(6)metodandWF(7)method,WFandGLOBAL(8)method,WF,GLOBAL,SCF`` 

* ``units=`` *[character]*
  *Default* ``"ANGS"`` 

* ``doubleZeroThreshold=`` *[float]*
  *Default* ``1.0E-12`` 


    !!***************************************************************************
    !! CISD - FCI
    !!
* ``configurationInteractionLevel=`` *[character]*
  *Default* ``"NONE"`` 

* ``numberOfCIStates=`` *[integer]*
  *Default* ``1`` 

* ``CIdiagonalizationMethod=`` *[character]*
  *Default* ``"DSYEVR"`` 

* ``CIdiagonalDressedShift=`` *[character]*
  *Default* ``"NONE"`` 

* ``CIactiveSpace=`` *[character]*
  *Default* ``0!!Full`` 

* ``CIstatesToPrint=`` *[integer]*
  *Default* ``1`` 

* ``CImaxNCV=`` *[integer]*
  *Default* ``30`` 

* ``CIsizeOfGuessMatrix=`` *[integer]*
  *Default* ``300`` 

* ``CIstackSize=`` *[integer]*
  *Default* ``5000`` 

* ``CIConvergence=`` *[float]*
  *Default* ``1E-4`` 

* ``CImatvecTolerance=`` *[float]*
  *Default* ``1E-10`` 

* ``CISaveEigenVector=`` *[logical]*
  *Default* ``.false.`` 

* ``CILoadEigenVector=`` *[logical]*
  *Default* ``.false.`` 

* ``CIJacobi=`` *[logical]*
  *Default* ``.false.`` 

* ``CIBuildFullMatrix=`` *[logical]*
  *Default* ``.false.`` 

* ``CIMadSpace=`` *[integer]*
  *Default* ``5`` 

* ``CINaturalOrbitals=`` *[logical]*
  *Default* ``.false.`` 

* ``CIPrintEigenVectorsFormat=`` *[character]*
  *Default* ``"OCCUPIED"`` 

* ``CIPrintThreshold=`` *[float]*
  *Default* ``1E-1`` 


    !!***************************************************************************
    !! Non-orthogonal CI
    !!
* ``nonOrthogonalConfigurationInteraction=`` *[logical]*
  *Default* ``.false.`` 

* ``translationScanGrid(:)=`` *[integer]*
  *Default* ``0`` 

* ``rotationalScanGrid=`` *[integer]*
  *Default* ``0`` 

* ``rotationAroundZMaxAngle=`` *[integer]*
  *Default* ``360`` 

* ``rotationAroundZStep=`` *[integer]*
  *Default* ``0`` 

* ``nestedRotationalGrids=`` *[integer]*
  *Default* ``1`` 

* ``translationStep=`` *[integer]*
  *Default* ``0.0`` 

* ``nestedGridsDisplacement=`` *[integer]*
  *Default* ``0.0`` 

* ``configurationEnergyThreshold=`` *[integer]*
  *Default* ``1.0`` 

* ``configurationOverlapThreshold=`` *[float]*
  *Default* ``1.0E-8`` 

* ``configurationMaxDisplacement(:)=`` *[integer]*
  *Default* ``0.0`` 

* ``configurationMinDisplacement(:)=`` *[integer]*
  *Default* ``0.0`` 

* ``configurationMaxNPDistance=`` *[integer]*
  *Default* ``1.0E8`` 

* ``configurationMinPPDistance=`` *[integer]*
  *Default* ``0.0`` 

* ``configurationMaxPPDistance=`` *[integer]*
  *Default* ``1.0E8`` 

* ``configurationEquivalenceDistance=`` *[float]*
  *Default* ``1.0E-8`` 

* ``empiricalOverlapParameterA=`` *[float]*
  *Default* ``0.0604`` 

* ``empiricalOverlapParameterB=`` *[float]*
  *Default* ``0.492`` 

* ``empiricalOverlapParameterE0=`` *[integer]*
  *Default* ``0.0`` 

* ``empiricalOverlapParameterSc=`` *[integer]*
  *Default* ``0.0`` 

* ``configurationUseSymmetry=`` *[logical]*
  *Default* ``.false.`` 

* ``readNOCIgeometries=`` *[logical]*
  *Default* ``.false.`` 

* ``empiricalOverlapCorrection=`` *[logical]*
  *Default* ``.false.`` 

* ``onlyFirstNOCIelements=`` *[logical]*
  *Default* ``.false.`` 

* ``computeROCIformula=`` *[logical]*
  *Default* ``.false.`` 

    !!***************************************************************************
    !! CCSD
    !!
* ``coupledClusterLevel=`` *[character]*
  *Default* ``"NONE"`` 


    !!*****************************************************
    !! Parameter to general control
    !!
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


    !!*****************************************************
    !! Density Functional Theory Options
    !!
* ``gridStorage=`` *[character]*
  *Default* ``"DISK"`` 

* ``electronCorrelationFunctional=`` *[character]*
  *Default* ``"NONE"`` 

* ``electronExchangeFunctional=`` *[character]*
  *Default* ``"NONE"`` 

* ``electronExchangeCorrelationFunctional=`` *[character]*
  *Default* ``"NONE"`` 

* ``nuclearElectronCorrelationFunctional=`` *[character]*
  *Default* ``"NONE"`` 

* ``positronElectronCorrelationFunctional=`` *[character]*
  *Default* ``"NONE"`` 

* ``betaFunction=`` *[character]*
  *Default* ``"NONE"`` 

* ``gridRadialPoints=`` *[integer]*
  *Default* ``35`` 

* ``gridAngularPoints=`` *[integer]*
  *Default* ``110`` 

* ``gridNumberOfShells=`` *[integer]*
  *Default* ``5`` 

* ``finalGridRadialPoints=`` *[integer]*
  *Default* ``50`` 

* ``finalGridAngularPoints=`` *[integer]*
  *Default* ``302`` 

* ``finalGridNumberOfShells=`` *[integer]*
  *Default* ``5`` 

* ``polarizationOrder=`` *[integer]*
  *Default* ``1`` 

* ``numberOfBlocksInAuxiliaryFunctions=`` *[integer]*
  *Default* ``3`` 

* ``fukuiFunctions=`` *[logical]*
  *Default* ``.false.`` 

* ``auxiliaryDensity=`` *[logical]*
  *Default* ``.false.`` 

* ``storeThreeCenterElectronIntegrals=`` *[logical]*
  *Default* ``.true.`` 

* ``callLibxc=`` *[logical]*
  *Default* ``.true.`` 

* ``nuclearElectronDensityThreshold=`` *[float]*
  *Default* ``1E-10`` 

* ``electronDensityThreshold=`` *[float]*
  *Default* ``1E-10`` 

* ``gridWeightThreshold=`` *[float]*
  *Default* ``1E-10`` 

* ``betaParameterA=`` *[integer]*
  *Default* ``0.0`` 

* ``betaParameterB=`` *[integer]*
  *Default* ``0.0`` 

* ``betaParameterC=`` *[integer]*
  *Default* ``0.0`` 


    !!*****************************************************
    !! Subsystem embedding Options
    !!
* ``subsystemEmbedding=`` *[logical]*
  *Default* ``.false.`` 

* ``localizeOrbitals=`` *[logical]*
  *Default* ``.false.`` 

* ``subsystemLevelShifting=`` *[integer]*
  *Default* ``1.0E6`` 

* ``subsystemOrbitalThreshold=`` *[float]*
  *Default* ``0.1`` 

* ``subsystemBasisThreshold=`` *[float]*
  *Default* ``0.0001`` 

* ``erkaleLocalizationMethod=`` *[character]*
  *Default* ``"MU"`` 


    !!*****************************************************
    !! External Potential Options
    !!
* ``numericalIntegrationForExternalPotential=`` *[logical]*
  *Default* ``.false.`` 

* ``numericalIntegrationForOverlap=`` *[logical]*
  *Default* ``.false.`` 

* ``maxIntervalInNumericalIntegration=`` *[float]*
  *Default* ``10.0_8`` 

* ``relativeErrorInNumericalIntegration=`` *[float]*
  *Default* ``1E-10`` 

* ``initialNumberOfEvaluations=`` *[integer]*
  *Default* ``5000`` 

* ``increaseNumberOfEvaluations=`` *[integer]*
  *Default* ``5000`` 

* ``minimumNumberOfEvaluations=`` *[integer]*
  *Default* ``10000`` 

* ``maximumNumberOfEvaluations=`` *[integer]*
  *Default* ``20000`` 

* ``stepInNumericalIntegration=`` *[float]*
  *Default* ``0.1`` 

* ``coefficientForGaussianExternalPotential=`` *[float]*
  *Default* ``0.0_8`` 

* ``exponentForGaussianExternalPotential=`` *[float]*
  *Default* ``0.0_8`` 

* ``originOfGaussianExternalPotential=`` *[float]*
  *Default* ``0.0_8`` 

* ``numericalIntegrationMethod=`` *[character]*
  *Default* ``"NONE"`` 


    !!*****************************************************
    !! Graphs Options
    !!
* ``numberOfPointsPerDimension=`` *[integer]*
  *Default* ``50`` 

* ``moldenFileFormat=`` *[character]*
  *Default* ``"MIXED"`` 


    !!*****************************************************
    !! Cubes Options
    !!
* ``cubePointsDensity=`` *[integer]*
  *Default* ``125`` 

* ``volumeDensityThreshold=`` *[float]*
  *Default* ``1E-3`` 


    !!***************************************************** 
    !! Molecular Mechanics Options                                                        
* ``forceField=`` *[character]*
  *Default* ``"UFF"`` 

* ``electrostaticMM=`` *[logical]*
  *Default* ``.false.`` 

* ``chargesMM=`` *[logical]*
  *Default* ``.false.`` 

* ``printMM=`` *[logical]*
  *Default* ``.false.`` 


    !!*****************************************************                                                       
    !! Output Options          
* ``moldenFile=`` *[logical]*
  *Default* ``.false.`` 

* ``amberFile=`` *[logical]*
  *Default* ``.false.`` 


    !!*****************************************************
    !! Properties Options
* ``calculateInterparticleDistances=`` *[logical]*
  *Default* ``.false.`` 

* ``calculateDensityVolume=`` *[logical]*
  *Default* ``.false.`` 


    !!*****************************************************
    !! Miscelaneous Options
    !!
* ``MOFractionOccupation=`` *[float]*
  *Default* ``1.0_8`` 

* ``ionizeMO=`` *[integer]*
  *Default* ``0`` 

* ``ionizeSpecies=`` *[character]*
  *Default* ``"NONE"`` 

* ``exciteSpecies=`` *[character]*
  *Default* ``"NONE"`` 


    !!*****************************************************
    !! Integrals transformation options
    !!
* ``integralsTransformationMethod=`` *[character]*
  *Default* ``"C"`` 

* ``ITBuffersize=`` *[integer]*
  *Default* ``1024`` 


    !!***************************************************************************
    !! Variables de ambiente al sistema de archivos del programa
    !!
* ``homeDirectory=`` *[character]*
  *Default* ``CONTROL_getHomeDirectory()`` 

* ``dataDirectory=`` *[character]*
  *Default* ``CONTROL_getDataDirectory()`` 

* ``externalCommand=`` *[character]*
  *Default* ``CONTROL_getExternalCommand()`` 

* ``externalSoftwareName=`` *[character]*
  *Default* ``CONTROL_getExternalSoftwareName()`` 

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

* ``inputFile=`` *[character]*
  *Default* ``CONTROL_instance%INPUT_FILE`` 

