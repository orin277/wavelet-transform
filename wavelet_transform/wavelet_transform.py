import numpy as np
from abc import ABC, abstractmethod
from .binary_power import *
from .vector_transformation import *


class WaveletTransform(ABC):
  def __init__(self, data):
    self.data = data
    self.initital_size = data.size
    self.decompositions = []
    self.__decomposition()

  def __decomposition(self):
    if BinaryPower.is_power_of_two(self.data.size) == False:
      self.data = VectorTransformation.pad_vector_with_zeros(self.data)
    self.data = self.data.T

    for i in range(BinaryPower.get_power_of_two(self.data.size)):
      if len(self.decompositions) == 0:
        matrix_filter = self._get_matrix_filter(self.data.size)
        values = self.data
      else:
        new_size = int(len(self.decompositions[-1]) / 2)
        matrix_filter = self._get_matrix_filter(new_size)
        values = self.decompositions[-1][:new_size]
      self.decompositions.append(self._calc_decomposition(matrix_filter, values))

  def inverse_transform(self, level):
    if level < 0 or level >= len(self.decompositions):
      return

    curr_decomposition = self.decompositions[level]
    while level >= 0:
      matrix_filter = self._get_matrix_filter(self.decompositions[level].size)
      curr_approximation = self._calc_decomposition(matrix_filter.T, curr_decomposition)
      level -= 1

      if level != -1:
        half_length = self.decompositions[level].size // 2
        details = self.decompositions[level][half_length:]

        curr_decomposition = np.concatenate((curr_approximation, details))

    return curr_approximation[:self.initital_size]

  @abstractmethod
  def _get_matrix_filter(self, size):
    pass

  @abstractmethod
  def _calc_decomposition(self, matrix_filter, values):
    pass

  def set_to_zero_details(self, level):
    if level < 0 or level >= len(self.decompositions):
      return

    self.decompositions[level][len(self.decompositions[level]) // 2 :] = 0

  def apply_threshold_filtering_details(self, level, threshold):
    if level < 0 or level >= len(self.decompositions):
      return

    half_length = len(self.decompositions[level]) // 2
    mask = (abs(self.decompositions[level][half_length:]) < threshold)
    self.decompositions[level][half_length:][mask] = 0