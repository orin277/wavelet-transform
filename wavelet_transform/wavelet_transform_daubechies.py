import numpy as np
from .wavelet_transform import WaveletTransform


class WaveletTransformDaubechies(WaveletTransform):
    def _get_matrix_filter(self, size):
        matrix_filter = np.zeros((size, size), dtype=np.float32)

        j = 0
        numbers = [1 + np.sqrt(3), 3 + np.sqrt(3), 3 - np.sqrt(3), 1 - np.sqrt(3)]
        for i in range(size):
            if i == size / 2:
                j = 0
                numbers = [-(1 - np.sqrt(3)), 3 - np.sqrt(3), -(3 + np.sqrt(3)), 1 + np.sqrt(3)]

            for k in range(len(numbers)):
                matrix_filter[i][(j+k) % matrix_filter.shape[1]] = numbers[k]

            j += 2

        return matrix_filter

    def _calc_decomposition(self, matrix_filter, values):
        return np.dot(matrix_filter, values) / (4 * np.sqrt(2))