from setuptools import setup, find_packages

setup(
    name                = 'fbknockknock',
    version             = '0.1',
    description         = 'fbknockknock',
    author              = 'smlee',
    author_email        = 'cap1232@gmail.com',
    url                 = 'https://github.com/ZIZUN/fbknockknock',
    download_url        = 'https://github.com/ZIZUN/fbknockknock/archive/0.0.tar.gz',
    install_requires=[
        'ko',
    ],
    packages            = find_packages(exclude = []),
    keywords            = ['fbknockknock'],
    python_requires     = 'fbchat',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3.8.3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)