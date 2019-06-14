# ecnmr
`ecnmr` is a python script that exploits evolutionary couplings to extract interface residues in protein homo-multimers from NMR-derived ambiguous contact lists 

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Demo](#Demo)
- [Instructions for use](#Instructions-for-use)
- [Ecnmr protocol](#ecnmr-protocol)
- [License](#license)


# Overview
``ecnmr`` aims to extract a list of interface residues that can be provided as ambiguous interaction restraints in protein-protein docking. Four input files are needed: the PDB file of the monomeric protein, one (or more) lists of evolutionary couplings (ECs), the list of NMR-derived ambiguous contacts in CYANA format and the naccess rsa file with the per-residue solvent accessibility of the monomeric protein. There are two tunable parameters: a distance cutoff below which intra-monomeric contacts are removed and a probability cutoff below with the ECs are not taken in account. The script works on all the platforms supporting python2.7 and can be downloaded from GitHub.

# System requirements 
## Hardware requirements
The `ecnmr` package requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
`ecnmr` requires python2.7 and Naccess. Naccess is a stand alone program that calculates the accessible area of a molecule from a PDB file. It can be downloaded for free by researchers at academic and non profit-making institutions from http://wolf.bms.umist.ac.uk/naccess/

### OS Requirements
The script can work on all the platforms and has been tested on the following systems:
+ macOS: El Capitan (10.11.6), Mojave (10.14.1)
+ Linux: Ubuntu 18.04

### Python Dependencies
`ecnmr` depends on the following Python modules: 
```
- re 
- numpy 
- string
- argparse
```

# Installation Guide
The stand-alone `ecnmr` script can be downloaded from GitHub 
```
git clone https://github.com/davidesala/ecnmr 
```

# Demo
Detailed instructions to run `ecnmr.py` can be obtained by typing
```
python ecnmr.py -h
```
Expected output
```
List of matched interface residues:
Res1
Res2
Res3
...
...
Percentage of solvent accessible area represented by the list of residues:
###%
```
Expected run time on a normal desktop
```
less than a minute
```
# Instructions for use
## Instructions for use on your data
To run the script on your data 
```
python ecnmr.py [-h] -m PDBFILE -l ECFILE -e CYANAFILE -s NACCESSFILE (rsa format) [-d DIST_VALUE] [-p PROB_VALUE]
```
## Reproduction instructions
To reproduce the results reported in the manuscript on the L-asparaginase II type
```
python ecnmr.py -m '6EOK.pdb' -l 'gremlin.rr.txt' -l 'raptorx.rr.txt' -l 'respre.rr.txt' -e 'cyana_ss.upl' -s '6EOK.rsa' -d 12.0 -p 0.25
```
To reproduce the results reported in the manuscript on the Sod1 (run1) type
```
python ecnmr.py -m '3ECU.pdb' -l 'gremlin.rr.txt' -l 'raptorx.rr.txt' -l 'respre.rr.txt' -e 'cyana_ss.upl' -s '3ECU.rsa' -d 12.0 -p 0.25
```
To reproduce the results reported in the manuscript on the Sod1 (run2) type 
```
python ecnmr.py -m '3ECU.pdb' -l 'gremlin.rr.txt' -l 'raptorx.rr.txt' -l 'respre.rr.txt' -e 'cyana_sol.upl' -s '3ECU.rsa' -d 12.0 -p 0.3
```
# Ecnmr protocol
![Ecnmr protocol](https://github.com/davidesala/ecnmr/blob/master/protocol.png)

# License

This project is covered under the **MIT License**.
