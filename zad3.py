import math
import random


def readFromFile():  
    with open('transformation.txt') as file:
        for line in file.readlines():
            line = line.replace("\n", "")  # usuwa znaki końca linii
            line = line.replace(" ", "")   # usuwa spacje między liczbami
            tmp = [] 
            for i in range(4):   #można jeszcze zamienić 4 na ilość znaków w lini
                for char in line[i]:
                    tmp.append(float(char))
            dataIn.append(tmp)

def neuron(x, w, bias):     
    suma = 0
    for i in range(len(x)): 
        suma += x[i]*w[i]
    suma += bias
    return suma
    
def layer(x, w, howManyInLayer, bias):       #tablica wyjść dla odpowinich neuronów w wartwie
    tmp = 0
    y = [0]*howManyInLayer
    for i in range(howManyInLayer):
            tmp = neuron(x, w[i], bias[i])          
            y[i] = (sigmoid(tmp))
    return y

def sigmoid(y):              #wyjście y to wyniki funkcji nuron
    return 1/(1 + math.e**(-y))

def changeWeights(w, y, x, numberOfLayer, d ): #zmiana wag dla warstwy
    for i in range(len(w[numberOfLayer])):
            for j in range(len(w[numberOfLayer][i])):
                if( j == len(w[numberOfLayer][i])-1):
                    w[numberOfLayer][i][j] = w[numberOfLayer][i][j] + alfa*(d[numberOfLayer][i])*1*sigmoidDerivative(y[i])
                
                else:
                    w[numberOfLayer][i][j] = w[numberOfLayer][i][j] + alfa*(d[numberOfLayer][i])*(x[j])*sigmoidDerivative(y[i])
    return w

def initaliseWeights(x,w,bias, nOfNeurons):     #1 ok lista wag dla warstwy x- wejscia neuronów dla warstwy
    random.seed()
    result = []
    if(bias == False ):
        for j in range(nOfNeurons):
            for i in range(len(x)):
                w.append(random.random())
            result.append(w)
            w = []
    else: 
        for j in range(nOfNeurons):
            for i in range(len(x)+1):
                w.append(random.random())
            result.append(w)
            w = []            
    return result

def errors(z, y, w, howMuchLayers):         #3 w chyba ok - lista 3 wym, paramterów ze wszystkich warstw
    tmp = 0.0
    d = [[0]*len(y[0]) ,[0]*len(y[1]) ]

    for j in range(len(y[howMuchLayers-1])):
        d[howMuchLayers - 1][j] = z[j] - y[howMuchLayers-1][j]  

    for n in range(len(y[0])):
        for p in range(howMuchLayers-1):
            for i in range(len(y[1])):
                tmp += w[p+1][i][n] * d[p+1][i]
            d[p][n] = tmp
            tmp = 0
    return d   
    
def sigmoidDerivative(z):
    return sigmoid(z) * (1 - sigmoid(z))

def teach(x, bias, z, howManyInLayer2, howManyInLayer3, epochs):
    w1 = []
    w2 = []
    b1 = []
    y = []
    y1 = []
    y2 = []
    b = []
    w = []

    w1 = initaliseWeights(x,w1,bias,howManyInLayer2)
    if(bias == True):
        for i in range(howManyInLayer2):
            b.append(w1[i][len(w1[i])-1])
    else:
        b = [0]*howManyInLayer2
        b1 = [0]*howManyInLayer3
    y1 = layer(x,w1,howManyInLayer2,b)            
    w2 = initaliseWeights(y1,w2,bias,howManyInLayer3)
    if(bias == True):
        for i in range(len(w2)):
                b1.append(w2[i][len(w2[i])-1])
    y2 = layer(y1, w2, howManyInLayer3, b1)
    w.append(w1)
    w.append(w2)
    y.append(y1)
    y.append(y2)
    e = 0     
    e = errors(z,y, w, len(w))
    for i in range(epochs):
        w = changeWeights(w, y2, y1, 1, e)
        w = changeWeights(w, y1, x, 0, e)
        y1 = []
        y1 = layer(x,w[0],howManyInLayer2,b)
        y2 = []
        y2 = layer(y1, w[1], howManyInLayer3, b1)
        y = []
        y.append(y1)
        y.append(y2)
        e = errors(z,y, w, 2)
        if(avgErrorIter(z,y2) < 0.01):
            print('Błąd sieci:', avgErrorIter(z,y2))
            print('Sieć uzyskała błędy niższe od zadanej precyzji, po ', i, 'iteracjach.')
            return y2
    print('Błąd sieci:', avgErrorIter(z,y2))
    print('Sieć nie uzyskała błędów niższych od zadanej precyzji. ')
    return y2
                    
def run(x, bias, z, howManyInLayer2, howManyInLayer3, epochs):
    y = []
    err = []
    for i in range(len(x)):
        y.append(teach(x[i],bias,z[i],howManyInLayer2,howManyInLayer3,epochs))
        err.append(avgErrorIter(z[i],y[i]))
    print('Globalny błąd ', avg(err))
    return y

def avgErrorIter(z, y):
    n = len(y)
    suma = 0
    for i in range(len(z)):
        suma += math.fabs(z[i] - y[i])
    return 1/n * suma

def avg(y):
    suma = 0
    for i in range(len(y)):
        suma += y[i]
    return suma/len(y)


dataIn = []
alfa = 0.01
readFromFile()
y = []
r = []
print('-----------------Transformacja--------------------')
print('Dane wejściowe:', dataIn)
print('Oczekiwne dane wyjściowe:', dataIn)
print("\n")
y = run(dataIn, True, dataIn, 3, 4, 15000) 
print('Wynik sieci: ', y)
print('\n')


print('---------------------Xor-------------------------')

x = [[0,0],
     [0,1],
     [1,0],
     [1,1]]
# 0011 xor 0101 = 0110
z = [[0],[1],[1],[0]]

print('Dane wejściowe:', x)
print('Oczekiwne dane wyjściowe:', z)

r = run(x, True, z, 3, 1, 20000)
print('Wynik sieci: ', r)
