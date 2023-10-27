import sympy as sp

# Define the variables
x, y = sp.symbols('x y')

# Input the equations from the user
equation1_str = input("Enter the first equation (e.g., '13*x + 6*y - 1'): ")
equation2_str = input("Enter the second equation (e.g., '4*x - 2*y - 10'): ")

# Parse the user input into equation objects
equation1 = sp.Eq(sp.sympify(equation1_str), 0)
equation2 = sp.Eq(sp.sympify(equation2_str), 0)

# Solve the system of equations for the intersection
solution = sp.solve((equation1, equation2), (x, y))

# Display the intersection point
if solution:
    if all(sp.Eq(val.as_real_imag()[1], 0) for val in solution.values()):
        # Check if the imaginary parts of the solutions are all zero
        solution = {var: val.evalf() for var, val in solution.items()}
        print(f"The intersection point is at (x, y) = ({solution[x]}, {solution[y]})")
    else:
        print("The equations have infinite solutions or complex solutions.")
else:
    print("No solution found. The equations may be parallel and do not intersect.")