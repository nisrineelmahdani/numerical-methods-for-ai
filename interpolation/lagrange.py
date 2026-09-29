x_points = [0, 1, 2]
y_points = [1, 3, 7]

x = 1.5

P = 0

for k in range(len(x_points)):

    Lk = 1

    for j in range(len(x_points)):

        if j != k:
            Lk *= (x - x_points[j]) / (x_points[k] - x_points[j])

    P += y_points[k] * Lk

print("Interpolated value:", P)

print("lagrange interplation polynomial :")