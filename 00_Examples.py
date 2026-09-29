# ---
# jupyter:
#   jupytext:
#     notebook_metadata_filter: language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.13.5
# ---

import numpy as np

np.ones((3,5), dtype=np.uint8)

np.random.randint(0,2**8,(3,5), dtype=np.uint8)

tab = np.ones((6))
print(tab)
tab1 = tab.reshape(3,2)
print(tab1)
tab[0] = 2
print('#########')
print(tab)
print(tab1)

# +
# %%timeit
n = 1000000
x = np.linspace(0, 2*np.pi, n)

# la bonne façon
np.sin(x)         # np.sin appliquée au tableau x
# -

import math

# +
# %%timeit
n = 1000000
x = np.linspace(0, 2*np.pi, n)

# la mauvaise façon
for e in x:             # une boucle for sur un tableau numpy
                        # c'est toujours une mauvaise idée
    math.sin(e)
# -

SLICING

from pprint import pprint

import numpy as np
A=np.arange(1,31) * 2
B1, B2 = np.reshape(A,(2,5,3))
print('A :')
print(A)
print('B1 :')
print(B1)
print('B2 :')
print(B2)
print('douze :')
print(B1[1,2])

import numpy as np
A=np.arange(1,31) * 2
B = np.reshape(A,(2,5,3))
print('A :')
print(A)
print('B :')
print(B)
print('douze :')
print(B[0,1,2])

tab = np.arange(120).reshape(2,3,4,5)
out = tab[:,0,1:-1,1:-1]
print(tab)
print('#############')
print(out)

a = np.arange(1,13).reshape(2,2,3)*2
print(a)
print(a.base)
#b = a[::-1,::-1,::-1]
b=np.flip(a)
print(b)
print(b.base)
print()
print(b.base is a)

# # IMAGES

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 2,2
from matplotlib.pyplot import imshow as show

img = np.zeros((91,91,3), dtype=np.uint8)
show(img)

# +

img[:,:,:]=255
show(img)
# -

img[:,:,::2]=0
show(img)

print(img[0,0])
print(img[-1,-1])

img[::10,:]=[0,0,255]
img[:,::10]=[0,0,255]
show(img)

img[::10,:]=[0,0,255]
img[:,::10]=[0,0,255]
show(img)



img = plt.imread("C:\\Users\\Hadrien Bodin\\Documents\\00_Production\\Cours\\Mines_PE\\numerique\\notebooks\\data\\les-mines.jpg")

print(img.flags.writeable)
import copy
img = copy.deepcopy(img)
print(img.flags.writeable)

np.shape(img)

show(img)

print(img.itemsize)
print(img.dtype)
print(img.min())
print(np.max(img))
show(img[:10,:10])

img = plt.imread("C:\\Users\\Hadrien Bodin\\Documents\\00_Production\\Cours\\Mines_PE\\numerique\\notebooks\\data\\les-mines.jpg")
for i in [2,5,10,20]:
    show(img[::i,::i])
    plt.show()

fig, (axes) = plt.subplots(1,4,figsize = (rcParams['figure.figsize'][0]*4, rcParams['figure.figsize'][1]))
for i, value in enumerate([2,5,10,20]):
    axes[i].imshow(img[::value,::value])


def show_window(l,c):
    minx = (img.shape[1]-c)//2
    maxx = minx+c
    miny = (img.shape[0]-l)//2
    maxy=miny+l
    plt.imshow(img[miny:maxy,minx:maxx,:])
    plt.show()
show_window(10,20)
show_window(200,300)

plt.imshow(img[-1:,-1:,:])


# le but est de ne pas utiliser de fct numpy
def unravel_index(index, shape):
    size = 1
    for item in shape:
        size *= item
    coords = []
    
    for dim_size in shape:
        size = size //dim_size
        coords.append(index // size)
        index = index % size
    
    return np.array(coords)



np.ones((3,5), dtype=np.uint8)

np.random.randint(0,256,(3,5), np.uint8)

l = ['un', 'deux', 'trois', 'cinq']
tab = np.array(l)
tab[0] = 'quatre'

tab

tab = np.ones((6))
tab

tab1 = np.reshape(tab, (3,2))
tab1

tab[0]=2
tab1

type(math.sin)

import numpy as np
A=np.arange(1,31) * 2
B = np.reshape(A,(2,5,3))
B

tab = np.arange(30)

tab

tab[::-1]

a = np.arange(1,13).reshape(2,2,3)*2
print(a)
print(a.base)


#b = a[::-1,::-1,::-1]
b=np.flip(a)
print(b)
print(b.base)
print()
print(b.base is a)

lines, cols = np.indices((4, 4))

cols

(cols+1)%2


# +

def block_checkers(n, k):
    Y,X = np.indices((n*k,n*k))
    Yk, Xk = (Y//k)%2, (X//k)%2
    return (((Xk == 0) & (Yk == 1)) | ((Xk == 1) & (Yk == 0))).astype(int)


# -

n=4
k=3
Y,X = np.indices((n*k,n*k))
Yk, Xk = (Y//k)%2, (X//k)%2
(Xk+Yk)%2

import numpy as np
def stairs(n):
    Y,X = np.indices((2*n+1,2*n+1))
    out = (X+Y)*(X<n+1)*(Y<n+1)
    out += (X[:,::-1]+Y[::-1,:])*(X>=n+1)*(Y>=n+1)
    out += (X + Y[::-1,:])*(X<n+1)*(Y>=n+1)
    out += (X[:,::-1] + Y)*(X>=n+1)*(Y<n+1)
    return out
print(stairs(4))

n=3
Y,X = np.indices((2*n+1,2*n+1))
#out = (X+Y)*(X<n+1)*(Y<n+1)
(X+Y)*(X<n+1)*(Y<n+1)
X[:,::-1]

n=4
k=3
Y,X = np.indices((n*k,n*k))

Y

((Y//k) + (X//k))%2

# ## Broadcasting

# +
import numpy as np
mat = np.ones((3,4))

mat + 1

# -

import numpy as np
mat = np.ones((3,4))
mat += np.ones((1,4))
mat

import pandas as pd
pd.options.display.precision = 2

df = pd.read_csv('data/titanic.csv')

df.describe()

df.describe(include='all')

df['Age']

df.head(8)

df = pd.read_csv('data/titanic.csv')
df = df.set_index('PassengerId')
df

df['Name'][552]

df = pd.read_csv('data/titanic.csv')
df.index


df = df.set_index('PassengerId')
df.index
