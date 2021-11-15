#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib as mp
import math as m

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3,2.5,64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0
def functionaDeriver(x):
    return m.e**-(x**2)

def integratoin(n,d,f,c=0):
    demisaxe = (n*d)/2
    points = np.linspace(-demisaxe+c,demisaxe+c,n)
    somme = 0
    for p in points:
        somme += f(p)
    somme *= d
    return(somme)

def integrationLim(a,b,f,d):
    c = (a+b)/2
    n = abs(round((b-a)/d))
    return integratoin(n,d,f,c)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(integratoin(10000,0.001,functionaDeriver))
    print(integrationLim(-5,5,functionaDeriver,0.1))
    pass
