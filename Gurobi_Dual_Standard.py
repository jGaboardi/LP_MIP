'''
GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
'''
# Building a Standard Dual Linear Programming Problem 
#            in Python/Gurobi[gurobipy]

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

def GbpDualStd():
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
    mDual_Standard_GUROBI = gbp.Model(' -- Standard Dual Linear Programming Problem -- ')
    
    # Set Focus to Optimality
    gbp.setParam('MIPFocus', 2)
    
    # Decision Variables
    desc_var = []
    for orig in rows:
        desc_var.append([])
        desc_var[orig].append(mDual_Standard_GUROBI.addVar(vtype=gbp.GRB.CONTINUOUS, 
                                        name='u'+str(orig+1)))
    # Slack Variables
    slack_var = []
    for dest in cols:
        slack_var.append([])
        slack_var[dest].append(mDual_Standard_GUROBI.addVar(vtype=gbp.GRB.CONTINUOUS, 
                                    name='t'+str(dest+1)))
    # Update Model
    mDual_Standard_GUROBI.update()
    
    #Objective Function
    mDual_Standard_GUROBI.setObjective(gbp.quicksum(Bi[orig]*desc_var[orig][0] 
                            for orig in rows), 
                            gbp.GRB.MAXIMIZE)
    # Constraints
    for dest in cols:
        mDual_Standard_GUROBI.addConstr(gbp.quicksum(Aij[orig][dest]*desc_var[orig][0] 
                            for orig in rows) + 
                            slack_var[dest][0] -
                            Cj[dest] == 0)
    
    # Optimize
    try:
        mDual_Standard_GUROBI.optimize()
    except Exception as e:
        print '   ################################################################'
        print ' < ISSUE : ', e, ' >'
        print '   ################################################################'
        
    # Write LP file
    mDual_Standard_GUROBI.write('LP.lp')
    print '\n*************************************************************************'
    print '    |   Decision Variables'
    for v in mDual_Standard_GUROBI.getVars():
        print '    |  ', v.VarName, '=', v.x
    print '*************************************************************************'
    val = mDual_Standard_GUROBI.objVal
    print '    |   Objective Value ------------------ ', val
    print '    |   Aij Sum -------------------------- ', AijSum
    print '    |   Cj Sum --------------------------- ', CjSum
    print '    |   Bi Sum --------------------------- ', BiSum
    print '    |   Matrix Dimensions ---------------- ', Aij.shape
    print '    |   Date/Time ------------------------ ', dt.datetime.now()
    print '*************************************************************************'
    print '-- Gurobi Standard Dual Linear Programming Problem --'

try:
    GbpDualCStd()
    print '\nJames Gaboardi, 2015'
except Exception as e:
        print '   ################################################################'
        print ' < ISSUE : ', e, ' >'
        print '   ################################################################'