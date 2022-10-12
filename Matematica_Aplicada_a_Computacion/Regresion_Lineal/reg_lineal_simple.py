import numpy as np
from models.regresion import estimate_b0_b1, plot_regression


def main():
    #  Dataset
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 6, 5])

    # Obtenemos b1 y b2
    b = estimate_b0_b1(x, y)
    print(f"Los valores b0 = {b[0]}, b1 = {b[1]}")

    # Graficamos nuestra linea de regresion
    plot_regression(x, y, b)


if __name__ == '__main__':
    main()