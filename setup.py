# setup.py for pySerial
#
# Windows installer:
#   "python setup.py bdist_wininst"
#
# Direct install (all systems):
#   "python setup.py install"
#
# For Python 3.x use the corresponding Python executable,
# e.g. "python3 setup.py ..."

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# importing version does not work with Python 3 as files have not yet been
# converted.
import serial
version = serial.VERSION

setup(
    name = "pyserial",
    description = "Python Serial Port Extension",
    version = version,
    author = "Chris Liechti",
    author_email = "cliechti@gmx.net",
    url = "https://github.com/pyserial/pyserial",
    packages = ['serial', 'serial.tools', 'serial.urlhandler'],
    license = "Python",
    long_description = "Python Serial Port Extension for Win32, Linux, BSD, Jython, IronPython",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals :: Serial',
    ],
    platforms = 'any',
    scripts = ['serial/tools/miniterm.py'],
)
