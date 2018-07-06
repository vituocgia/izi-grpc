import os
import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')
_root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_root, 'izi_grpc/__init__.py')) as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read()).group(1)))

with open(os.path.join(_root, 'requirements.txt')) as f:
    requirements = f.readlines()

with open(os.path.join(_root, 'README.md')) as f:
    readme = f.read()


def find_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return filepaths


setup(
    name='izi_grpc',
    version=version,
    description='iZi gRPC framework',
    long_description=readme,
    url='https://github.com/vituocgia/izi-grpc',
    author='DiepDT',
    author_email='dotiendiep@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['rpc', 'grpc'],
    packages=find_packages(exclude=['tests']),
    package_data={'izi_grpc': find_package_data('izi_grpc')},
    python_requires='>=3',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'izi_grpc=izi_grpc.cli:main'
        ],
        'izi_grpc.jobs': [
            'celery=izi_grpc.contrib.extensions.celery.cmd:main',
        ]
    }
)
