#!/usr/bin/env python
# -*- coding: UTF-8  -*-


"""
Interface residues prediction.

Authors:
           SALA Davide
           GIACHETTI Andrea
           ROSATO Antonio
"""


import re
import numpy as np
from string import split
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--pdb-monomer', action='store', dest='pdbfile',
                        help='Add single chain PDB', required=True)

    parser.add_argument('-l', '--list', action='append', dest='ecfile',
                        default=[],
                        help='Add ECs files (rr or gremlin format)', required=True)

    parser.add_argument('-e', '--exper', action='store', dest='cyanafile',
                        help='Ambiguous NMR contacts list (cyana format)', required=True)

    parser.add_argument('-s', '--solvent', action='store', dest='naccessfile', required=True,
                        help='Naccess rsa file')

    parser.add_argument('-d', '--distance', action='store', dest='dist_value', type=float, default=10.0,
                        help='Distance cutoff')

    parser.add_argument('-p', '--prob', action='store', dest='prob_value', type=float, default=0.3,
                        help='Probability cutoff')

    results = parser.parse_args()
    totalec = reduce(lambda s, a: open(a, "r").readlines() + s, results.ecfile, [])
    MINDIST = float(results.dist_value)
    MINPROB = float(results.prob_value)
    cadiz = get_CA_coord(open(results.pdbfile, "r").readlines())
    dizec = filtering(filter_input(totalec), cadiz, MINDIST, MINPROB)
    dizecg = formatting(open(results.cyanafile, "r").readlines(), dizec)
    sasa(open(results.naccessfile, "r").readlines(), dizecg)


def regex_findCA(a):
    return bool(re.match(r"^ATOM\s{2,}[0-9]+\s+CA\s", a))


def regex_filterEC(a):
    return bool(re.match(r"^[0-9]+\s+[0-9]+\s+[0-9 _ A-Z]+\s+[0-9 _ A-Z]+\s+[0-9 .]+\s+[0-9 .]+\s+[0-9 .]+$", a)) or \
           bool(re.match(r"^\s+[0-9]+\s+[0-9]+\s+[0-9 .]+$", a)) or \
           bool(re.match(r"^\s*[0-9]+\s+[0-9]+\s[0-9]+\s+[0-9]+\s+[0-9 .]+", a))


def filter_input(inp):
    return filter(lambda a: regex_filterEC(a), inp)


def get_CA_coord(inp):
    ca_line = filter(lambda a: regex_findCA(a), inp)
    cadiz = reduce(lambda d, a: d.update({int(a[22:26].strip()): a[30:54]}) or d, ca_line, {})
    return cadiz


def create_diz1RES(diz1RES, a, distca, mindist, minprob):
    raw = split(a)
    if len(raw) == 5 or len(raw) == 7:
        keys = str("%-5s" % raw[0] + "%-5s" % raw[1]).strip()
        if not diz1RES.has_key(keys):
            diz1RES[keys] = {}
            if len(raw) == 5:
                diz1RES[keys]["prob"] = float(raw[4])

            elif len(raw) == 7:
                print raw
                diz1RES[keys]["prob"] = float(raw[6])

        else:

            if len(raw) == 5:
                if (float(raw[4]) > float(diz1RES[keys]["prob"])):
                    diz1RES[keys]["prob"] = float(raw[4])
            elif len(raw) == 7:
                if (float(raw[6]) > float(diz1RES[keys]["prob"])):
                    diz1RES[keys]["prob"] = float(raw[6])

        if distca.has_key(int(raw[0].strip())) and distca.has_key(int(raw[1].strip())):
            dist1 = np.fromstring(distca[int(raw[0].strip())], dtype=float, sep=' ')
            dist2 = np.fromstring(distca[int(raw[1].strip())], dtype=float, sep=' ')
            distp = np.around(np.sqrt(np.sum((dist1 - dist2) ** 2)), decimals=1)
            diz1RES[keys]["dist"] = distp

        else:
            del diz1RES[keys]

        if diz1RES.has_key(keys):
            if diz1RES[keys]["dist"] > mindist and "50   113" in keys:
                print "-------------"
                print keys, diz1RES[keys]
                print "-------------"
            if diz1RES[keys]["dist"] < mindist or diz1RES[keys]["prob"] < minprob:
                del diz1RES[keys]

    return diz1RES


def filtering(totalec, cadiz, mindist, minprob):
    dizEC = reduce(lambda diz, current: create_diz1RES(diz, current, cadiz, mindist, minprob), totalec, {})
    return dizEC


def filter_cyana(a, cyana):
    return ([a[0].split()[0], a[0].split()[1]] in cyana) or ([a[0].split()[1], a[0].split()[0]] in cyana)


def filter_cyana_regex(a):
    return bool(re.match(r"^[0-9\s]{3}\s[A-Z]{3}\s\s[1-9A-Z\s]{4}\s[0-9\s]{4}\s", a))


def formatting(cyana, dizec):
    cyanafilter = filter(lambda a: filter_cyana_regex(a), cyana)
    cyanamap = map(lambda a: [a.split()[0], a.split()[3]], cyanafilter)

    diznew = dict(filter(lambda a: filter_cyana(a, cyanamap), dizec.items()))
    return diznew


def filter_sasa_red(s, a):
    if (float(a[9:-1].split()[4]) >= 40.0 or float(a[9:-1].split()[6]) >= 40.0):
        return s.append(a[9:-1].split()[0])


def filter_sasa(a, nacc):
    res = a[0].split()
    return res[0] in nacc or res[1] in nacc


def filter_sasa1(s, a, nacc):
    res = a[0].split()
    if res[0] in nacc:
        s.append(int(res[0]))
    if res[1] in nacc:
        s.append(int(res[1]))
    return s


def sasa(nacc, diz):
    naccf = filter(lambda a: bool(re.match(r"^RES", a)), nacc)
    naccfacc = reduce(lambda s, a: filter_sasa_red(s, a) or s, naccf, [])
    diznew1 = reduce(lambda s, a: filter_sasa1(s, a, naccfacc), diz.items(), [])
    unec = sorted(list(set(diznew1)))
    print("List of matched interface residues:")
    for i in unec:
        print i

    print("Percentage of solvent accessible area represented by the list of residues:")
    print("%3.1f" % (float(len(unec)) / float(len(naccfacc)) * 100.0)+" %")


if __name__ == '__main__':
    main()
