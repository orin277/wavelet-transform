from setuptools import setup, find_packages

setup(
    name='Wavelet transform',
    version='0.0.1',
    description='Library for wavelet transform, in particular can be used for data approximation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Orin',
    author_email='bogush.vasyar@gmail.com',
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    license='MIT',
    python_requires='>=3.7',
)