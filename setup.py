from setuptools import setup

with open('./README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='linq-t',
    version='0.1',
    keywords='Linq, type hinting, type inference',
    long_description=readme,
    packages=['linq', 'linq.core', 'linq.standard'],
    package_data={
        'linq':[
            'core/*.pyi',
    ]},
    url='https://github.com/Xython/Linq.py',
    license='MIT',
    author='thautwarm',
    author_email='twshere@outlook.com',
    description='Language Integrated Query for Python',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'],
    zip_safe=False
)
