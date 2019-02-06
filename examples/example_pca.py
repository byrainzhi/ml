import os
import sys

import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from ml.principal_component_analysis import principal_component_analysis
from ml.math_tools import mt


def main():
    df = pd.read_csv("data/iris.csv")

    X = df.iloc[:, :-1].values
    X = mt.normalize(np.array(X))

    y = df.iloc[:, -1]
    y = y.replace(to_replace=['setosa', 'virginica',
                              'versicolor'], value=[0, 1, 2])
    y = y.values

    pca = principal_component_analysis.PCA()
    pca.plot_pca(X, y, 'example_pca.png')


if __name__ == "__main__":
    main()
