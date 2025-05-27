# openLOWDIN manual #

![openLOWDIN logo](docs/source/logo/openLowdin_logo_v2_white_black.svg) 

This online manual has been developed with Sphinx.

website: https://openlowdin.github.io/openLOWDIN_manual/

[![Sphinx: Render docs](https://github.com/openLOWDIN/openLOWDIN_manual/actions/workflows/sphyinx.yml/badge.svg)](https://github.com/openLOWDIN/openLOWDIN_manual/actions/workflows/sphyinx.yml)

[![pages-build-deployment](https://github.com/openLOWDIN/openLOWDIN_manual/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/openLOWDIN/openLOWDIN_manual/actions/workflows/pages/pages-build-deployment)

© All rights reserved, 2025.

Installation notes.
=============

### Prerequisites: ###

* Sphinx 
* pdflatex

### Compile html ###

* run `make html`

### Compile pdf(LaTeX) ###

* run `make latexpdf`

### clean ###

* run `make clean`


### Tips ###

* Check whitespace and empty lines.

* Links to sections in the same Document require the full title header declared in the file.

* Use pandoc to convert latex to rst. 

`pandoc -s -f latex file.tex -t rst > file.rst`

