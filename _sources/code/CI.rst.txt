.. _CI:

=============================
Configuration Interaction, CI
=============================

CI Wavefunction 
===============

The APMO/CI wave function is written as a linear combination of CI configurations

.. math::
   :nowrap:

    \begin{equation}
      | \Psi_{\text{CI}} \rangle = \sum_{I}^{N_{\text{conf}}} c_I|\Psi_I\rangle
   \end{equation}

as products of Slater determinants between all quantum species

.. math::
  :nowrap:

     \begin{equation}
      | \Psi_I \rangle =
      \prod_{\alpha}^{N_{sp}} | D_I \rangle_{\alpha} = | D_I \rangle_{\alpha}  | D_I \rangle_{\beta}
      | D_I \rangle_{\gamma} \dots
   \end{equation}

where each is built as excitations within each type of quantum species, written in second quantization as:

.. math::
  :nowrap:

   \begin{equation}
    | D_I \rangle_{\alpha} = a_i^{\dagger}a_j^{\dagger}\dots a_{N_{\alpha}}^{\dagger} | \rangle_{\alpha}
    \end{equation}

For example,

.. figure:: CI/conf.svg
   :alt: Schematic of a configuration
   :width: 400px
   :align: center

   Schematic of multicomponent CI configuration

Normally in CI, those configurations are group together according to the excitation level

.. math::
  :nowrap:

   \begin{equation}
      | \Psi_{\text{CI}} \rangle = c_0|\Psi_0\rangle
      + \sum_{\alpha}\sum_{ia \in \alpha} c_i^a|\Psi_i^a \rangle
      +\sum_{\alpha,\beta}\sum_{\substack{ia\in\alpha\\jb\in\beta}} c_{ij}^{ab}|\Psi_{ij}^{ab} \rangle
      +\sum_{\alpha,\beta}\sum_{\substack{ia\in\alpha\\jb\in\alpha\\kc\in\beta}} c_{ijk}^{abc}|\Psi_{ijk}^{abc} \rangle
      + \cdots
   \end{equation}

leading to all singles excitations for all species, doubles within the same species (intraspecies), doubles as products of two single excitations from two different species (interspecies) for all possible pairs, as well as triples, quadrupoles, ... and so on.

.. figure:: CI/CI_confs.svg
   :alt: Schematic of a configuration
   :width: 800px
   :align: center

   Schematic of multicomponent CI wave function 

Given that wavefunction, the CI Hamiltonian matrix are computed following Slater’s rules taking into accound that the multispecies potential operator are still a two-body operator at most.

Identical determinants:

.. math::
  :nowrap:
 
  \begin{equation}
  \langle \Phi_I | \hat{H} | \Phi_I \rangle =
  \sum_{\alpha}^{N_s} \sum_i^{N^{\alpha}} [i|\hat{h}|i] +
  \sum_{\alpha}^{N_s} \sum_i^{N^{\alpha}}\sum_{j>i}^{N^{\alpha}} ([ii|jj]-[ij|ji]) +
  \sum_{\alpha}^{N_s}\sum_{\beta > \alpha}^{N_s} \sum_{\substack{i \in \alpha \\ j \in \beta}}^{N^{\alpha}N^{\beta}} [ii|jj] 
  \end{equation}

One spin-orbital different

.. math::
  :nowrap:

  \begin{align}
  & | \Phi_I \rangle = | \cdots i_{\alpha} \cdots \rangle \prod_{\beta \ne \alpha}^{N_s} | \beta(I)\rangle \quad \quad
   | \Phi_J \rangle = | \cdots j_{\alpha} \cdots \rangle
  \prod_{\beta \ne \alpha}^{N_s} | \beta(I)\rangle \\
  & \langle \Phi_I | \hat{H} | \Phi_J \rangle = [i|\hat{h}|i] +  \sum_k^{N^{\alpha}} ([ij|kk]-[ik|kj]) +
  \sum_{\beta \ne \alpha}^{N_s} \sum_{k \in\beta}^{N^{\beta}}[ij|kk], \ \ i,j \in \alpha
  \end{align}

Two spin-orbital different, same species

.. math::
  :nowrap:

  \begin{align}
  & | \Phi_I \rangle = | \cdots i_{\alpha}j_{\alpha}  \cdots \rangle \prod_{\beta \ne \alpha}^{N_s} | \beta(I)\rangle \quad \quad | \Phi_J \rangle = | \cdots k_{\alpha}l_{\alpha}  \cdots \rangle
  \prod_{\beta \ne \alpha}^{N_s} | \beta(I)\rangle\\
  & \langle \Phi_I | \hat{H} | \Phi_J \rangle =
  [ik|jl]-[il|jk], \ \ i,j,k,l \in \alpha
  \end{align}

One spin-orbital different for two different quantum species

.. math::
  :nowrap:

  \begin{align}
  & | \Phi_I \rangle = | \cdots i_{\alpha} \cdots \rangle 
  | \cdots k_{\beta} \cdots \rangle 
  \prod_{\substack{\gamma \ne \alpha\\ \gamma\ne\beta}}^{N_s} | \gamma(I)\rangle \\ &
   | \Phi_J \rangle =  | \cdots j_{\alpha} \cdots \rangle 
  | \cdots l_{\beta} \cdots \rangle 
  \prod_{\substack{\gamma \ne \alpha\\ \gamma\ne\beta}}^{N_s} | \gamma(I)\rangle \\
  & \langle \Phi_I |  \hat{H} |  \Phi_J \rangle =  [ij| kl], \ \ i,j \in \alpha ,k,l \in \beta
  \end{align}

More than two spin orbital different within same species or more than two different species, differing in one spin orbital.

.. math::
  :nowrap:

  \begin{align}
  & \langle \Phi_I | \hat{H} | \Phi_J \rangle = 0
  \end{align}

The combinational CI coefficients :math:`c` are obtained variationally by solving the CI eigenvalue problem :math:`\textbf{Hc} = E\textbf{c}`. 
Due to the size of the Hamiltonian Matrix :math:`\textbf{H}`, it is necessary to use iterative techniques for diagonalization of real symmetric matrices avoiding the memory storage of the full matrix. Davidson's method is the most used technique to find the lowest eigenvalues and eigenvectors. Here, the storage requirements of :math:`\textbf{H}` can be greatly reduced by direct calculation of a matrix-vector product of the form :math:`\textbf{Hc} = \sigma`.

Selected CI, SCI
================

In openLOWDIN, the CI techniques aimed to select the most relevant configurations within the whole CI space are encompassed as the SCI family. These are usually categorized as stochastic or deterministic :cite:p:`eriksen_JPCL_11_8922_2020`. Currently the code has implemented an extended multicomponent version of Adaptive Sampling CI, ASCI :cite:p:`tubman_JCP_145_044112_2016`.

.. figure:: CI/SCI_scheme.svg
   :alt: Schematic of SCI
   :width: 500px
   :align: center

   Schematic of SCI algorithm




Natural orbitals
================

CI Input options
================


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


