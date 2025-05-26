.. Getting started:

===============
Getting started
===============

Let's get ready to run openLOWDIN. Here you can find the basic information about the input and how to run the code.
A more exhaustive description of all code keywords and files can be found in section :ref:`Code`

Input file
===========

The code requires a plain text ``input`` file with extension ``.lowdin``. Here is an example of a minimum ``input`` file for computing muonic water with propagator theory

.. literalinclude:: mu-H2O.APMO.P2.lowdin

The minimum required blocks to run a calculation are ``GEOMETRY``,  ``TASKS``, and ``CONTROL``.

The ``GEOMETRY`` block provides the information needed to build the molecular system. 
The first column declares the type of the quantum species. 
As shown in the above example, ``e-[H]`` and ``e-[O]`` define the electrons of a Hydrogen and a Oxygen atom respectively; ``U-`` defines a negative muon, ``O dirac``, ``H\_1`` and ``H\_2`` define a :math:`^{16}\text{O}`, :math:`^{1}\text{H}` and :math:`^{2}\text{H}` nuclei respectively. 

The second column declares the basis sets. When the ``dirac`` basis is chosen, the particle is treated as a classical point charge. 
The third, fourth and fifth columns declare the $x,y,z$ coordinates of the particle basis set center.

The sixth column provides additional information via keywords  ``addParticles`` and ``multiplicity``. 
These keywords are used to change the default values. ``addParticles`` is used to modify the number of particles of a quantum species. 
As shown in the provided example, one electron is removed from the system. ``multiplicity`` defines the multiplicity for open shell calculations. 
In the example, an electronic multiplicity of 2 was chosen. 


How to run
==========

To run openLOWDIN with 4 OMP threads simply run 

.. code-block:: bash

        openlowdin -i inputname.lowdin -n 4

This will generate a plain text output file called ``inputname.out``. These are the full command line options:

.. code:: 

   $ openlowdin -i file.lowdin [-t [all] [list] [file]] [-n number] [-v number] [-p] [-s] [-h] 

   -i file.lowdin
      This is the input file name
   -n number
      This will set the number of OMP threads
   -t all
      This will run all the test files located on the test database.
   -t list
      This will list all the test files located on the test database.
   -t file
      This will run a specific test file which is located on test database.
   -v number
      This is the lowdin version that will be used
   -p
      This will print the output file to the standard output on the fly
   -w
      This will save the LOWDIN .wfn file
   -k
      This will keep the temporary files in the scratch directory after running the calculation
   -s
      This activate the singleton mode
   -h
      This will print this same message

Scratch
=======
 
openLOWDIN creates a folder to save temporary files located at ``$LOWDIN_SCRATCH/$nameFile`` where ``$nameFile`` is the input name given after the command line ``-i file.lowdin``  without the ``.lowdin`` extension. 
The ``$LOWDIN_SCRATCH`` environmental variable is set in the bash script ``.openlowdin/lowdinvars.sh`` which is located in the installation folder during configuration.  

.. warning::

   Please notice that the scratch folder is completely removed after the calculation terminates.
