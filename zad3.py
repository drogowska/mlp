import math

tab = []

def toInt(a, b, c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)


def readFromFile():
    i = 0
    with open('transformation.txt') as file:
        for line in file.readlines():
            a,b,c,d = line.strip().split(",")
            toInt(a,b,c,d)
            tab.append([a, b, c, d])
            i+=1


def neuron(x, w):
    suma = 0
    for i in range(len(w)):
        suma += x[i]*w[i]
    return suma
    
def actFunction(x):
    return 1/(1+math.e**(-1*x))

readFromFile()
print(tab)