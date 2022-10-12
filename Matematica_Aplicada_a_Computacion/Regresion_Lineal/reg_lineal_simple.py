from tkinter import *
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import PolynomialFeatures
from pandas import DataFrame
import scipy.stats
from scipy import stats


def solutionS():
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    a = list(map(float, E1.get().split()))
    b = list(map(float, E2.get().split()))
    x = np.array(a).reshape((-1, 1))
    y = np.array(b)
    # Multiplicacion de X*X guardada en lista3
    for i in range(len(x)):
        lista3.append(x[i] * x[i])
    lix = np.array(lista3)
    # Multiplicacion de Y*Y guardada en lista4
    for i in range(len(y)):
        lista4.append(y[i] * y[i])
    liy = np.array(lista4)
    # Multiplicacion de X*Y guardada en lista4
    for i in range(len(x)):
        lista5.append(x[i] * y[i])
    lixy = np.array(lista5)
    # Calculo de medias
    xmean = x.mean()
    ymean = y.mean()
    # Calculo de sumas
    sum1 = x.sum()
    sum2 = y.sum()
    sum3 = lix.sum()
    sum4 = liy.sum()
    sum5 = lixy.sum()
    per = float(len(x))
    # Calculo de SSxx y SSxy y ssyy
    ssxx = (sum3 - (math.pow(sum1, 2) / per))
    ssyy = (sum4 - (math.pow(sum2, 2) / per))
    ssxy = (sum5 - (sum1 * sum2 / per))
    # Calculo de b0 y b1
    b1 = (ssxy / ssxx)
    b0 = (ymean - (b1 * xmean))
    # Calculo de ygorrito
    for i in range(len(x)):
        lista6.append((b0 + (b1 * a[i])))
    # Calculo de SSE
    for i in range(len(x)):
        lista7.append(math.pow(b[i] - lista6[i], 2))
    lisse = np.array(lista7)
    # suma de SSE
    sum6 = lisse.sum()
    # Calculo de sb0, sb1, tb0 y tb1
    # Paso 1
    var1 = per - 2
    pas1 = (sum6 / var1)
    # Paso 2
    pas2 = (1 / per + (math.pow(xmean, 2) / ssxx))
    sb0 = math.sqrt(pas1 * pas2)
    sb1 = math.sqrt(sum6 / (var1 * ssxx))
    tb0 = b0 / sb0
    tb1 = b1 / sb1
    # Calculo de S, S^2 y R
    s2 = sum6 / var1
    s = math.sqrt(s2)
    r = (ssxy / (math.sqrt(ssxx * ssyy)))
    model = LinearRegression().fit(x, y)
    listboxF.insert(0, "El modelo de regresion es: " + str(round(b0, 3)) + " + " + str(round(b1, 3)) + "x")
    listboxF.insert(0, "r: " + " " + str(round(r, 3)))
    listboxF.insert(0, "s2: " + " " + str(round(s2, 3)))
    listboxF.insert(0, "s: " + " " + str(round(s, 3)))
    listboxF.insert(0, "tb1: " + " " + str(round(tb1, 3)))
    listboxF.insert(0, "tb0: " + " " + str(round(tb0, 3)))
    listboxF.insert(0, "sb1: " + " " + str(round(sb1, 3)))
    listboxF.insert(0, "sb0: " + " " + str(round(sb0, 3)))
    listboxF.insert(0, "b1: " + " " + str(round(b1, 3)))
    listboxF.insert(0, "b0: " + " " + str(round(b0, 3)))
    E1.config(state=DISABLED)
    E2.config(state=DISABLED)
    listboxF.config(state=DISABLED)
    y_pred = model.predict(x)
    plt.scatter(x, y)
    plt.plot(x, y_pred, color='red')
    plt.title("Regresion Linear Simple")
    plt.show()


