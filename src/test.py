import numpy as np


def main() -> None:
    np_array1: np.ndarray = np.array([1, 2, 3])
    np_array2: np.ndarray = 2 * np_array1
    print(np_array2)


if __name__ == '__main__':
    main()
