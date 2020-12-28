import math

tab = []
hidden = []
layer = []

def readFromFile():  #czyta jako stringa
    i = 0
    with open('transformation.txt') as file:
        for line in file.readlines():
            a, b, c, d = line.strip().split(",")
            tab.append([a, b, c, d])
            i+=1

def neuron(x, w):
    suma = 0
    for i in range(len(w)):
        suma += x[i]*w[i]
    return suma
    
def actFunction(y):              #wyjście y to wyniki funkcji nuron
    return 1/(1+math.e**(-1*y))

def changeW(w, x): #zmiana wag
     for i in range(len(x)):
        w[i] = w[i] - 2*alfa*(x[i]* d[i])
     return w

def f(z, y, howMuchLayers):
    for p in range(howMuchLayers):
        for j in range(len(y)):
            d[p][j] = z[j] - y[j]


def pochodna(z):
    return actFunction(z) * (1 - actFunction(z))

alfa = 0.1
d =[]
readFromFile()
print(tab)
