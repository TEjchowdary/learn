import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Algebra
expr = (x + 2) * (x - 3)
print('Expanded expression:', sp.expand(expr))

# Solve an equation
solution = sp.solve(sp.Eq(x**2 - 5*x + 6, 0), x)
print('Solutions:', solution)

# Differentiate and integrate
f = sp.sin(x) * x**2
print('Derivative:', sp.diff(f, x))
print('Integral:', sp.integrate(f, x))

# Limits and simplification
print('Limit:', sp.limit(sp.sin(x)/x, x, 0))
print('Simplified:', sp.simplify((x**2 - 1)/(x - 1)))

# Matrix example
A = sp.Matrix([[1, 2], [3, 4]])
print('Determinant:', A.det())
print('Inverse:', A.inv())

# Symbolic equation system
sol = sp.solve([sp.Eq(2*x + y, 5), sp.Eq(x - y, 1)], [x, y])
print('System solution:', sol)
