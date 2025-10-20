==========
Potentials
==========

Given all the integrals implemented in openLOWDIN (see :ref:`Integrals`), the code is capable of building the following potentials to the Core and Fock matrices:

Fixed point charges repulsion

.. math::
  :nowrap:
  
  \begin{equation}
  V_{PP} =  \sum_{I,J} \frac{Z_I Z_J}{R_{IJ}} 
  \end{equation}

Quantum/fixed charges interaction

.. math::
  :nowrap:
  
  \begin{equation}
  \hat{V}_{\mathbb{PC}} = \sum_{j}^{n_c} \frac{q_i^{\alpha} Z_J}{r_i - R_{J}}, \quad 
  {\bf V}_{\mathbb{PC}} = q^{\alpha} \sum_{j}^{n_c} Z_J \mathbb{PC}^\alpha   
  \end{equation}

External electric field. It requires adding in the ``CONTROL`` section a non-zero electric field strength :math:`\vec{F}` for each cartesian component XYZ as a real vector  ``ELECTRIC_FIELD =`` *[real real real]* 

.. math::
  :nowrap:
  
  \begin{equation}
  \sum_{\mathbb{A}}^{X,Y,Z} \hat{V}_{\mathbb{UA}} = \sum_{\mathbb{A}}^{X,Y,Z}\sum_{i}^{N_{\alpha}} q_i^{\alpha} F_{\mathbb{A}} \cdot r_{i,\mathbb{A}} , \quad 
  \sum_{\mathbb{A}}^{X,Y,Z} {\bf V}_{\mathbb{UA}} =  \sum_{\mathbb{A}}^{X,Y,Z} q^{\alpha} F_{\mathbb{A}} \mathbb{UA}^\alpha   
  \end{equation}

Harmonic potential, centered at the origin of coordinates. It requires to declare non-zero frequency :math:`\omega` in the ``GEOMETRY`` block with the flag ``omega =`` *[real]*  

.. math::
  :nowrap:
  
  \begin{equation}
  \hat{V}_{\mathbb{HA}} = \sum_{i}^{N_{\alpha}} \frac{1}{2} m^{\alpha} (\omega^{\alpha})^2 r^2_{i} , \quad 
  {\bf V}_{\mathbb{HA}} = \frac{1}{2} m^{\alpha} (\omega^{\alpha})^2 \mathbb{HA}^\alpha   
  \end{equation}

Quantrum Drude oscillator potential. It requires to declare non-zero frequency :math:`\omega` in the ``GEOMETRY`` block with the flag ``omega =`` *[real]* , as well as declaring a fixed point charge as the QDO charged center associated to the quantum species symbol with the flag ``qdoCenterOf=`` *[character]*, adding this flag will replace the quantum/fixed Coulomb potential with this point charge.
For example   ``H dirac 0.00 0.00 0.00 qdoCenterOf=EA-`` (See :ref:`QDO`)

.. math::
  :nowrap:
  
  \begin{equation}
  \hat{V}_{QDO} = \sum_{i}^{N_{\alpha}} \frac{1}{2} m^{\alpha} (\omega^{\alpha})^2 (r_{i} - R_{QDO}^{\alpha})^2 , \quad 
  {\bf V}_{QDO} = \frac{1}{2} m^{\alpha} (\omega^{\alpha})^2 \mathbb{HA}^\alpha 
  \end{equation}

External potential. See :ref:`External potential basis` 


.. math::
  :nowrap:

  \begin{equation}
  \hat{V}_1^{\alpha} = \sum_i^{N_{\alpha}}\sum_{\tau}^{N_{bas}^{\alpha}} C_{\tau}^{\alpha} (x_i-X_{\tau})^{l_{\tau}^{\alpha}}(y_i-Y_{\tau})^{m_{\tau}^{\alpha}}(z_i-Z_{\tau})^{n_{\tau}^{\alpha}}
  			\times \text{exp}[ -a_{\tau}^{\alpha} (\mathbf{r}_i - \mathbf{R}_{\tau})^2 ], 
  {\bf V}_1^{\alpha} = \mathbb{3C}^{\alpha} 
  \end{equation}

Intraspecies repulsion

.. math::
  :nowrap:
  
  \begin{equation}
  \hat{V}_{2}^{\alpha\alpha} = \sum_{i\ne j}^{N_{\alpha}} \frac{q_i^{\alpha} q_j^{\alpha}  }{r_i - r_{j}}, \quad 
  {\bf V}_{2}^{\alpha\alpha} = q^{\alpha} q^{\alpha} G^\alpha   
  \end{equation}

Interspecies repulsion

.. math::
  :nowrap:
  
  \begin{equation}
  \sum_{\beta\ne \alpha}^{N_{sp}} \hat{V}_{2}^{\alpha\beta} = \sum_{\beta\ne \alpha}^{N_{sp}} \sum_{i}^{N_{\alpha}} \sum_{j}^{N_{\beta}} \frac{q_i^{\alpha} q_j^{\alpha}  }{r_i - r_{j}}, \quad 
  \sum_{\beta\ne \alpha}^{N_{sp}} {\bf V}_{2}^{\alpha\beta} = \sum_{\beta\ne \alpha}^{N_{sp}} q^{\alpha} q^{\beta} G^\beta
  \end{equation}


Internal potential. See :ref:`Internal potential basis`. Notice this potential will replace the Coulomb intraspecies or interspecies potential.

.. math::
  :nowrap:

  \begin{equation}
  V_2^{\alpha\beta} = \sum_{i}^{N_{\alpha}} \sum_{j}^{N_{\beta}} \sum_{\tau}^{N_{bas}^{\alpha\beta}} C_{\tau}^{\alpha\beta} \text{exp}[ -a_{\tau}^{\alpha\beta} (\mathbf{r}^{\alpha}_i - \mathbf{r}^{\beta}_{j})^2 ], \quad
  {\bf V}_2^{\alpha\beta} = \mathbb{5C}^{\alpha} 
  \end{equation}

