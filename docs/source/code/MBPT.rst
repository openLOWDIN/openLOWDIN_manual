.. _MBPT:

===================================
Many-Body Perturbation Theory, MBPT
===================================

OpenLowdin can perform second order many-body perturbation theory (MP2) corrections to the energy on systems including any kind of quantum particle. These corrections are probably the simplest way to recover the effects of correlation between particles of different species. 

.. math::
   \begin{align}
       E_{\text{MP2}}=& \text{E}_{\text{HF}} + \sum_{\alpha}^{N_{typ}} \text{E}_{\alpha \alpha}^{(2)} + \sum_{\alpha\beta}^{N_{typ}} \text{E}_{\alpha \beta}^{(2)}, \\
       E_{\alpha \alpha}^{(2)}=& \frac{q_{\alpha}^2}{4}
       \sum_{ij}^{oc_\alpha}
       \sum_{ab}^{vir_\alpha}
       \frac{\mid {\langle i_{\alpha} j_{\alpha} \mid \mid a_{\alpha} b_{\alpha} \rangle }  \mid ^2}
       {\varepsilon_{\alpha i} + \varepsilon_{\alpha j} - \varepsilon_{\alpha a} - \varepsilon_{\alpha b}}, \notag \\
       E_{\alpha \beta}^{(2)}=& q_{\alpha}q_{\beta}
       \sum_{i}^{oc_\alpha}
       \sum_{j}^{oc_\beta}
       \sum_{a}^{vir_\alpha}
       \sum_{b}^{vir_\beta}
       \frac{\mid {\langle i_{\alpha} j_{\beta}  \mid a_{\alpha} b_{\beta} \rangle } \mid ^2}
       {\varepsilon_{\alpha i} + \varepsilon_{\beta j} - \varepsilon_{\alpha a}- \varepsilon_{\beta b}}. \notag
   \end{align}


For more information on APMO-MP2 calculations see S. A. Gonz\'alez, A. Reyes, "Nuclear Quantum Effects on the He2H+ Complex With the Nuclear Molecular Orbital Approach", Int. J. Quant. Chem. 110 689 (2010) https://doi.org/10.1002/qua.22118

In addition, OpenLowdin can compute second order Epsein-Nesbet (EN2) corrections, which correspond to renormalized MP2 equations.

See :ref:`MP2 example` for an example of a MP2 calculation in openLowdin
