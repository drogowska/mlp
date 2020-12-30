import math

dataIn = []
hidden = []
layer = []

def readFromFile():  
    with open('transformation.txt') as file:
        for line in file.readlines():
            line = line.replace("\n", "")  # usuwa znaki końca linii
            line = line.replace(" ", "")   # usuwa spacje między liczbami
            tmp = [] 
            for i in range(4):   #można jeszcze zamienić 4 na ilość znaków w lini
                for char in line[i]:
                    tmp.append(int(char))
            dataIn.append(tmp)

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
print(dataIn)
