from setuptools import setup

with open('./README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='Linq',
    version='0.2',
    keywords='Linq',
    long_description=readme,
    packages=['linq', 'linq.core', 'linq.standard'],
    url='https://github.com/thautwarm/Linq.py/',
    license='MIT',
    author='thautwarm',
    author_email='twshere@outlook.com',
    description='Language Integrated Query for Python',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'],
    zip_safe=False
)
