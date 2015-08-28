Maximize
    9 x + 7 y
Subject To
    c1: 10 x + 5 y <= 50
    c2: 6 x + 6 y <= 36
    c3: 4.5 x + 18 y <= 81
Bounds
    x >= 0
    y >= 0
End
'''


Mathematical Optimization of Profit
The Shop Problem
Example Linear Programming Problem
James Gaboardi, MSGISci
8/2015

This .lp file can be read into a solver (CPLEX, Gurobi, etc.)

x = Product 1
y = Product 2

$9 for each unit of [x] and $7 for each unit of [y]

Constraint 1 = Machine 1 time (hrs.)
Constraint 2 = Machine 2 time (hrs.)
Constraint 3 = Machine 3 time (hrs.)


Originally Published:
    Greenwald, D. U.
    1957
    Linear Programming: An Explanation of the Simplex Algorithm
    New York, NY
    The Ronald Press Company