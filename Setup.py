from setuptools import setup, find_packages

setup(
    name                = 'fbknockknock',
    version             = '0.2',
    description         = 'fbknockknock',
    author              = 'smlee',
    author_email        = 'cap1232@gmail.com',
    url                 = 'https://github.com/ZIZUN/fbknockknock',
    download_url        = 'https://github.com/ZIZUN/fbknockknock/archive/0.0.tar.gz',
    install_requires = ['fbchat', ],
    packages            = find_packages(exclude = []),
    keywords            = ['fbknockknock'],
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)