#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Manuel Guenther <manuel.guenther@idiap.ch>
# Tue Jun 24 09:32:21 CEST 2014

bob_packages = ['bob.core', 'bob.io.base', 'bob.sp']

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.blitz'] + bob_packages))
from bob.blitz.extension import Extension, Library, build_ext

version = '2.0.0a1'

setup(

    name='bob.ip.gabor',
    version=version,
    description='C++ code and Python bindings for Bob\'s Gabor wavelet analysis tools',
    url='http://github.com/bioidiap/bob.ip.gabor',
    license='BSD',
    author='Manuel Guenther',
    author_email='manuel.guenther@idiap.ch',

    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
      'setuptools',
      'matplotlib',
      'bob.blitz',
      'bob.core',
      'bob.io.base',
      'bob.sp',
      'bob.io.image',
      'bob.ip.color',
    ],

    namespace_packages=[
      "bob",
      "bob.ip",
    ],

    ext_modules = [
      Extension("bob.ip.gabor.version",
        [
          "bob/ip/gabor/version.cpp",
        ],
        version = version,
        bob_packages = bob_packages,
      ),

      Library("bob.ip.gabor.bob_ip_gabor",
        [
          "bob/ip/gabor/cpp/Wavelet.cpp",
          "bob/ip/gabor/cpp/Transform.cpp",
          "bob/ip/gabor/cpp/Jet.cpp",
          "bob/ip/gabor/cpp/Graph.cpp",
          "bob/ip/gabor/cpp/Similarity.cpp",
        ],
        version = version,
        bob_packages = bob_packages,
      ),

      Extension("bob.ip.gabor._library",
        [
          "bob/ip/gabor/wavelet.cpp",
          "bob/ip/gabor/transform.cpp",
          "bob/ip/gabor/jet.cpp",
          "bob/ip/gabor/graph.cpp",
          "bob/ip/gabor/similarity.cpp",
          "bob/ip/gabor/main.cpp",
        ],
        bob_packages = bob_packages,
        version = version,
      ),
    ],

    cmdclass = {
      'build_ext': build_ext
    },

    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],

)
