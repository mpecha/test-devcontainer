import numpy as np
import matplotlib.pyplot as plt


def plot(x: np.ndarray, y: np.ndarray) -> None:
    plt.plot(x, y)
    plt.show()


def main() -> None:
    np_array1: np.ndarray = np.array([1, 2, 3])
    np_array2: np.ndarray = 2 * np_array1

    np_array3: np.ndarray = np_array1 + np_array2
    np_array4: np.ndarray = 4 * np_array3
    print(np_array4)

    plot(x=np_array2, y=np_array3)


if __name__ == '__main__':
    main()
