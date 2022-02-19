import random
from re import T
import matplotlib.pyplot as plt
import numpy as np


def IFS(iter, matrices, probs):
    print(matrices)
    print(probs)
    punto = np.matrix([1.0,1.0,1.0]).T
    for i in range (iter):
        #descartamos las primeras iteraciones
        if(i > 40):
            rand = random.uniform(0.0, 1.0)
    
            for n in range(matrices.__len__()):
                if(rand <= probs[n]):
                    punto = (matrices[n] @ punto)
                    
                    break
            
            #x.append(int(map(punto[0], 0.0, 1.0, -1920/2, 1920/2)))
            #print(x)
            #y.append(int(map(punto[1], 0.0, 1.0, -1080/2, 1080/2)))

            x.append(punto[0])
            y.append(punto[1])
        pass



######################SIERPINSKY##########################
x = []
y = []


sierMat1 = np.matrix ([[0.5, 0, -1], 
                     [0.0, 0.5, 1], 
                     [0,    0,   1]])

sierMat2 = np.matrix ([[0.5, 0, 1], 
                     [0.0, 0.5, 1], 
                     [0,    0,   1]])

sierMat3 = np.matrix ([[0.5, 0, 0], 
                     [0.0, 0.5, -1], 
                     [0,    0,   1]])

sierMats = [sierMat1, sierMat2, sierMat3]
sierDets =  [np.abs(np.linalg.det(sierMat1)), np.abs(np.linalg.det(sierMat2)), np.abs(np.linalg.det(sierMat3))]

sierProbs=[0,0,0]
sumDets = np.sum(sierDets)

for i in range (sierDets.__len__()):
        
    if (i > 0):
        
        sierProbs[i] = (sierDets[i] / sumDets) + sierProbs[i - 1]
     
    else: 
        sierProbs[i] = (sierDets[i] / sumDets)
    
      
print(sierProbs)
print(np.sum(sierProbs))

IFS(50000, sierMats, sierProbs)

plt.scatter(x,y,s = 1, edgecolor='blue')

plt.show()        




#######################FERN########################
x = []
y = []


fernMat1 = np.matrix ([[0.81, -0.04, 0.12], 
                     [0.07, 0.84, 0.195], 
                     [0,    0,    1]])

fernMat2 = np.matrix ([[0.18, 0.27, 0.12], 
                        [-0.25, 0.23, 0.02], 
                        [0,    0,     1]])

fernMat3 = np.matrix ([[0.19, 0.238, 0.16], 
                       [0.275, -0.14, 0.16], 
                       [0,0,1]])

fernMat4 = np.matrix ([[0.0235,0.045, 0.11], 
                       [0.087,0.1666,0], 
                       [0,0,1]])

fernMats = [fernMat1, fernMat2, fernMat3, fernMat4]

fernDets = [np.abs(np.linalg.det(fernMat1)), np.abs(np.linalg.det(fernMat2)), np.abs(np.linalg.det(fernMat3)), np.abs(np.linalg.det(fernMat4))]


sumDets = np.sum(fernDets)
print(sumDets)

fernProbs = [0,0,0,0]

for i in range (fernDets.__len__()):
        
    if (i > 0):
        
        fernProbs[i] = (fernDets[i] / sumDets) + fernProbs[i - 1]
     
    else: 
        fernProbs[i] = (fernDets[i] / sumDets)
    
      
print(fernProbs)
print(np.sum(fernProbs))

IFS(99999, fernMats, fernProbs)

plt.scatter(x,y,s = 1, edgecolor='green')

plt.show()        

