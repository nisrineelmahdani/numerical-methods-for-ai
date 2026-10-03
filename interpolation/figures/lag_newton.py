import numpy as np
import matplotlib.pyplot as plt
import os




def f1(x):
    return x * np.exp(-x**2)


def f2(x):
    return np.log(x + 3)




def lagrange_interpolation(x_nodes, y_nodes, x):

    n = len(x_nodes)

    P = np.zeros_like(x, dtype=float)

    for k in range(n):

        Lk = np.ones_like(x, dtype=float)

        for j in range(n):

            if j != k:

                Lk *= (
                    (x - x_nodes[j])
                    /
                    (x_nodes[k] - x_nodes[j])
                )

        P += y_nodes[k] * Lk

    return P


def divided_differences(x_nodes, y_nodes):

    n = len(x_nodes)

    coefficients = y_nodes.astype(float).copy()

    for j in range(1, n):

        coefficients[j:n] = (
            coefficients[j:n]
            - coefficients[j - 1:n - 1]
        ) / (
            x_nodes[j:n]
            - x_nodes[0:n - j]
        )

    return coefficients



def newton_interpolation(x_nodes, coefficients, x):

    n = len(coefficients)

    P = np.ones_like(x) * coefficients[-1]

    for k in range(n - 2, -1, -1):

        P = (
            coefficients[k]
            +
            (x - x_nodes[k]) * P
        )

    return P



def plot_interpolation(function, function_name, number_of_points):

    # Interval
    a = -2
    b = 2

    # Dense x values for smooth curves
    x = np.linspace(a, b, 1000)

    # Original function
    y = function(x)



    x_nodes = np.linspace(
        a,
        b,
        number_of_points
    )

    y_nodes = function(x_nodes)



    P_lagrange = lagrange_interpolation(
        x_nodes,
        y_nodes,
        x
    )


    
    coefficients = divided_differences(
        x_nodes,
        y_nodes
    )

    P_newton = newton_interpolation(
        x_nodes,
        coefficients,
        x
    )


    

    error = np.max(
        np.abs(y - P_lagrange)
    )


    # Graph

    plt.figure(figsize=(9, 6))

    plt.plot(
        x,
        y,
        label="Original function",
        linewidth=2.5
    )

    plt.plot(
        x,
        P_lagrange,
        "--",
        label="Lagrange"
    )

    plt.plot(
        x,
        P_newton,
        ":",
        label="Newton"
    )

    plt.scatter(
        x_nodes,
        y_nodes,
        label="Interpolation points",
        zorder=5
    )

    plt.title(
        f"{function_name} - {number_of_points} interpolation points"
    )

    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()


    # Save graph

    os.makedirs(
        "figures",
        exist_ok=True
    )

    filename = (
        f"figures/{function_name}_"
        f"{number_of_points}_points.png"
    )

    plt.savefig(
        filename,
        dpi=300
    )

    plt.show()


    

    print(
        f"\n{function_name}"
    )

    print(
        f"Number of points: {number_of_points}"
    )

    print(
        "Interpolation nodes:",
        x_nodes
    )

    print(
        "Newton coefficients:",
        coefficients
    )

    print(
        f"Maximum error: {error:.8f}"
    )

    print(
        "-" * 50
    )



numbers_of_points = [
    3,
    5,
    7
]



for n in numbers_of_points:

    plot_interpolation(
        f1,
        "f1",
        n
    )


for n in numbers_of_points:

    plot_interpolation(
        f2,
        "f2",
        n
    )