import numpy as np


# -------------------------------------------------
# 1. Our known data points
# -------------------------------------------------

x_points = [0, 1, 2]
y_points = [1, 3, 7]

n = len(x_points)


# -------------------------------------------------
# 2. Build the Vandermonde matrix
# -------------------------------------------------

V = []

for x in x_points:
    row = []

    for power in range(n):
        row.append(x ** power)

    V.append(row)


print("Vandermonde matrix:")
print(V)


# 3. Convert lists to NumPy arrays


V = np.array(V, dtype=float)
y = np.array(y_points, dtype=float)


# -------------------------------------------------
# 4. Solve the linear system
#
# V * a = y
#
# where:
#
# a = [a0, a1, a2]
#
# and:
#
# P(x) = a0 + a1*x + a2*x^2
# -------------------------------------------------

coefficients = np.linalg.solve(V, y)

print("\nPolynomial coefficients:")
print(coefficients)


# -------------------------------------------------
# 5. Display the coefficients separately
# -------------------------------------------------

a0 = coefficients[0]
a1 = coefficients[1]
a2 = coefficients[2]

print("\na0 =", a0)
print("a1 =", a1)
print("a2 =", a2)


# -------------------------------------------------
# 6. Create the interpolation polynomial
# -------------------------------------------------

def P(x):
    return a0 + a1 * x + a2 * x**2


# -------------------------------------------------
# 7. Verify that the polynomial passes
#    through all original points
# -------------------------------------------------

print("\nVerification:")

for x, y_real in zip(x_points, y_points):
    y_predicted = P(x)

    print(
        "x =", x,
        "| expected y =", y_real,
        "| P(x) =", y_predicted
    )


# -------------------------------------------------
# 8. Interpolate a new value
# -------------------------------------------------

x_new = 1.5

y_new = P(x_new)

print("\nInterpolation:")
print("P(", x_new, ") =", y_new)