""" Setup script for local developer install of ``gromp``. """
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='gromp',
    version='0.5.0',
    author='Wilhelm Ågren',
    author_email='wilhelmagren98@gmail.com',
    packages=find_packages(),
    url='https://github.com/willeagren/gromp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI ::Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
    ],
    description='Holistic python wrapper for the public Riot Games developer API.',
    long_description=readme,
)

