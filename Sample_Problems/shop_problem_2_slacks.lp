Maximize
    9 x + 7 y + 3 z
Subject To
    c1: 10 x + 5 y + 4 z + a = 15
    c2: 6 x + 6 y + 8 z + b = 44
    c3: 4.5 x + 18 y + 12 z + c = 22
    c4: 21 x + 42 y + 17 z + d = 99
    c5: 4.5 x + 18 y + 19 z + f = 132
Bounds
    x >= 0
    y >= 0
    z >= 1
    a >= 0
    b >= 0
    c >= 0
    d >= 0
    f >= 0
End
'''


Mathematical Optimization of Profit
The Shop Problem with Slack Variables
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
Constraint 4 = Machine 3 time (hrs.)
Constraint 5 = Machine 3 time (hrs.)


Adapted from:
    Greenwald, D. U.
    1957
    Linear Programming: An Explanation of the Simplex Algorithm
    New York, NY
    The Ronald Press Company