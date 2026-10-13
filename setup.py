#!/usr/bin/env python
from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='phonesec',
    version='1.0.0',
    author='AndiSec',
    description='Phone Number OSINT Tool - Comprehensive phone number analysis and intelligence gathering',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AndiSec/phonesec',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    install_requires=[
        'phonenumbers>=8.13.0',
        'requests>=2.31.0',
        'colorama>=0.4.6',
        'tabulate>=0.9.0',
        'pytz>=2024.1',
    ],
    entry_points={
        'console_scripts': [
            'phonesec=phonesec:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords='osint phone-number phone intelligence security reconnaissance pentesting',
)
