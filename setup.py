
from setuptools import setup, find_packages

setup(
    name='zendesk_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    package_data={
        'my_package': ['*.json'],
    },
    entry_points={
        'console_scripts': [
            'myapp=my_package.main:main_entry_point',
        ],
    },
)
