from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
from typing import Tuple


def divide_datos(
    xdata: np.array, y: np.array
) -> Tuple[np.array, np.array, np.array, np.array]:
    """Toma un conjunto de datos `xdata` y sus etiquetas `y` y regresa
    un nuevo conjunto de datos dividido en etrenamiento y prueba.
    
    Arguments:
        xdata {np.array} -- Conjunto de datos
        y {np.array} -- Etiquetas del conjunto de datos
    
    Returns:
        Tuple[np.array, np.array, np.array, np.array] -- Conjunto de datos para entrenamiento, sus etiquetas y prueba con sus respectivas etiquetas.
    """
    xtrain, xtest, ytrain, ytest = train_test_split(xdata, y, test_size=0.2)

    return xtrain, xtest, ytrain, ytest


def ajuste_y_predice(
    xtrain: np.array, ytrain: np.array, xtest: np.array, ytest: np.array
) -> float:
    """Toma conjuntos de datos de prueba y entrenamiento, con sus respectivas etiquetas y realiza una regresión mediante el método de Boosting Trees
    
    Arguments:
        xtrain {np.array} -- Datos de entrenamiento
        ytrain {np.array} -- Etiquetas de entrenamiento
        xtest {np.array} -- Datos de prueba
        ytest {np.array} -- Etiquetas de prueba
    
    Returns:
        float -- Error cuadrático medio sobre el conjunto de prueba
    """
    params = {
        "n_estimators": 500,
        "max_depth": 4,
        "min_samples_split": 2,
        "learning_rate": 0.01,
        "loss": "ls",
    }
    clf = GradientBoostingRegressor(**params)

    clf.fit(xtrain, ytrain)
    mse = mean_squared_error(ytest, clf.predict(xtest))

    return mse


if __name__ == "__main__":
    boston = load_boston()
    x_data, y = boston.data, boston.target

    xtrain, xtest, ytrain, ytest = divide_datos(x_data, y)
    resultado = ajuste_y_predice(xtrain, ytrain, xtest, ytest)
    print(f"MSE del ajuste: {resultado}")
