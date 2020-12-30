import math
import random

dataIn = []
hidden = []
alfa = 0.01
d =[]

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
    
def layer(x, w, howManyInLayer):
    y = []
    for i in range(howManyInLayer):
        y[i] = neuron(x, w[i])
        y[i] = actFunction(y[i])
    return y


def actFunction(y):              #wyjście y to wyniki funkcji nuron
    return 1/(1+math.e**(-1*y))

def changeWeight(w, x, numberOfWag): #zmiana wag
     suma = 0
     if not w:
        random.seed()
        w = [0] * numberOfWag
        for i in range(1,numberOfWag):
            w[i] = random.random()
     for i in range(len(x)):
        suma += x[i]* d[i]
        w[i] = w[i] - 2*alfa*(suma)
     return w

def errors(z, y, w, howMuchLayers):
    tmp = 0.0
    for p in range(howMuchLayers):
        for j in range(len(y)):
            if(p == howMuchLayers - 1): #ostatnia warstwa
                d[p][j] = y[j] - z[j]
            for i in range(len(d[p+1])):
                tmp += w[i] * d[p+1][i] #propagacja wsteczna
            d[p][j] = tmp
    return d
        

def pochodna(z):
    return actFunction(z) * (1 - actFunction(z))


readFromFile()
print(dataIn)
