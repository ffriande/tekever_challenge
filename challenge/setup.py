from setuptools import setup

setup(
    name='challenge',
    packages=['challenge'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy'
    ],
)