==================
BCJ-cffi ChangeLog
==================

All notable changes to this project will be documented in this file.

`Unreleased`_
=============

Added
-----

Changed
-------

Fixed
-----

Deprecated
----------

Removed
-------

Security
--------

`v0.5.3`_
=========

Fixed
-----
* Dependency error for PyPy3 build.
   * Dependency for CFFI 0.15.0 for CPython and 0.14.6 for PyPy3

`v0.5.2`_
=========

Added
-----
* Provide wheels for python 3.10

Changed
-------
* Consolidate tox.ini config to pyproject.toml
* Exclude .github files from source distribution
* CFFI dependency for 0.15.0

`v0.5.1`_
=========

Added
-----
* Release 32bit, MacOS Arm binaries.

Changed
-------
* Improve release CI/CD script.
* Make C header code diet by dropping unused part.


`v0.5.0`_
=========

* Change _*_code() functions to *_code() to expose

`v0.4.0`_
=========

* Add type hint stub.
* Add test configurations.

`v0.3.1`_
=========

* Add ARMT, ARM, SPARC, PPC, IA64 codes.


`v0.3.0`_
=========

* Add x86 BCJFilter class.


.. History links
.. _Unreleased: https://github.com/miurahr/py7zr/compare/v0.5.3...HEAD
.. _v0.5.3: https://github.com/miurahr/py7zr/compare/v0.5.2...v0.5.3
.. _v0.5.2: https://github.com/miurahr/py7zr/compare/v0.5.1...v0.5.2
.. _v0.5.1: https://github.com/miurahr/py7zr/compare/v0.5.0...v0.5.1
.. _v0.5.0: https://github.com/miurahr/py7zr/compare/v0.4.0...v0.5.0
.. _v0.4.0: https://github.com/miurahr/py7zr/compare/v0.3.1...v0.4.0
.. _v0.3.1: https://github.com/miurahr/py7zr/compare/v0.3.0...v0.3.1
.. _v0.3.0: https://github.com/miurahr/py7zr/compare/v0.1.0...v0.3.0
