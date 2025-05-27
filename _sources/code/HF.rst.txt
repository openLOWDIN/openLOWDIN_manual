.. _HF:

================
Hartree-Fock, HF
================

The APMO/HF level wave function for a multispecies molecular
system in the ground state, :math:`\Psi_0`, is constructed as a product
of a single-configurational wave function, :math:`\Phi_{\alpha}`, :

.. math::

   {\Psi}_0= \prod_{\alpha}^{N_{sp}} \Phi_{\alpha}

In the most common case, :math:`\Phi_{\alpha}` is
built as a single slater determinant of single-particle spin molecular orbitals :math:`\chi_i`
as

.. math::

   \begin{aligned}
   \Psi_{\mathrm{SD}}(\overline{\mathbf{x}})=\frac{1}{\sqrt{N_{\alpha} !}}\left|\begin{array}{cccc}
   \chi_1\left(\mathbf{x}_1\right) & \chi_1\left(\mathbf{x}_2\right) & \ldots & \chi_1\left(\mathbf{x}_{N_{\alpha}}\right) \\
   \chi_2\left(\mathbf{x}_1\right) & \chi_2\left(\mathbf{x}_2\right) & \ldots & \chi_2\left(\mathbf{x}_{N_{\alpha}}\right) \\
   \ldots & \ldots & \ldots & \ldots \\
   \chi_{N_{\alpha}}\left(\mathbf{x}_1\right) & \chi_{N_f}\left(\mathbf{x}_2\right) & \ldots & \chi_{N_{\alpha}}\left(\mathbf{x}_{N_{\alpha}}\right)
   \end{array}\right|,
   \label{chap2:eq:SD}\end{aligned}

here :math:`\alpha` symbol is used to represent quantum species,
:math:`\mathbf{x}` corresponds to their spin-coordinates
vector, and :math:`\overline{\mathbf{x}}` is the full set of
4\ :math:`N` coordinates. The spatial part of these spin orbitals,
:math:`\phi`, is written as a linear combination of atomic orbitals
:math:`\varphi` with a basis set of size :math:`B` (notice that the
number of atomic centers can be greater than the number of classical
nuclei :math:`N_c`) as

.. math::

   \begin{aligned}
   \phi_i^{\alpha}(\mathbf{r}_i) = \sum_{\mu}^{N_{bas}^{\alpha}} C_{\mu}^{\alpha} \varphi_{\mu}^{\alpha}(\mathbf{r}_i;\mathbf{R}_{\mu})
   \end{aligned}

Commonly these atomic orbitals are constructed with GTFs that depend on
the spatial coordinate of one single particle :math:`r_i` and are
centered on a fixed position :math:`R` for each atomic center. See :ref:`Basis`

The molecular orbitals are obtained by solving the coupled Fock equations, see :ref:`SCF`, 

.. math::

   \begin{aligned}
   \label{chap2:eq:FockEquation}
   f^\alpha(i)\phi^\alpha_i=\varepsilon^\alpha_i\phi^\alpha_i,
   \end{aligned}

where :math:`\varepsilon_i` are the single particle orbital energies.
The effective one-particle Fock operators, :math:`f^\alpha(i)`, for the
quantum species :math:`e^-` and :math:`e^+` are expanded as

.. math::

   \begin{aligned}
   \label{chap2:eq:FockOperator}
   f^{\alpha}(i)=h^{\alpha}(i) + \sum^{N_{\alpha}}_{j} (q^{\alpha})^2 [J^{\alpha}_j - K^{\alpha}_j]
   + \sum_{\beta\ne\alpha}^{N_{sp}} \sum^{N_{\beta}}_{j} q^{\alpha}q^{\beta} J^{\beta}_j.
   \end{aligned}

In the above equation :math:`h^\alpha(i)` is the single-particle core
Hamiltonian

.. math::

   \begin{aligned}
   \label{chap2:eq:CoreHamiltonian}
   h^\alpha(i)=-\frac{1}{2m_{\alpha}}\nabla_{i}^{2} + \sum_{J}^{N_c}\frac{q^{\alpha} Z^{\alpha}}{R_{iJ}},
   \end{aligned}

and :math:`J^\alpha` and :math:`K^\alpha` are the Coulomb and exchange
operators defined as

