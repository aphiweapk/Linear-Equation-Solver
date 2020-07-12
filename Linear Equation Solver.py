# Linear Equation Solver
# Solve for X
# Format 2x + 4 = 8
# Format 5x - 10 = 0

print('''Format:2X + 4 = 4
Input:
2
4
4

Output:
x = 0''')
print()

print('Solve for X:')
print()
co_eff_x = float(input("Enter the Coefficient of X[positive/negative]: "))
print()

constant = float(input("Enter the left side constant of equation[positive/negative]: "))
print()

const_after_eq = float(input("Enter the right side constant of equation: "))
print()

if constant == 0:
	print("X =",const_after_eq/co_eff_x)

elif constant > 0:
	print("X=",((constant*-1+const_after_eq)/co_eff_x))
	
elif constant < 0:
	print("X = ",((constant*-1+const_after_eq)/co_eff_x))
