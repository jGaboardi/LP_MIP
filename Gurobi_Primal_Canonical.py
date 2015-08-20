'''
GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
'''
# Building a Canonical Primal Linear Programming Problem 
#    in Python/Gurobi[gurobipy]
#
'''
Adapted from:
    Daskin, M. S.
    1995
    Network and Discrete Location: Models, Algorithms, and Applications
    Hoboken, NJ, USA: John Wiley & Sons, Inc.
'''
# Imports
import numpy as np
import gurobipy as gbp
import datetime as dt

#  Constants
Aij = np.random.randint(5, 50, 25)
Aij = Aij.reshape(5,5)
AijSum = np.sum(Aij)
Cj = np.random.randint(10, 20, 5)
CjSum = np.sum(Cj)
Bi = np.random.randint(10, 20, 5)
BiSum = np.sum(Bi)

# Matrix Shape
rows = range(len(Aij))
cols = range(len(Aij[0]))

# Instantiate Model
mPrimal_Canonical_GUROBI = gbp.Model(' -- Canonical Primal Linear Programming Problem -- ')

# Set Focus to Optimality
gbp.setParam('MIPFocus', 2)

# Decision Variables
desc_var = []
for dest in cols:
    desc_var.append([])
    desc_var[dest].append(mPrimal_Canonical_GUROBI.addVar(vtype=gbp.GRB.CONTINUOUS, 
                                    name='y'+str(dest+1)))
# Update Model
mPrimal_Canonical_GUROBI.update()

#Objective Function
mPrimal_Canonical_GUROBI.setObjective(gbp.quicksum(Cj[dest]*desc_var[dest][0] 
                        for dest in cols), 
                        gbp.GRB.MINIMIZE)
# Constraints
for orig in rows:
    mPrimal_Canonical_GUROBI.addConstr(gbp.quicksum(Aij[orig][dest]*desc_var[dest][0] 
                        for dest in cols) - Bi[orig] >= 0)
# Optimize
mPrimal_Canonical_GUROBI.optimize()
# Write LP file
mPrimal_Canonical_GUROBI.write('LP.lp')
print '\n*************************************************************************'
for v in mPrimal_Canonical_GUROBI.getVars():
    print '    |  ', v.VarName, '=', v.x
print '*************************************************************************'
val = mPrimal_Canonical_GUROBI.objVal
print '    |   Objective Value ------------------ ', val
print '    |   Aij Sum -------------------------- ', AijSum
print '    |   Cj Sum --------------------------- ', CjSum
print '    |   Bi Sum --------------------------- ', BiSum
print '    |   Matrix Dimensions ---------------- ', Aij.shape
print '    |   Date/Time ------------------------ ', dt.datetime.now()
print '*************************************************************************'
print '-- Gurobi Canonical Primal Linear Programming Problem --'
print '\nJames Gaboardi, 2015'