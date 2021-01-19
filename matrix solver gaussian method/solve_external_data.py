'''solves linear equations from file: in.txt with solvers and outputs the result in out.txt'''

import csv
import numpy as np
import solvers

###read data
matrix = []
with open('in.txt','r',encoding='utf-8') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        if row[0][0] == '#':
            continue
#convert to float numbers
        pos=0
        while pos<len(row):
        	row[pos]=float(row[pos])
        	pos+=1
        matrix.append(row)

bb = np.array(matrix.pop(len(matrix)-1)) #vector
aa = np.array(matrix)

print('matrix:','\n',aa,'\n\n','vector:','\n',bb,'\n')

###solve
xx_gauss = solvers.gaussian_eliminate(aa, bb)
print("solution:",'\n',xx_gauss)

###output
file = open('out.txt','w',encoding='utf-8')
file.write(str(xx_gauss))
file.close()
