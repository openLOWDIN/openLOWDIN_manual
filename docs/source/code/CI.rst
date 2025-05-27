.. _CI:

=============================
Configuration Interaction, CI
=============================

The APMO/CI wave function is written as a linear combination of CI configurations between all quantum species

.. math::
   :nowrap:

   \begin{equation}
      | \Phi_0 \rangle = c_0|\Psi_0\rangle
      + \sum_{\alpha}\sum_{ia \in \alpha} c_i^a|\Psi_i^a \rangle
      +\sum_{\alpha,\beta}\sum_{\substack{ia\in\alpha\\jb\in\beta}} c_{ij}^{ab}|\Psi_{ij}^{ab} \rangle
      +\sum_{\alpha,\beta}\sum_{\substack{ia\in\alpha\\jb\in\alpha\\kc\in\beta}} c_{ijk}^{abc}|\Psi_{ijk}^{abc} \rangle
      + \cdots
   \end{equation}

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


