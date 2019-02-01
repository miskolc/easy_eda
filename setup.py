from setuptools import setup

setup(
    name='easy_eda',
    version='0.1.2',
    description='Exploratory Data Analysis',
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