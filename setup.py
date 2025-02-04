#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'influxdb-client[ciso]', 'jupyter', 'pandas', 'ipykernel']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Alexander Hasha",
    author_email='ahasha@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A functional example of using iotawatt with InfluxDB",
    entry_points={
        'console_scripts': [
            'iotawatt_influx=iotawatt_influx.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='iotawatt_influx',
    name='iotawatt_influx',
    packages=find_packages(include=['iotawatt_influx', 'iotawatt_influx.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ahasha/iotawatt_influx',
    version='0.1.0',
    zip_safe=False,
)