def solutionM():
    lista1M = []
    lista2M = []
    lista3M = []
    lista4M = []
    lista5M = []
    lista6M = []
    a = list(map(float, E3.get().split()))
    b = list(map(float, E4.get().split()))
    x = np.array(a)
    y = np.array(b)
    x1 = np.column_stack((x, y))
    # Calculo de x^2
    for i in range(len(y)):
        lista1M.append(x[i] * x[i])
    lixM = np.array(lista1M)
    # Calculo de x^3
    for i in range(len(y)):
        lista2M.append(x[i] * x[i] * x[i])
    lix2M = np.array(lista2M)
    # Calculo de x^4
    for i in range(len(y)):
        lista3M.append(x[i] * x[i] * x[i] * x[i])
    lix3M = np.array(lista3M)
    # Calculo de xy
    for i in range(len(y)):
        lista4M.append(x[i] * y[i])
    lixyM = np.array(lista4M)
    # Calculo de x^2y
    for i in range(len(y)):
        lista5M.append(x[i] * x[i] * y[i])
    lix2yM = np.array(lista5M)
    # Sumas
    sum1M = x.sum()
    sum2M = y.sum()
    sum3M = lixM.sum()
    sum4M = lix2M.sum()
    sum5M = lix3M.sum()
    sum6M = lixyM.sum()
    sum7M = lix2yM.sum()

    # Metodo crammer
    def sarrus(A):
        val = ((A[0][0] * A[1][1] * A[2][2]) +
               (A[0][1] * A[1][2] * A[2][0]) +
               (A[0][2] * A[1][0] * A[2][1])) - \
              ((A[2][0] * A[1][1] * A[0][2]) +
               (A[2][1] * A[1][2] * A[0][0]) +
               (A[2][2] * A[1][0] * A[0][1]))
        return val

    sismat = [[0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0]]
    res = [0.0, 0.0, 0.0]
    sismat[0][0] = len(y)
    sismat[0][1] = sum1M
    sismat[0][2] = sum3M
    sismat[0][3] = sum2M

    sismat[1][0] = sum1M
    sismat[1][1] = sum3M
    sismat[1][2] = sum4M
    sismat[1][3] = sum6M

    sismat[2][0] = sum3M
    sismat[2][1] = sum4M
    sismat[2][2] = sum5M
    sismat[2][3] = sum7M

    mat_x = [[sismat[0][3], sismat[0][1], sismat[0][2]],
             [sismat[1][3], sismat[1][1], sismat[1][2]],
             [sismat[2][3], sismat[2][1], sismat[2][2]]]
    mat_y = [[sismat[0][0], sismat[0][3], sismat[0][2]],
             [sismat[1][0], sismat[1][3], sismat[1][2]],
             [sismat[2][0], sismat[2][3], sismat[2][2]]]
    mat_z = [[sismat[0][0], sismat[0][1], sismat[0][3]],
             [sismat[1][0], sismat[1][1], sismat[1][3]],
             [sismat[2][0], sismat[2][1], sismat[2][3]]]
    det_mat = sarrus(sismat)
    if det_mat == 0:
        listboxM.insert(0, "Determinante de A nulo...")
    else:
        det_matx = sarrus(mat_x)
        det_maty = sarrus(mat_y)
        det_matz = sarrus(mat_z)
        res[0] = det_matx / det_mat
        res[1] = det_maty / det_mat
        res[2] = det_matz / det_mat
        listboxM.insert(0, "P => " + " " + str(res))
    A = res[0]
    b1 = res[1]
    b2 = res[2]
    ##Calculo de ygorrito
    for i in range(len(y)):
        lista6M.append((b2 * lixM[i]) + (b1 * x[i]) + A)
    liygorr = np.array(lista6M)
    pf = PolynomialFeatures(degree=2)
    X = pf.fit_transform(x.reshape(-1, 1))
    regresion_lineal = LinearRegression()
    regresion_lineal.fit(X, y)
    r2 = regresion_lineal.score(X, y)
    listboxM.insert(0, "El modelo de regresion es: " + str(round(b2, 3)) + "x^2" + " + " + str(
        round(b1, 3)) + "x" + " + " + str(
        round(A, 3)))
    listboxM.insert(0, "r2: " + " " + str(round(r2, 3)))
    listboxM.insert(0, "liygorr: " + " " + str(liygorr))
    matri = []
    for i in range(len(b)):
        matri.append([b[i], liygorr[i], abs(round(b[i] - liygorr[i], 3))])
    data = DataFrame(matri, columns=['y', 'ygorr', 'diff'])
    listboxM.insert(0, data)
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(x.reshape(-1, 1))
    lin_reg2 = LinearRegression()
    lin_reg2.fit(X_poly, y.reshape(-1, 1))
    y_pred = lin_reg2.predict(X_poly)
    plt.scatter(x, y, color='red')
    plt.plot(x, y_pred)
    plt.title("Regresion Linear Cuadratica")
    plt.show()