.. math::

   \begin{aligned}
   \label{chap2:eq:CoulombOperator}
   J^\alpha_j(1)\phi^\alpha_i(1)= q^\alpha q^\alpha\left[\int d{\bf r}_2\phi^{\alpha*}_j(2) \frac{1}{r_{12}} \phi^{\alpha}_j(2)\right]\phi^\alpha_i(1) ,\end{aligned}

.. math::

   \begin{aligned}
   \label{chap2:eq:ExchangeOperator}
   K^{\alpha} _j(1)\phi^{\alpha}_i(1)=\left[\int d{\bf r}_2\phi^{{\alpha}*}_j(2)\frac{1}{r_{12}} \phi^{\alpha}_i(2)\right]\phi^{\alpha}_j(1) .\end{aligned}

In addition, :math:`J^\beta` is the operator which accounts for the
Coulomb potential between particles of different quantum species, thus
is the term which couples the electronic and positronic Fock equations,
and is defined as

.. math::

   \begin{aligned}
   \label{chap2:eq:CoulombCouplingOperator}
   J^\beta_j(1)\phi^\alpha_i(1)= q^\beta q^\alpha\left[\int d{\bf r}_2\phi^{\beta*}_j(2) \frac{1}{r_{12}} \phi^{\beta}_j(2)\right]\phi^\alpha_i(1) .
   \end{aligned}

In openLOWDIN, these expressions are implemented in a matrix form :cite:p:`szabo.1996.modern`

.. math::

   \begin{aligned}
   \begin{aligned}
   S_{\mu \nu}^\alpha & =\int d r_1 \varphi_\mu^\alpha(1) \varphi_\nu^\alpha(1) \\
   F_{\mu \nu}^\alpha & =H_{\mu \nu}^\alpha+G_{\mu \nu}^\alpha + \sum_{\beta\ne\alpha}^{N_{sp}} G_{\mu \nu}^\beta \\
   H_{\mu \nu}^\alpha & =\int d r_1 \varphi_\mu^\alpha(1) h^\alpha(1) \varphi_\nu^\alpha(1) \\
   G_{\mu \nu}^\alpha & =\sum_{\lambda \sigma} P_{\lambda \sigma}^\alpha\left[\left(\mu^\alpha \nu^\alpha \mid \sigma^\alpha \lambda^\alpha\right)- (1/2) \left(\mu^\alpha \lambda^\alpha \mid \sigma^\alpha \nu^\alpha\right)\right] \\
   G_{\mu \nu}^\beta & =\sum_{\lambda \sigma} P_{\lambda \sigma}^\beta\left(\mu^\alpha \nu^\alpha \mid \sigma^\beta \lambda^\beta\right),
   \end{aligned}\end{aligned}

where :math:`S_{\mu \nu}`, :math:`F_{\mu \nu}`, :math:`H_{\mu \nu}`, and
:math:`G_{\mu \nu}` correspond to the overlap, one-core Hamiltonian, and
two-particles matrices, which all run over the total number of atomic orbitals
:math:`\mu,\nu`. Here, the chemistry notation of two-particles integrals
:math:`( \varphi_{\mu} \varphi_{\nu} | \varphi_{\sigma} \varphi_{\lambda} )` has
been simplified to :math:`( \mu \nu | \sigma \lambda)`. See :ref:`Integrals`.

In addition, the density matrix elements are defined from the coefficient matrix
:math:`\mathbf{C}` of the molecular orbitals expansion and the fermionic orbital
occupation :math:`\eta`

.. math:: P_{\mu \nu}^{\alpha} = \eta^{\alpha}\sum_{\lambda}^{occ^\alpha} C^{\alpha}_{\mu \lambda} C^{* \alpha}_{\lambda \nu}.

These coefficient matrices are found by diagonalizing the Roothan-Hall
equations

.. math::

   \mathbf{F C} = \epsilon \mathbf{S C}.
   \label{chap2:eq:roothan}

Finally, the total Hartree-Fock energy is computed from

.. math::

   \begin{aligned}
   E_0=\frac{1}{2} \sum_{\alpha}^{N_{sp}} \sum_{\mu\nu}^{occ^{\alpha}} P_{\mu \nu}^\alpha\left(H_{\mu \nu}^\alpha+F_{\mu \nu}^\alpha\right).
   \label{chap2:eq:HF}\end{aligned}

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

