from .wavelet_transform import WaveletTransform
from .wavelet_transform_haar import WaveletTransformHaar
from .wavelet_transform_daubechies import WaveletTransformDaubechies

__all__ = ['WaveletTransform', 
    'WaveletTransformHaar', 
    'WaveletTransformDaubechies',
    ]

def __version__():
    return "0.0.1"

def describe():
    description = (
        "Library for wavelet transform, in particular can be used for data approximation\n"
        "Version: {}\n"
    ).format(__version__())
    print(description)