def solutionX():
    lista2X = []
    lista3X = []
    lista4X = []
    lista5X = []
    lista6X = []
    lista7X = []
    lista8X = []
    lista9X = []
    lista10X = []
    lista11X = []
    a = list(map(float, E5.get().split()))
    b = list(map(float, E6.get().split()))
    c = list(map(float, E7.get().split()))
    x = np.array(a)  # x2
    y = np.array(b)  # x1
    z = np.array(c)  # y
    k = 2
    # Multiplicacion de X1*X1 guardada en lista3
    for i in range(len(x)):
        lista2X.append(x[i] * x[i])
    lix1X = np.array(lista2X)
    # Multiplicacion de X2*X2 guardada en lista3
    for i in range(len(x)):
        lista3X.append(y[i] * y[i])
    lix2X = np.array(lista3X)
    # Multiplicacion de X1*X2 guardada en lista3
    for i in range(len(x)):
        lista4X.append(a[i] * y[i])
    lix1x2X = np.array(lista4X)
    # Multiplicacion de X1*Y guardada en lista3
    for i in range(len(x)):
        lista5X.append(a[i] * z[i])
    lix1yX = np.array(lista5X)
    # Multiplicacion de X2*Y guardada en lista3
    for i in range(len(x)):
        lista6X.append(y[i] * z[i])
    lix2yX = np.array(lista6X)
    # Multiplicacion de Y*Y guardada en lista3
    for i in range(len(x)):
        lista7X.append(z[i] * z[i])
    liyyX = np.array(lista7X)
    # Calculo de sumas
    sum1X = x.sum()
    sum2X = y.sum()
    sum3X = z.sum()
    sum4X = lix1X.sum()
    sum5X = lix2X.sum()
    sum6X = lix1x2X.sum()
    sum7X = lix1yX.sum()
    sum8X = lix2yX.sum()
    sum9X = liyyX.sum()

    ##Regla de cramer
    def sarrus(A):
        val = ((A[0][0] * A[1][1] * A[2][2]) +
               (A[0][1] * A[1][2] * A[2][0]) +
               (A[0][2] * A[1][0] * A[2][1])) - \
              ((A[2][0] * A[1][1] * A[0][2]) +
               (A[2][1] * A[1][2] * A[0][0]) +
               (A[2][2] * A[1][0] * A[0][1]))
        return val

    sismat = [[0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 0.0]]
    res = [0.0, 0.0, 0.0]
    sismat[0][0] = len(x)
    sismat[0][1] = sum1X
    sismat[0][2] = sum2X
    sismat[0][3] = sum3X
    sismat[1][0] = sum1X
    sismat[1][1] = sum4X
    sismat[1][2] = sum6X
    sismat[1][3] = sum7X
    sismat[2][0] = sum2X
    sismat[2][1] = sum6X
    sismat[2][2] = sum5X
    sismat[2][3] = sum8X
    mat_x = [[sismat[0][3], sismat[0][1], sismat[0][2]],
             [sismat[1][3], sismat[1][1], sismat[1][2]],
             [sismat[2][3], sismat[2][1], sismat[2][2]]]
    mat_y = [[sismat[0][0], sismat[0][3], sismat[0][2]],
             [sismat[1][0], sismat[1][3], sismat[1][2]],
             [sismat[2][0], sismat[2][3], sismat[2][2]]]
    mat_z = [[sismat[0][0], sismat[0][1], sismat[0][3]],
             [sismat[1][0], sismat[1][1], sismat[1][3]],
             [sismat[2][0], sismat[2][1], sismat[2][3]]]
    det_mat = sarrus(sismat)
    if det_mat == 0:
        listboxX.insert(0, "Determinante de A nulo...")
    else:
        det_matx = sarrus(mat_x)
        det_maty = sarrus(mat_y)
        det_matz = sarrus(mat_z)
        res[0] = det_matx / det_mat
        res[1] = det_maty / det_mat
        res[2] = det_matz / det_mat
        listboxX.insert(0, "P => " + str(res))
    A = res[0]
    b1 = res[1]
    b2 = res[2]
    listboxX.insert(0, "El modelo de regresion es: " + str(round(A, 3)) + " + " + str(round(b1, 3)) + "x1",
                    " + " + str(round(b2, 3)) + "x2")
    # Calculo de ygorrito
    for i in range(len(x)):
        lista8X.append((A + (b1 * x[i]) + (b2 * y[i])))
    liygorrX = np.array(lista8X)
    sum10X = liygorrX.sum()
    # Calculo de SSE
    for i in range(len(x)):
        lista9X.append(math.pow((z[i] - liygorrX[i]), 2))
    liysseX = np.array(lista9X)
    sum11X = liysseX.sum()
    prom = z.mean()
    # Calculo de variacion total
    for i in range(len(x)):
        lista10X.append(math.pow(z[i] - prom, 2))
    livartX = np.array(lista10X)
    # Calculo de variacion Explicada
    for i in range(len(x)):
        lista11X.append(math.pow(lista8X[i] - prom, 2))
    livarexX = np.array(lista11X)
    sum12X = livarexX.sum()
    # Calculo de variacion inexplicada
    livarinX = liysseX
    sum13X = sum11X
    # Calculo de S^2 y S
    s2 = (sum11X / (len(z) - (k + 1)))
    s = math.sqrt(s2)
    # Calculo de Variacion total, r^2, r
    vartotal = sum12X + sum11X
    r2 = sum12X / vartotal
    r = math.sqrt(r2)
    # R ajustada
    var1 = k / (len(x) - 1)
    var2 = ((len(x) - 1) / (len(x) - (k + 1)))
    rajustado = (r2 - var1) * var2
    # Calculo de valores f
    f1 = (sum12X / k)
    f2 = (sum13X / (len(x) - (k + 1)))
    fmodelo = (f1 / f2)

    q = scipy.stats.f.ppf(q=1 - 0.05, dfn=k, dfd=(len(x) - (k + 1)))
    falpha = round(q, 3)

    listboxX.insert(0, str(round((stats.t.ppf(1 - 0.025, (len(x) - (k + 1)))), 3)))
    listboxX.insert(0, "s2: " + " " + str(round(s2, 3)))
    listboxX.insert(0, "s: " + " " + str(round(s, 3)))
    listboxX.insert(0, "r2: " + " " + str(round(r2, 3)))
    listboxX.insert(0, "r: " + " " + str(round(r, 3)))
    listboxX.insert(0, "rajustado: " + str(round(rajustado, 3)))
    listboxX.insert(0, "fmodelo: " + str(round(fmodelo, 3)))
    listboxX.insert(0, "falpha: " + str(round(falpha, 3)))
    listboxX.insert(0, "fmodelo: " + str(round(fmodelo, 3)))


