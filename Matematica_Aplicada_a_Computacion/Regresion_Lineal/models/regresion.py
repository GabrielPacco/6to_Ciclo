import numpy as np
import matplotlib.pyplot as plt


def estimate_b0_b1(x, y):
    """ Calculo de la ecuación
    Estimación de constante y pendiente de la regresión lineal
    """
    n = np.size(x)

    # Obtenemos el promedio de X y de Y
    m_x, m_y = np.mean(x), np.mean(y)

    # Calcular sumatoria de XY y mi sumatoria de XX
    sumatoria_xy = np.sum([x - m_x] * (y - m_y))
    sumatoria_xx = np.sum(x * (x - m_x))

    # Coeficientes de regresión
    b_1 = sumatoria_xy / sumatoria_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


# Funcion de graficado
def plot_regression(x, y, b):
    """ Calculo de la ecuación
    Gráficado de las regresiones
    """
    # Color verde, marcador de puntos de grosor 30
    plt.scatter(x, y, color="g", marker="o", s=30)
    y_pred = b[0] + b[1] * x
    plt.plot(x,y_pred, color="b")

    # Etiqueta
    plt.xlabel('x-Independiente')
    plt.ylabel('y-Dependiente')

    plt.show()