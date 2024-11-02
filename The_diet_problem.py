#NU MSDS 460 Assignment 1 - The Diet Problem
#John Leigh
#Linear Programming - Minimization using Pulp

import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpMinimize, LpStatus, value

print("Assignment 1, Part 3: Solve the diet problem using Pulp, values can contain zeros:")

#create lp variable with minimization parameter
lp = LpProblem("Diet_Problem", LpMinimize)

#define variables (values can include zero)
x1 = LpVariable("3 Eggs", 0, None)
x2 = LpVariable("3 Pieces of Bacon", 0, None)
x3 = LpVariable("Can of Lentils", 0, None)
x4 = LpVariable("Can of Tomatoes", 0, None)
x5 = LpVariable("3 servings of pasta", 0, None)

#add the weekly nutritional component amounts
sodium = 7*5000
energy = 7*2000
protein = 7*50
vitamin_d = 7*20
iron = 7*18
potassium = 7*4700
calcium = 7*1300

#add the constraints for each nutrient
lp += 195*x1 + 540*x2 + 595*x3 + 630*x4 <= sodium #sodium values
lp += 180*x1 + 180*x2 + 350*x3 + 140*x4 + 600*x5 >= energy #energy values
lp += 18*x1 + 12*x2 + 28*x3 + 7*x4 + 24*x5 >= protein #protein values
lp += 18*x1 + 0.6*x2 >= vitamin_d #vitamin d values
lp += 2.7*x1 + 0.6*x2 + 6.65*x3 + 5.1*x5 >= iron #iron values
lp += 210*x1 + 210*x2 + 840*x3 + 1400*x4 + 417*x5 >= potassium #potassium values
lp += 90*x1 + 30*x2 + 105*x3 + 45*x5 >= calcium #calcium values

#define the objective function
lp += 1.5*x1 + 1.25*x2 + 1.59*x3 + 2.99*x4 + 8.99*x5

#solve the problem
status = lp.solve()

#print results
for variable in lp.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(lp.objective)}")

print(" \n\n -------------------------------- \n\n")
print("Assignment 1, Part 4: Solve the diet problem using Pulp, values can not contain zeros:")

#create lp variable with minimization parameter
lp = LpProblem("Diet_Problem", LpMinimize)

#define variables with min value of 1
x1 = LpVariable("3 Eggs", 1, None)
x2 = LpVariable("3 Pieces of Bacon", 1, None)
x3 = LpVariable("Can of Lentils", 1, None)
x4 = LpVariable("Can of Tomatoes", 1, None)
x5 = LpVariable("3 servings of pasta", 1, None)

#add the constraints for each nutrient
lp += 195*x1 + 540*x2 + 595*x3 + 630*x4 <= sodium #sodium values
lp += 180*x1 + 180*x2 + 350*x3 + 140*x4 + 600*x5 >= energy #energy values
lp += 18*x1 + 12*x2 + 28*x3 + 7*x4 + 24*x5 >= protein #protein values
lp += 18*x1 + 0.6*x2 >= vitamin_d #vitamin d values
lp += 2.7*x1 + 0.6*x2 + 6.65*x3 + 5.1*x5 >= iron #iron values
lp += 210*x1 + 210*x2 + 840*x3 + 1400*x4 + 417*x5 >= potassium #potassium values
lp += 90*x1 + 30*x2 + 105*x3 + 45*x5 >= calcium #calcium values

#define the objective function
lp += 1.5*x1 + 1.25*x2 + 1.59*x3 + 2.99*x4 + 8.99*x5

#solve the problem
status = lp.solve()

#print results
for variable in lp.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(lp.objective)}")