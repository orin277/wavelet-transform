import numpy as np


class BinaryPower:
    @staticmethod
    def is_power_of_two(n):
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    @staticmethod
    def next_power_of_two(n):
        if n <= 0:
            return 1
        power = int(np.ceil(np.log2(n)))
        return 2 ** power

    @staticmethod
    def get_power_of_two(n):
        if n <= 0:
            return 1
        power = int(np.ceil(np.log2(n)))
        return power

class VectorTransformation:
    @staticmethod
    def pad_vector_with_zeros(data):
        new_size = BinaryPower.next_power_of_two(data.size)
        data = np.pad(data, pad_width=(0, new_size - data.size), mode='constant')

        return data