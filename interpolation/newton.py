



# n = len(x_points)


# coefficients = y_points.copy()



# for j in range(1, n):
#     for i in range(n - 1, j - 1, -1):

#         coefficients[i] = (
#             coefficients[i] - coefficients[i - 1]
#         ) / (
#             x_points[i] - x_points[i - j]
#         )


# print("Newton coefficients:")
# print(coefficients)


x_points = [0, 1, 2,3]
y_points = [1, 9, 9,28]


def divided_difference(x_points, y_points):
    n = len(x_points)
    coefficients = y_points.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (
                coefficients[i] - coefficients[i - 1]
            ) / (
                x_points[i] - x_points[i - j]
            )

    return coefficients
  













# # ---------------------------------------------
# # 2. Newton interpolation function
# # ---------------------------------------------

# def newton_interpolation(x):

#     result = coefficients[0]
#     product = 1

#     for i in range(1, n):

#         product *= (x - x_points[i - 1])

#         result += coefficients[i] * product

#     return result


# # ---------------------------------------------
# # 3. Verification
# # ---------------------------------------------

# print("\nVerification:")

# for x, y_real in zip(x_points, y_points):

#     y_predicted = newton_interpolation(x)

#     print(
#         "x =", x,
#         "| expected y =", y_real,
#         "| P(x) =", y_predicted
#     )


# # ---------------------------------------------
# # 4. Interpolate a new point
# # ---------------------------------------------

# x_new = 1.5

# y_new = newton_interpolation(x_new)

# print("\nInterpolation:")
# print("P(", x_new, ") =", y_new)

coefficients = divided_difference(x_points, y_points)


def format_number(value):
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return str(value)


polynomial = format_number(coefficients[0])
for i in range(1, len(coefficients)):
    coefficient = coefficients[i]
    product = "x"
    for j in range(1, i):
        product += f"(x - {x_points[j]})"

    if coefficient >= 0:
        polynomial += f" + {format_number(coefficient)}{product}"
    else:
        polynomial += f" - {format_number(abs(coefficient))}{product}"

print(f"P(x) = {polynomial}")