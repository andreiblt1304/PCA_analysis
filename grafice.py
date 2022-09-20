import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd


def corelagrama(matrice=None, dec=2, titlu='Corelograma', valMin=-1, valMax=1):
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrice, dec), cmap='bwr', vmin=valMin, vmax=valMax, annot=True)


def cerculCorelatiilor(matrice=None, k1=0, k2=1, raza=1, dec=2, valMin=-1, valMax=1,
        etichetaX=None, etichetaY=None, titlu='Cercul corelatiilor'):
    plt.figure(titlu, figsize=(8, 8))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    T = [t for t in np.arange(0, np.pi*2, 0.01)]
    X = [np.cos(t)*raza for t in T]
    Y = [np.sin(t)*raza for t in T]
    plt.plot(X, Y)
    plt.axvline(x=0, color='g')
    plt.axhline(y=0, color='g')
    if etichetaX==None or etichetaY==None:
        if isinstance(matrice, pd.DataFrame):
            plt.xlabel(xlabel=matrice.columns[k1], fontsize=12, color='k', verticalalignment='top')
            plt.ylabel(ylabel=matrice.columns[k2], fontsize=12, color='k', verticalalignment='bottom')
        else:
            plt.xlabel(xlabel='Var '+str(k1+1), fontsize=12, color='k', verticalalignment='top')
            plt.ylabel(ylabel='Var '+str(k2+1), fontsize=12, color='k', verticalalignment='bottom')
    else:
        plt.xlabel(xlabel=etichetaX, fontsize=12, color='k', verticalalignment='top')
        plt.ylabel(ylabel=etichetaY, fontsize=12, color='k', verticalalignment='bottom')

    if isinstance(matrice, np.ndarray):
        plt.scatter(x=matrice[:, k1], y=matrice[:, k2], c='r', vmin=valMin, vmax=valMax)
        # putem face o rotunjire la o zecimala dorita pentru intrega matrice de corelatie
        matrice_rotunjita = np.round(matrice, dec)
        for i in range(matrice.shape[0]):
            # plt.text(x=0.25, y=0.25, s='exemplu de text')
            plt.text(x=matrice[i, k1], y=matrice[i, k2], s='(' +
                     str(matrice_rotunjita[i, k1]) + ', ' + str(matrice_rotunjita[i, k2]) + ')')

    if isinstance(matrice, pd.DataFrame):
        # plt.text(x=0.25, y=0.25, s='avem un pandas.DataFrame')
        plt.scatter(x=matrice.iloc[:, k1], y=matrice.iloc[:, k2], c='r', vmin=valMin, vmax=valMax)
        # for i in range(len(matrice.index)):
        for i in range(matrice.values.shape[0]):
            # plt.text(x=0.25, y=0.25, s='exemplu de text')
            # plt.text(x=matrice.iloc[i, k1], y=matrice.iloc[i, k2], s='(' +
            #          str(np.round(matrice.iloc[i, k1], dec)) + ', ' +
            #         str(np.round(matrice.iloc[i, k2], dec)) + ')')
            plt.text(x=matrice.iloc[i, k1], y=matrice.iloc[i, k2], s=matrice.index[i])


def componentePrincipale(valoriProprii=None, eticheteComp=None,
                         titlu='Varianta explicata de componentele principale',
                         etichetaX='Componente principale', etichetaY='Valori proprii (varianta)'):
    plt.figure(titlu, figsize=(11, 8))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    lungime = 0
    print(type(valoriProprii), valoriProprii)

    if isinstance(valoriProprii, np.ndarray):
        lungime = valoriProprii.shape[0]

    if isinstance(valoriProprii, list):
        lungime = len(valoriProprii)

    componente = ['C' + str(i + 1) for i in range(lungime)]

    plt.axhline(y=1, color='r')
    plt.xlabel(xlabel=etichetaX, fontsize=12, color='k', verticalalignment='top')
    plt.ylabel(ylabel=etichetaY, fontsize=12, color='k', verticalalignment='bottom')
    plt.plot(componente, valoriProprii, 'bo-')


def afisare():
    plt.show()