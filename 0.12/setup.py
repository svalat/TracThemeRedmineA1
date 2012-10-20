#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'RedmineA1Theme',
    version = '1.0',
    packages = [ 'redmineA1theme' ],
    package_data = { 'redmineA1theme': [ 'htdocs/*.css', 'htdocs/*.png', 'htdocs/*.jpg', 'htdocs/*.gif', 'templates/*.html' ] },
    author = 'Sebastien Valat',
    author_email = 'sebastien.valat@gmail.com',
    description = 'Trac adaptation of A1 theme from redmine',
    license = 'GPLv2',
    keywords = 'trac plugin theme',
    url = 'http://',
    classifiers = [
        'Framework :: Trac',
    ],
    install_requires = [ 'Trac', 'TracThemeEngine>=2.0' ],

    entry_points = {
        'trac.plugins': [
            'redmineA1theme.theme = redmineA1theme.theme',
        ]
    },
)

