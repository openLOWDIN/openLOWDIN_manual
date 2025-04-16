============
Installation
============

Dependencies
============

openLOWDIN requires the following standard packages:

.. code::

  wget git build-essential liblapack-dev libblas-dev libgsl0-dev autotools-dev automake libtool gfortran python3 gawk libeigen3-dev libgmp-dev libboost-all-dev

Additionally, it requires some quantum chemistry libraries:

::

  libinit - Molecular integrals in gaussian type orbital basis
  libxc - DFT functionals 

The following opensource libraries are distributed within the openLOWDIN code

.. code::

  aduw - Four-index integrals transformation 
  erkale - Orbital localization
  gepol - COSMO 
  jadamilu - large sparse matrix diagonalization
  molden2aim - molden to AIM wave function converter

Getting the code
================

The source code is available at https://github.com/efposadac/openLOWDIN

.. code:: bash

  git clone https://github.com/efposadac/openLOWDIN

Basic installation
==================

Once all the dependencies are installed, the code is compile with the following steps.
First, run the interactive configuration script in openLOWDIN root directory. 
Be sure that you have permissions to write in the installation directory and have properly exported the `$PATH` environment.

.. code:: bash

  ./configure

This script will ask a set of questions, please provide the option that satisfies your needs.

.. code::

  INFO: Interactive configuration options
  Fortran Compiler command? gfortran(default) or ifort/ifx [gfortran]
  
  Compiler Options: (1) regular,  (2) backtrace and debug,  (3) static (for intel fortran compiler only), (4) Full debug, (5) Highest optimization level [1]
  
  Speed up on GPUs? (you need to have already installed CUDA and Magma libraries): yes/no [no]
  
  Executable name? default=openlowdin [openlowdin]
  
  Installation directory? default=/usr/local [/usr/local]

Compile the code with 

.. code:: bash

  make

you can add the parallel flag to compile in paralle, e.g. with 4 threads as `-j 4`. 

Finally, install as

.. code:: bash

  make install

To uninstall the binaries from the selected installation folder

.. code:: bash

  make uninstall

To clean the project

.. code:: bash

  make clean
  make distclean

Step-by-step installation
=========================

Here you can find a step-by-step workflow to install on ubuntu-latest linux distribution.

.. code:: bash

  ### Step-by-step  installation example: (replace apt-get with your preferred package manager) ###
  
          sudo apt-get update
          sudo apt-get -y install wget git build-essential liblapack-dev libblas-dev libgsl0-dev autotools-dev automake libtool gfortran python3 gawk libeigen3-dev libgmp-dev libboost-all-dev
          # Define ENV Variables
          export WORKDIR=$PWD/dependencies
          export PATH=$PATH:$WORKDIR/bin
          export C_INCLUDE_PATH=$C_INCLUDE_PATH:$WORKDIR/include:$WORKDIR/include/libint2:/usr/include/eigen3
          export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:$WORKDIR/include:$WORKDIR/include/libint2:/usr/include/eigen3
          export LIBRARY_PATH=$LIBRARY_PATH:$WORKDIR/lib
          export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$WORKDIR/lib
          # Create work directories
          mkdir $WORKDIR
          mkdir $WORKDIR/bin
          mkdir $WORKDIR/lib
          cd $WORKDIR
  
  	# Libint2
          # If you have Ubuntu, you can get this precompiled Libint2 library
          wget https://www.dropbox.com/s/d3d44j238lkfwcr/libint-master-SEP052019.tgz
          tar xzvf libint-master-SEP052019.tgz
  
  	# Otherwise, download and compile with minimal (default am), G12, fPIC options (libint2 commit 668b10c4bdca5876984058742d4212675eb93f3f)
  	# git clone https://github.com/evaleev/libint.git
  	# cd libint
  	# git checkout 668b10c4bdca5876984058742d4212675eb93f3f
  	# ./autogen.sh
  	# mkdir ../build
          # cd ../build
          # ../libint/configure --prefix=$WORKDIR --with-max-am=6 --enable-g12=4 --with-g12-max-am=4 --with-cxxgen-optflags
          # make -j 4
          # make install
  	# ../libint/configure --prefix=$WORKDIR
  
          cd -
  	
          # Libint1
          git clone https://github.com/evaleev/libint.git
          cd libint
          git checkout v1
          aclocal -I lib/autoconf
          autoconf
          ./configure --prefix=$WORKDIR
          make -j 4
          make install
          make clean
          make distclean
          cd -
  
  	# Libxc
          cd $WORKDIR        
          # If you have Ubuntu, you can get this precompiled Libxc library
          wget https://www.dropbox.com/s/6cja3zzhl1cq46i/libxc-master-MAY242023.tgz
          tar xzvf libxc-master-MAY242023.tgz
  	# Otherwise, download and compile with default options (libxc commit 4bd0e1e36347c6d0a4e378a2c8d891ae43f8c951)
  	# git clone https://gitlab.com/libxc/libxc.git
  	# cd libxc
  	# git checkout 4bd0e1e36347c6d0a4e378a2c8d891ae43f8c951
  	# autoreconf -i
  	# ./configure --enable-shared --prefix=$WORKDIR
  	# make -j 4
  	# make install
  
          cd ..
  	
          # Configure Lowdin
          ./configure -p $WORKDIR/bin -s /tmp -l "-lblas -llapack"
          # Build Lowdin
          make -j 4
          # Install Lowdin
          make install
          # Run Tests
          make test
  
