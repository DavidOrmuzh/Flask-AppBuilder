import os
import sys
from setuptools import setup, find_packages

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return open(fpath(fname)).read()


def desc():
    return read('README.rst')

setup(
    name='Flask-AppBuilder',
    version='0.1.35',
    url='https://github.com/dpgaspar/flask-appbuilder/',
    license='BSD',
    author='Daniel Vaz Gaspar',
    author_email='danielvazgaspar@gmail.com',
    description='Simple and rapid Application builder, includes detailed security, auto form generation, google charts and much more.',
    long_description=desc(),
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    scripts=['bin/init_app.py'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'Flask-Babel==0.8',
        'Flask-Login>=0.1.2',
        'Flask-OpenID>=1.1.0',
        'Flask-SQLAlchemy==0.16',
        'Flask-WTF==0.8.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite=''
)
