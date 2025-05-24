.. _PT:

======================
Propagathor Theory, PT
======================

OpenLOWDIN can calculate ionization potentials for any species employing the propagator formalism, where ionization energy for an specific orbital is calculated
as the Koopmans value plus self-energy corrections.
The current implementation includes second order corrections (APMO/P2), second order plus transition operator corrections (APMO/TOEP2),
third order corrections (APMO/P3) and renormalized third order corrections (APMO/REN-P3) as in the multicomponent extension of the outer valence Green function method (APMO/OVGF)

At second order, there are intraspecies and interspecies contributions to the self energy corrections to the eigenvalue of reference orbital p:

.. math::
   :nowrap:

   \begin{align}
   \omega_{\alpha p}  = &  \epsilon_{\alpha p}+\Sigma_{\alpha pp}(\omega_{\alpha p}) \notag \\
   \Sigma_{\alpha pp}^{(2)}(\omega_{\alpha p}) = & \notag
   \sum_{i}^{oc_\alpha} \sum_{ab}^{vir_\alpha}
   \frac{| \langle p_\alpha i_\alpha||a_\alpha b_\alpha\rangle|^{2} }
   {\omega_{\alpha p}+\epsilon_{\alpha i}-\epsilon_{\alpha a}-\epsilon_{\alpha b}}
   +\sum_{ij}^{oc_\alpha} \sum_{a}^{vir_\alpha}
   \frac{| \langle p_\alpha a_\alpha||i_\alpha j_\alpha\rangle|^{2} }       
   {\omega_{\alpha p}+\epsilon_{\alpha a}-\epsilon_{\alpha i}-\epsilon_{\alpha j}} \\ & 
   +\sum_{a}^{vir_\alpha} \sum_{i}^{oc_\beta} \sum_{b}^{vir_\beta}
   \frac{| \langle p_\alpha i_\beta|a_\alpha b_\beta\rangle|^{2} }
   {\omega_{\alpha p}+\epsilon_{\beta i}-\epsilon_{\alpha a}-\epsilon_{\beta b}}
   +\sum_{i}^{oc_\alpha}\sum_{j}^{oc_\beta} \sum_{a}^{vir_\beta}
   \frac{| \langle p_\alpha a_\beta|i_\alpha j_\beta\rangle|^{2}}
   {\omega_{\alpha p}+\epsilon_{\beta a}-\epsilon_{\alpha i}-\epsilon_{\beta j}}
   \end{align}

More details on the multicomponent propagator methods can be found in (romero.JCP.137.074105.2012,romero.JCP.141.114103.2014)

To perform a propagator calculations using LOWDIN, the order of PT (2 or 3) must be specified in the "TASKS" block using the keyword "propagatorTheoryCorrection".
Currently, the third order corrections is only available from a UHF reference.

A default calculation obtains ionization energies for the HOMO and LUMO orbitals of all the species present in the input.
Using the "IonizeMO" and "ionizeSpecies" in the "CONTROL" block, allows the user to select specific orbitals for the propagator calculation. In that case, set up the flag "ptJustOneOrbital=.T." to save computational time.

Transition operator corrections latter take advantage of fractional occupation to include additional relaxation in calculated ionization energies.
To perform calculations with this method, select the UHF reference, add to the control block the "ptTransitionOperator=.T." and select a fractional occupation using "MOfractionOccupation". The recommended value is 0.5.

For third order calculations, you can select in the "CONTROL" block the type of correction to be used by adding "ptP3Method=" with "P3","EP3","OVGF-A","OVGF-B","OVGF-C" and "REN-P3" as options. By default, the six correction types are computed. 

See :ref:`PT2 example`, :ref:`TOEP2 example` and :ref:`PT3 example` for examples of propagator calculations in openLowdin
