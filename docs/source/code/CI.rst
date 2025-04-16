.. _CI:

=============================
Configuration Interaction, CI
=============================

The APMO/CI wave function is written as a linear combination of CI configurations between all quantum species

.. math::
   :nowrap:

   \begin{equation}
      | \Phi_0 \rangle = c_0 |\Psi_0\rangle
      + \sum_{\alpha}\sum_{ia \in \alpha} c_i^a |\Psi_i^a \rangle
      +\sum_{\alpha,\beta}\sum_{\substack{ia\in\alpha\\jb\in\beta}} c_{ij}^{ab} |\Psi_{ij}^{ab} \rangle
      +\sum_{\alpha,\beta}\sum_{\substack{ia\in\alpha\\jb\in\alpha\\kc\in\beta}} c_{ijk}^{abc} |\Psi_{ijk}^{abc} \rangle
      + \cdots
   \end{equation}

