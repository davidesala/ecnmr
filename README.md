# ecnmr
`ecnmr` is a python script that exploits evolutionary couplings to extract interface residues from NMR-derived ambiguous contacts 

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Demo](#Demo)
- [Instructions](#Instructions)
- [Ecnmr protocol](#ecnmr-protocol)
- [License](#license)


# Overview
``ecnmr`` aims to extract a list of interface residues that can be provided as ambiguous interaction restraints in protein-protein docking. Four input files are needed: the PDB of the monomeric protein, one or more evolutionary couplings list, the cyana NMR-derived abiguous contacts list and the naccess rsa file with the per-residue solvent accessibility of the monomeric protein. Two parameters are tunable: a distance cutoff above with false-positive inter-monomeric contacts are ruled out and a probability cutoff below with the ECs are not taken in account. The script works on all the platforms supporting python2.7 and can be downloaded from GitHub.

# System requirements 
## Hardware requirements
`ecnmr` package requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
`ecnmr` requires python2.7 and Naccess. Naccess is a stand alone program that calculates the accessible area of a molecule from a PDB (Protein Data Bank) format file. It can be downloaded for free for researchers at academic and  non profit-making institutions at http://wolf.bms.umist.ac.uk/naccess/

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
`ecnmr` only needs to be downloaded from GitHub 
```
git clone https://github.com/davidesala/ecnmr 
```

# Demo
Detailed instructions to run `ecnmr.py` can be found typing
```
python ecnmr.py -h
```
expected output
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
# Instructions
## Instructions for use on your data
To run the script on your data 
```
python ecnmr.py [-h] -m PDBFILE -l ECFILE -e CYANAFILE -s NACCESSFILE [-d DIST_VALUE] [-p PROB_VALUE]
```
## Reproduction instructions
To reproduce the results reported in the manuscript on the L-asparaginase II type
```
python ecnmr.py -m '6EOK.pdb' -l 'gremlin.rr.txt' -l 'raptorx.rr.txt' -l 'nebcon.rr.txt' -l 'respre.rr.txt' -e 'ss.upl' -s '6EOK.rsa' -d 10.0 -p 0.3
```
To reproduce the results reported in the manuscript on the Sod1 (run1) type
```
python ecnmr.py -m '3ECU.pdb' -l 'gremlin.rr.txt' -l 'raptorx.rr.txt' -l 'nebcon.rr.txt' -l 'respre.rr.txt' -e 'ss.upl' -s '3ECU.rsa' -d 10.0 -p 0.3
```
To reproduce the results reported in the manuscript on the Sod1 (run2) type 
```
python ecnmr.py -m '3ECU.pdb' -l 'gremlin.rr.txt' -l 'raptorx.rr.txt' -l 'nebcon.rr.txt' -l 'respre.rr.txt' -e 'sol.upl' -s '3ECU.rsa' -d 13.0 -p 0.3
```
# Ecnmr protocol
![Ecnmr protocol](https://github.com/davidesala/ecnmr/blob/master/protocol.png)

# License

This project is covered under the **Apache 2.0 License**.
