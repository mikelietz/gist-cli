import codecs
try:
    from setuptools import setup, find_packages
    extra_setup = dict(
        zip_safe=True,
        install_requires = ['argparse'],
        )
except ImportError:
    from distutils.core import setup
    extra_setup = {}

setup(
    name='gist-cli',
    version='0.1',
    author='Mike Leitz, Issac Kelly',
    url='http://github.com/mikelietz/gist-cli',
    description='Create Github Gist from files or stdin',
    package_dir={'': '.'},
    py_modules=['gist_cli'],
    long_description=codecs.open("README.md", "r", "utf-8").read(),
    entry_points={
        'console_scripts': [
            'mkgist=gist_cli:main'
            ]
        },
    **extra_setup
)