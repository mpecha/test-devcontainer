import numpy as np


def main() -> None:
    np_array1: np.ndarray = np.array([1, 2, 3])
    np_array2: np.ndarray = 2 * np_array1
    np_array3: np.ndarray = np_array1 + np_array2

    print(np_array3)


if __name__ == '__main__':
    main()
