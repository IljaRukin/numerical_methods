"""Routines for solving a linear system of equations."""
import numpy as np


def gaussian_eliminate(aa, bb):
    """Solves a linear system of equations (Ax = b) by Gauss-elimination

    Args:
        aa: Matrix with the coefficients. Shape: (n, n).
        bb: Right hand side of the equation. Shape: (n,)

    Returns:
        Vector xx with the solution of the linear equation or None
        if the equations are linearly dependent.
    """


    dimensions = np.shape(aa)

##################################################test dimensions
    if dimensions[0] != dimensions[1] or dimensions[0] != len(bb):
        raise TypeError('matrix not quadratic')
    else:
        pass

##################################################modify vektor bb --> cc
    cc = []
    for kk in range(0,len(bb)):
        cc.append([bb[kk]])

##################################################add vektor cc to matrix cc
    aa = np.append(aa, cc,1)

##################################################triangle matrix
    pos = 0; counter = 0
    while pos < dimensions[1]:
        line = pos + 1
        while line < dimensions[0]:
            if aa[pos][pos] != 0:
                aa[line] = aa[line] - (aa[line][pos]/aa[pos][pos]) * aa[pos]
            elif line == dimensions[0] or counter == dimensions[1] - pos:
                pass
            else:
                #rotate matrix
                cache = np.array(aa[pos])
                iterate = pos
                while iterate < dimensions[0]-1:
                    aa[iterate] = np.array(aa[iterate+1])
                    iterate += 1
                aa[dimensions[0]-1] = cache
                counter += 1
                line = line - 1
            counter = 0
            line += 1
        pos += 1


##################################################test for zero lines

    k=0
    while k < dimensions[1]:
        kk = 0
        while kk < dimensions[0]:
            if aa[k][kk] != 0:
                kk=dimensions[0]
            elif kk != dimensions[0]-1:
                kk += 1
            else:
                return None
        k += 1

##################################################diagonal matrix
    pos = dimensions[1] -1
    while pos >= 0:
        line = pos -1
        while line >= 0:
            aa[line] = aa[line] - (aa[line][pos]/aa[pos][pos]) * aa[pos]
            line -= 1
        pos -= 1

##################################################unit matrix
    for ii in range(0,dimensions[0]):
        aa[ii] = aa[ii]/aa[ii][ii]

##################################################resulting values
    xx = np.zeros((dimensions[1],), dtype=float)
    for jj in range(0,dimensions[0]):
        xx[jj] = aa[jj][dimensions[1]]

    return xx