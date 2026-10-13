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



img = plt.imread("adresse de l'imag")

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

img = plt.imread("adresse de l'image")
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

# # PANDAS

import pandas as pd
pd.options.display.precision = 2

df = pd.read_csv('data/titanic.csv')

df

df.describe()

df.describe(include='all')

df.columns

df['Age']

df.head(8)

df = pd.read_csv('data/titanic.csv')
df = df.set_index('PassengerId')
df

df['Name']

df['Name'][552]

df = pd.read_csv('data/titanic.csv')
df.index


df = df.set_index('PassengerId')
df.index

# # EXO

df = pd.read_csv('data/petit-titanic.csv')
df.head(2)

df = pd.read_csv('data/petit-titanic.csv', sep=';')
df.head(2)

df = pd.read_csv('data/petit-titanic.csv', sep=';', header=None)
df.head(2)

df_ref = pd.read_csv('data/titanic.csv')
print(df_ref.columns)
df = pd.read_csv('data/petit-titanic.csv', sep=';', names=df_ref.columns)
df.head(2)

columns = ['Identifiant', 'Survécu', 'Pclass',
           'Nom', 'Genre', 'Age', 'SibSp', 'Parch',
           'Ticket', 'Tarif', 'Cabine', 'Embarquement']
df.columns = columns
df.head(2)

# # MASQUES

df = pd.read_csv('data/titanic.csv')
df[df['Age']<12]

df = pd.read_csv('data/titanic.csv')
girls = (df['Age'] < 12) & (df['Sex'] == 'female')
girls

df = pd.read_csv('data/titanic.csv')
girls = (df['Age'] < 12) & (df['Sex'] == 'female')
girls.sum()

df[girls]

df = pd.read_csv('data/titanic.csv')
girls = (df['Age'] < 12) & (df['Sex'] == 'female')
girls.sum()

df[girls]

children = df['Age'] < 12
children.value_counts()

df['Name'].value_counts()

(~children).sum()

df['Age'].isna()

df['Age'].isna().sum()

df.isna().sum()

df.isna().sum(axis=1)

# # Exo Agregation

df.isna().sum().sum()

import numpy as np
np.sum(df.isna().to_numpy())
df.isna().to_numpy().sum()

# # Exo type colonnes

import pandas as pd
df = pd.read_csv('data/titanic.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Embarked']
for col in cols:
    print(col)
    print(df[col].unique())

dft=df[cols]
dft.dtypes

# # Exo stats

import pandas as pd
df = pd.read_csv('data/titanic.csv')

df.isna().sum().sum()

print(len(df.Pclass.unique()))
print(df.Pclass.value_counts())

df.Sex.value_counts()/len(df)

df.Sex.value_counts(normalize=True)

rate = ((df['Age'] >= 20) & (df['Age'] <= 40)).sum()/len(df)
print(rate)

df.Survived.describe()

(df.Survived == 1).mean()

for id_class in [1,2,3]:
    print(f"class_{id_class}")
    for sex in ['male', 'female']:
        print(sex)
        print(((df['Sex']==sex) & (df['Pclass']==id_class) & (df['Survived']==1)).sum() /
             ((df['Sex']==sex) & (df['Pclass']==id_class)).sum())

# # Copie

df = pd.read_csv('data/titanic.csv', index_col='PassengerId')
df2 = df.copy()
df2.loc[552, 'Age'] = 100
df2.head(1)

df.head(1)

# # Ajoute colonne

df['Deceased'] = 1 - df['Survived']
df.head(3)

df = pd.read_csv('data/titanic.csv')#, index_col='PassengerId')
df = df.set_index('PassengerId')
print(df.loc[552, 'Name'])
print(df.iloc[0, 2])

# # Sélection multiple

# comme avec un tableau numpy,
# si on ne précise pas les colonnes
# on les obtient toutes
df.loc[552]

# on peut passer des listes à loc/iloc
# pour sélectionner explicitement
# plusieurs lignes / colonnesa
df.loc[[552, 832]]

df.loc[[552, 832], ['Name', 'Pclass']]

# à nouveau pour les indices de colonnes
# la colonne d'index ne compte pas
df.iloc[[0, -1], [2, 1]]

# +
# pour sélectionner plusieurs colonnes
# le plus simple c'est quand même cette forme
df[['Name', 'Pclass']]

df[(df['Pclass'] != 1) & (df['Age']>=70)]
# -

# mais bien sûr on peut aussi faire
df.loc[:, ['Name', 'Pclass']]
df[df['Sex']=='female']

df.loc[552, 'Name'] = 'test'
df

# # Exo passageres femmes 1ere classe

# +
# le code
df = pd.read_csv('data/titanic.csv', index_col='PassengerId')

df_survived = (df['Survived'] == 1)
print(   df_survived.sum()/len(df)   )

( ((df['Sex'] == 'female') & (df['Survived'] == 1) & (df['Pclass'] == 1)).sum()
  /((df['Sex'] == 'female') & (df['Pclass'] == 1)).sum()   )
# -

# # group by

import pandas as pd
df = pd.read_csv('data/titanic.csv', index_col='PassengerId')
by_sex = df.groupby(by='Sex')
by_sex

by_sex_class = df.groupby(by=['Sex', 'Pclass'])

by_sex_class.size().index

pd.cut(df['Age'], bins=[0, 12, 19, 55, 100])

df = pd.read_csv('data/titanic.csv', index_col='PassengerId')
df['Age-class'] = pd.cut(
    df['Age'],
    bins=[0, 12, 19, 55, 100],
    labels=['child', ' young', 'adult', '55+'])
df.head()

df.groupby(['Age-class', 'Pclass'])['Survived'].mean()

