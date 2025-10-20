=========
Integrals
=========

openLOWDIN computes analitically one-body and two-body integrals based on atomic orbitals expressed as a sum of contracted GTFs under a cartesian coordinate representation (see :ref:`Basis`)

.. math::
  :nowrap:

   \begin{equation}                                                                                                                     
   \phi_i^{\alpha}(\mathbf{r}_i) = \sum_{\mu}^{N_{bas}^{\alpha}} C_{\mu}^{\alpha} \varphi_{\mu}^{\alpha}(\mathbf{r}_i;\mathbf{R}_{\mu}) 
   \end{equation}                                                                                                                       


In matrix form, the following integrals are implemented in openLOWDIN

One-body integrals
==================

All computed under an Obara-Saika scheme for any angular momentum in the basis set

Overlap

.. math::
  :nowrap:

  \begin{equation}
  S_{\mu \nu}^\alpha =\int d r_i \varphi_\mu^\alpha(i) \varphi_\nu^\alpha(i) 
  \end{equation}

Kinetic

.. math::
  :nowrap:

  \begin{equation}
  T_{\mu \nu}^\alpha =\int d r_i \varphi_\mu^\alpha(i) \nabla_i^2  \varphi_\nu^\alpha(i) 
  \end{equation}

Point charge potential

.. math::
  :nowrap:

  \begin{equation}
  \mathbb{PC}_{\mu \nu}^\alpha = \sum_{I} \int d r_i \varphi_\mu^\alpha(i) \frac{1}{r_i - R_I}  \varphi_\nu^\alpha(i) 
  \end{equation}

Moment integrals

.. math::
  :nowrap:

  \begin{align}
  \mathbb{UA}_{\mu \nu}^\alpha = \int d r_i \varphi_\mu^\alpha(i) r_{i,\mathbb{A}}  \varphi_\nu^\alpha(i) \quad \mathbb{A} = { x,y,z } \\
  \mathbb{UAB}_{\mu \nu}^\alpha = \int d r_i \varphi_\mu^\alpha(i) r_{i,\mathbb{A}} r_{i,\mathbb{B}} \varphi_\nu^\alpha(i) \quad \mathbb{A,B} = { x,y,z }
  \end{align}

Harmonic integrals

.. math::
  :nowrap:

  \begin{align}
  \mathbb{HA}_{\mu \nu}^\alpha = \int d r_i \varphi_\mu^\alpha(i) r^2_{i}  \varphi_\nu^\alpha(i) 
  \end{align}

Three-center integrals

.. math::
  :nowrap:

  \begin{align}
  \mathbb{3C}_{\mu \nu}^\alpha = \sum_{\sigma} \int d r_i \varphi_\mu^\alpha(i)  \varphi_{\sigma}(i)  \varphi_\nu^\alpha(i) 
  \end{align}

Two-body integrals
==================

These integrals are computed with LIBINT library `<https://github.com/evaleev/libint>`_ 

Four-center intraspecies coulomb potential

.. math::
  :nowrap:

  \begin{align}
  \mathbb{4C}_{\mu \nu \sigma \lambda }^{\alpha} &= \langle \mu^\alpha \nu^\alpha | \sigma^\alpha\lambda^\alpha \rangle \\
                                               &= \int \int d r_i d r_j \varphi_\mu^\alpha(i)  \varphi_\nu^\alpha(j) 
   \frac{1}{r_i - r_j} \varphi_\sigma^\alpha(i)  \varphi_\lambda^\alpha(j) 
  \end{align}

Four-center interspecies coulomb potential

.. math::
  :nowrap:

  \begin{align}
  \mathbb{4C}_{\mu \nu \sigma \lambda }^{\alpha\beta} &=  \langle \mu^\alpha \nu^\beta | \sigma^\alpha\lambda^\beta \rangle \\
                                               & = \int \int d r_i d r_j \varphi_\mu^\alpha(i)  \varphi_\nu^\beta(j) 
   \frac{1}{r_i - r_j} \varphi_\sigma^\alpha(i)  \varphi_\lambda^\beta(j) 
  \end{align}

Five-center, intra- and interspecies

.. math::
  :nowrap:

  \begin{align}
  \mathbb{5C}_{\mu \nu \sigma \lambda }^{\alpha,\beta} &= \langle \mu^\alpha \nu^\beta | V_2^{\alpha\beta}(\mathbf{r}^{\alpha}_i,\mathbf{r}^{\beta}_j) | \sigma^\alpha\lambda^\beta \rangle \\
  &= \sum_\tau C_\tau^{\alpha\beta} \int \int d r_i d r_j \varphi_\mu^\alpha(i)  \varphi_\nu^\beta(j) 
  \ \text{exp}[ -a_\tau^{\alpha\beta} ({r}_i - {r}_{j})^2 ]  \varphi_\sigma^\alpha(i)  \varphi_\lambda^\beta(j) 
  \end{align}

Input options
-------------

* ``tv=`` *[float]*
  deprecated *Default* ``1.0E-6`` 

* ``integralThreshold=`` *[float]*
  threshold to store integrals in disk above the given value. *Default* ``1.0E-10`` 

* ``integralStackSize=`` *[integer]*
  write and load integrals temporary files by stacks of this values. *Default* ``30000`` 

* ``integralStorage=`` *[character]*
  select storage scheme for two-particles integrals

  .. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ``"DISK"`` 
      - Storage all non-zero integrals in disk at $SCRATCH folder, after four-index permutational symmetries. *Default*
    * - ``"MEMORY"``
      - Allocate a four dimensional array in RAM memory 
    * - ``"DIRECT"``
      - Compute integrals on-the-fly (only for the SCF step)

* ``integralScheme=`` *[character]*
  select two-particles library. *Default* ``"LIBINT"``

* ``schwarzInequality=`` *[logical]*
  perfoms Schwarz inequality to skip blocks of small integrals. Deprecated, now it's used by default within libint interface. *Default* ``.false.`` 


