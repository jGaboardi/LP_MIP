Minimize
    x + y
Subject To
    c1: 20 x + 30 y >= 420
    c2: 2 x + 5 y <= 60
Bounds
    0 <= x <= 26
    0 <= y <= 13
Integers
    x
    y
End
'''


Mathematical Optimization of Profit
The Airline Problem
Example Integer Programming Problem
James Gaboardi, MSGISci
9/2015

This .lp file can be read into a solver (CPLEX, Gurobi, etc.)

x = Airplane 1 (one pilot)
y = Airplane 2 (one pilot)

We need to minimize the number of pilots. 

Constraint 1 = Passenger Seats
Constraint 2 = Flight Attendants

Bounds:
    There cannot be more than 26 of Airplane 1 or 13 or Airplane 2.

Originally Published:
    Cohen, S. S.
    1985
    Operational Researh
    London, UK
    Edward Arnold Publishers