from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'flask-samurai',
    version = '0.1',
    packages = ('samurai',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/flask-samurai',
    keywords = 'python security heroku flask web addon provider',
    description = 'Easily create Heroku addons in Flask.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
