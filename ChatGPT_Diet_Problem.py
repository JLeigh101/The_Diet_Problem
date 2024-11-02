from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, value

# Create a linear programming problem
problem = LpProblem("Grocery_Cost_Minimization", LpMinimize)

# Define decision variables
x1 = LpVariable('Eggs', lowBound=0, cat='Integer')  # Quantity of eggs
x2 = LpVariable('Bacon', lowBound=0, cat='Integer')  # Quantity of bacon
x3 = LpVariable('Lentils', lowBound=0, cat='Integer')  # Quantity of lentils
x4 = LpVariable('Tomatoes', lowBound=0, cat='Integer')  # Quantity of tomatoes
x5 = LpVariable('Pasta', lowBound=0, cat='Integer')  # Quantity of pasta

# Objective function
problem += (1.5 * x1 + 1.25 * x2 + 1.59 * x3 + 2.99 * x4 + 8.99 * x5), "Total Cost"

# Nutritional Constraints
problem += (195 * x1 + 540 * x2 + 595 * x3 + 630 * x4 <= 35000), "Sodium"
problem += (180 * x1 + 180 * x2 + 350 * x3 + 140 * x4 + 600 * x5 >= 14000), "Energy"
problem += (18 * x1 + 12 * x2 + 28 * x3 + 7 * x4 + 24 * x5 >= 350), "Protein"
problem += (18 * x1 + 0.6 * x2 >= 140), "Vitamin D"
problem += (90 * x1 + 30 * x2 + 105 * x3 + 45 * x5 >= 9100), "Calcium"
problem += (2.7 * x1 + 0.6 * x2 + 6.65 * x3 + 5.1 * x5 >= 126), "Iron"
problem += (210 * x1 + 210 * x2 + 840 * x3 + 1400 * x4 + 417 * x5 >= 32900), "Potassium"

# Solve the problem
problem.solve()

# Output results
print("Status:", LpStatus[problem.status])
for v in problem.variables():
    print(f"{v.name}: {v.varValue}")

print("Total Cost: $", value(problem.objective))
