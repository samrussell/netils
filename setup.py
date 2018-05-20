from setuptools import setup

long_description = """
    A very small collection of functions that are useful for networking in Python

    More information at https://github.com/samrussell/netils
"""

setup(
    name='netils',
    description='Some functions for networking in Python',
    long_description=long_description,
    version='0.0.1',
    url='https://github.com/samrussell/netils',
    author='Sam Russell',
    author_email='sam.h.russell@gmail.com',
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    keywords='routing sdn networking',
    packages=['netils'],
    python_requires='>=3',
    install_requires=[]
)
