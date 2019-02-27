import numpy as np

from zero.api import Adaboost
from zero.datasets.api import load_iris


def main():
    def load_simple_data():
        features = ([
            [1.0, 2.1],
            [2.0, 1.1],
            [1.3, 1.0],
            [1.0, 1.0],
            [2.0, 1.0]
        ])
        labels = [1.0, 1.0, -1.0, -1.0, 1.0]
        return np.array(features), np.array(labels)

    X, y = load_simple_data()
    model = Adaboost(max_iter=5)
    model.fit(X, y)

    y_pred = model.predict(X)

    print(y, y_pred)


if __name__ == "__main__":
    main()
