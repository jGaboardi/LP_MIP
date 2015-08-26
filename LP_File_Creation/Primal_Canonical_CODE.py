# -*- coding: utf-8 -*-
# The Canonical Primal Linear Programming Problem 
# This script creates a linear programming file to be read into an optimizer.
'''
GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
'''
# Developed by:  James D. Gaboardi, MSGIS
#                08/2015
#                © James Gaboardi


#    1. IMPORTS
# Other imports may be necessary for matrix creation and manipulation 
import numpy as np


#    2. DEFINED FUNCTIONS
# Objective Function 
def get_objective_function_CPLPP():
    outtext = ' obj: '
    temp = ''
    for j in range(cols):
        temp += str(Cj[j]) + 'y' + str(j+1) + ' + '
    outtext += temp + ' \n      '
    outtext = outtext[:-11] + ' \n'
    return outtext

# Add Constraints

# Declaration of Bounds




# Declaration of Decision Variables (form can be: Binary, Integer, etc.)
# In this case decision variables are General.

#    3. DATA READS & VARIABLE DECLARATION
#  Constants
Aij = np.random.randint(5, 50, 25)
Aij = Aij.reshape(5,5)
AijSum = np.sum(Aij)
Cj = np.random.randint(10, 20, 5)
CjSum = np.sum(Cj)
Bi = np.random.randint(10, 20, 5)
BiSum = np.sum(Bi)
    # Matrix Shape
rows, cols = Aij.shape


#    4. START TEXT FOR .lp FILE
# Declaration of Objective Function
text = "The Canonical Primal Linear Programming Problemn"
text += "'''\n"
text += 'Minimize\n'          
text += get_objective_function_CPLPP()
text += '\n'
# Declaration of Constraints



# Declaration of Decision Variables form: Binaries
text += 'Binaries\n'
#text += get_decision_variables()
text += '\n'
text += 'End\n'
text += "'''\n"
text += "© James Gaboardi, 2015"                


#   5. CREATE & WRITE .lp FILE TO DISK
# Fill path name  --  File name must not have spaces.
outfile = open('name.lp', 'w')
outfile.write(text)
outfile.close()
