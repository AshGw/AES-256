import warnings
import sys

__all__ = ['AshCrypt']
__version__ = "1.1.6"
__author__ = "Ashref Gwader"

if sys.version_info.major <= 3 and sys.version_info.minor <= 11 or sys.version_info.major < 3:
    warnings.warn(
        message='''
            This Python version is no longer supported by the Python team nor is it supported by this Project
            Python 3.7 or newer is required for this library to work properly !
        ''',
        stacklevel = 2
    )