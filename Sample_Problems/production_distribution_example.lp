Maximize
    2400 x + 3400 y + 1800 z
Subject To
    c1: 6 x + 12 y + 4 z <= 160
    c2: 3 x + 2 y + 15 z <= 160
    c3: 8 x + 2 y + 20 z <= 320
    c4: - y + x >= 0
    c5: - y + z >= 0
Bounds
    x >= 1
    y >= 2
    z >= 1
End
'''

Mathematical Optimization of Profit
A Procurement, Production, and Distribution Problem
Example Linear Programming Problem
James Gaboardi, MSGISci
8/2015

This .lp file can be read into a solver (CPLEX, Gurobi, etc.)

VARIABLES:
x = mid grade product   --> $2400 for each unit of [x]
y = high grade product  --> $3400 for each unit of [y]
z = low grade product   --> $1100 for each unit of [z]

CONSTRAINTS:
Constraint 1 = Travel time for procurement (hrs.)
Constraint 2 = Production time (hrs.)
Constraint 3 = 'Hardship' time for production distribution (hrs.)
Constraint 4 = Ratio of x to y Production
Constraint 5 = Ratio of z to y Production

BOUNDS:
One or more units of [x] and [z] and two or more units of [y] must be distributed.