import numpy as np
from .binary_power import *


class VectorTransformation:
  @staticmethod
  def pad_vector_with_zeros(data):
    new_size = BinaryPower.next_power_of_two(data.size)
    data = np.pad(data, pad_width=(0, new_size - data.size), mode='constant')

    return data