import numpy as np
from .wavelet_transform import WaveletTransform


class WaveletTransformHaar(WaveletTransform):
    def _get_matrix_filter(self, size):
        matrix_filter = np.zeros((size, size), dtype=np.int8)

        j = 0
        numbers = [1, 1]
        for i in range(size):
            if i == size / 2:
                j = 0
                numbers[1] = -1

            matrix_filter[i][j] = numbers[0]
            matrix_filter[i][j+1] = numbers[1]

            j += 2

        return matrix_filter

    def _calc_decomposition(self, matrix_filter, values):
        return np.dot(matrix_filter, values) / np.sqrt(2)