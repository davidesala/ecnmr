# ecnmr
`ecnmr` is a python script that exploits evolutionary couplings to extract interface residues from NMR-derived ambiguous contacts 

- [Overview](#overview)
- [Documentation](#documentation)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Setting up the development environment](#setting-up-the-development-environment)
- [License](#license)
- [Issues](https://github.com/neurodata/mgcpy/issues)

# Overview
``ecnmr`` aims to extract a list of interface residues that can be provided as ambiguous interaction restraints in protein-protein docking. Four input files are needed: the PDB of the monomeric protein, one or more evolutionary couplings list, the cyana NMR-derived abiguous contacts list and the naccess rsa file with the per-residue solvent accessibility of the monomeric protein. Two parameters are tunable: a distance cutoff above with false-positive inter-monomeric contacts are ruled out and a probability cutoff below with the ECs are not taken in account. The script works on all the platforms supporting python2.7 and can be downloaded from GitHub.

# System requirements 
## Hardware requirements
`ecnmr` package requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
`ecnmr` requires python 2.7 and Naccess. Naccess is a stand alone program that calculates the accessible area of a molecule from a PDB (Protein Data Bank) format file. It can be downloaded for free for researchers at academic and  non profit-making institutions at http://wolf.bms.umist.ac.uk/naccess/

### OS Requirements
The script can work on all the platforms and has been tested on the following systems:
+ macOS: El Capitan (10.11.6), Mojave (10.14.1)
+ Linux: Ubuntu 18.04

### Python Dependencies
`ecnmr` depends on the following Python modules: re, numpy, string and argparse.