def create_window():
    global listboxM, E3, E4, E5, E6, E7
    newWindow = Toplevel()
    newWindow.title("Regresion Linear Cuadratico")
    newWindow.config(bg='thistle3')
    newWindow.geometry('{}x{}'.format(775, 675))
    newWindow.resizable(False, False)
    top = Frame(newWindow, bg='thistle3')
    top1 = Frame(newWindow, bg='thistle3')
    mid = Frame(newWindow, bg='thistle3')
    mid1 = Frame(newWindow, bg='thistle3')

    top.pack()
    top1.pack()
    mid.pack(anchor='n', fill=BOTH)
    mid1.pack(anchor='n', fill=BOTH)

    Label4 = Label(top, text="Regresion Linear Cuadratica", bg="thistle3", font=("Helvetica", 18, "bold"))
    Label4.pack(pady=(20, 0))

    btnM = Button(mid, text='Respuesta!', borderwidth=5, command=solutionM, font=("Helvetica", 16))
    btnM.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

    btnM1 = Button(mid, text='CE', borderwidth=5, command=otraM, font=("Helvetica", 16))
    btnM1.pack(pady=(30, 0), side=LEFT, anchor='n')

    Label5 = Label(top1, text="Valores de x: ", bg="thistle3", font=("Helvetica", 16, "bold"))
    Label5.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

    E3 = Entry(top1, font=("Helvetica", 14), width=50)
    E3.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

    Label6 = Label(top1, text="Valores de y: ", bg="thistle3", font=("Helvetica", 16, "bold"))
    Label6.pack(padx=(0, 10), anchor='sw')

    E4 = Entry(top1, font=("Helvetica", 14), width=50)
    E4.pack(padx=(0, 25), anchor='sw')

    Label6 = Label(mid1, text="Regresion Linear Cuadratica: ", bg="thistle3",
                   font=("Helvetica", 16, "bold"))
    Label6.pack(anchor='n', pady=(25, 0), padx=(20, 0))

    listboxM = Listbox(mid1, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
    listboxM.pack(padx=(18, 5), pady=(0, 25))


def create_window1():
    global listboxX
    newWindow1 = Toplevel()
    newWindow1.geometry('{}x{}'.format(750, 750))
    newWindow1.resizable(False, False)
    newWindow1.config(bg="thistle3")
    newWindow1.title('Regresion Linear Multiple')
    top_frame1 = Frame(newWindow1, bg='thistle3')
    top_frame2 = Frame(newWindow1, bg='thistle3')
    btm_frame1 = Frame(newWindow1, bg='thistle3')
    btm_frame2 = Frame(newWindow1, bg='thistle3')

    top_frame1.pack()
    top_frame2.pack()
    btm_frame1.pack(anchor='n', fill=BOTH)
    btm_frame2.pack(anchor='n', fill=BOTH)

    Label7 = Label(top_frame1, text="Regresion Linear Multiple", bg="thistle3",
                   font=("Helvetica", 18, "bold"))
    Label7.pack(pady=(20, 0))

    btnX = Button(btm_frame1, text='Respuesta!', borderwidth=5, command=solutionX,
                  font=("Helvetica", 16))
    btnX.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

    btnX1 = Button(btm_frame1, text='CE', borderwidth=5, command=otraX, font=("Helvetica", 16))
    btnX1.pack(pady=(30, 0), side=LEFT, anchor='n')

    Label8 = Label(top_frame2, text="Valores de x: ", bg="thistle3", font=("Helvetica", 16, "bold"))
    Label8.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

    E5 = Entry(top_frame2, font=("Helvetica", 14), width=50)
    E5.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

    Label9 = Label(top_frame2, text="Valores de x1: ", bg="thistle3", font=("Helvetica", 16, "bold"))
    Label9.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

    E6 = Entry(top_frame2, font=("Helvetica", 14), width=50)
    E6.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

    Label10 = Label(top_frame2, text="Valores de y: ", bg="thistle3", font=("Helvetica", 16, "bold"))
    Label10.pack(padx=(0, 10), anchor='sw')

    E7 = Entry(top_frame2, font=("Helvetica", 14), width=50)
    E7.pack(padx=(0, 25), anchor='sw')

    Label11 = Label(btm_frame2, text="Regresion Linear Multiple: ", bg="thistle3",
                    font=("Helvetica", 16, "bold"))
    Label11.pack(anchor='n', pady=(25, 0), padx=(20, 0))

    listboxX = Listbox(btm_frame2, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
    listboxX.pack(padx=(18, 5), pady=(0, 25))


def otra():
    E1.config(state=NORMAL)
    E2.config(state=NORMAL)
    listboxF.config(state=NORMAL)
    plt.close()
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    listboxF.delete(0, 'end')


def otraM():
    E3.config(state=NORMAL)
    E4.config(state=NORMAL)
    listboxM.config(state=NORMAL)
    plt.close()
    E3.delete(0, 'end')
    E4.delete(0, 'end')
    listboxM.delete(0, 'end')


def otraX():
    E5.config(state=NORMAL)
    E6.config(state=NORMAL)
    E7.config(state=NORMAL)
    listboxX.config(state=NORMAL)
    plt.close()
    E5.delete(0, 'end')
    E6.delete(0, 'end')
    E7.delete(0, 'end')
    listboxX.delete(0, 'end')


root = Tk()
root.geometry("725x650")
root.resizable(False, False)
root.config(bg="thistle3")
# mainloop
top_frameL = Frame(bg="thistle3", width=425, height=150)
top_frameR = Frame(bg="thistle3", width=425, height=150)

btm_frameR = Frame(bg="thistle3", width=425, height=150)
btm_frameR1 = Frame(bg="thistle3", width=425, height=150)

top_frameL.pack()
top_frameR.pack()
btm_frameR.pack(anchor='n', fill=BOTH)
btm_frameR1.pack(anchor='n', fill=BOTH)

w = Label(top_frameL, text="Regresion Linear Simple", bg="thistle3", font=("Helvetica", 18, "bold"))
w.pack(pady=(20, 0))

btn = Button(btm_frameR, text='Respuesta!', borderwidth=5, command=solutionS,
             font=("Helvetica", 16))
btn.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

btn1 = Button(btm_frameR, text='CE', borderwidth=5, command=otra, font=("Helvetica", 16))
btn1.pack(pady=(30, 0), side=LEFT, anchor='n')

w1 = Label(top_frameR, text="Valores de x: ", bg="thistle3", font=("Helvetica", 16, "bold"))
w1.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

E1 = Entry(top_frameR, font=("Helvetica", 14), width=50)
E1.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

w2 = Label(top_frameR, text="Valores de y: ", bg="thistle3", font=("Helvetica", 16, "bold"))
w2.pack(padx=(0, 10), anchor='sw')

E2 = Entry(top_frameR, font=("Helvetica", 14), width=50)
E2.pack(padx=(0, 25), anchor='sw')

w3 = Label(btm_frameR1, text="Regresion Linear Simple: ", bg="thistle3",
           font=("Helvetica", 16, "bold"))
w3.pack(anchor='n', pady=(25, 0), padx=(20, 0))
listboxF = Listbox(btm_frameR1, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
listboxF.pack(padx=(18, 5), pady=(0, 25))

root.title("Regresion Linear")

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Regresion Linear Cuadratica", command=create_window)
filemenu.add_command(label="Regresion Linear Multiple", command=create_window1)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Programs", menu=filemenu)

mainloop()