from setuptools import setup

LONG_DESCRIPTION = """Easy Exploratory Data Analysis

The functionality present in this package simplifies
Exploratory Data Analysis for datasets provided as
pandas DataFrames.
"""

setup(
    name='easy_eda',
    version='0.1.8',
    description='Exploratory Data Analysis',
    long_description=LONG_DESCRIPTION,
    url='http://github.com/miskolc/easy_eda',
    author='Dragos Calin',
    author_email='dragos.calin.gm@mail.com',
    license='MIT',
    packages=['easy_eda'],
    install_requires=[
        'matplotlib >= 2.2.3',
        'numpy >= 1.15.1',
        'pandas >= 0.22.0',
        'seaborn >= 0.9.0',
    ],
    zip_safe=False
)