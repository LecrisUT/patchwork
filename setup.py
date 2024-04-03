# -*- coding: utf-8 -*-

"""
setup.py implementation, interesting because it parsed the first __init__.py and
    extracts the `__author__` and `__version__`
"""

import sys
from ast import parse
from os import path

from setuptools import setup

if sys.version_info[:2] > (3, 7):
    from ast import Constant
else:
    if sys.version_info[0] == 2:
        from itertools import imap as map

    from ast import expr

    # Constant. Will never be used in Python =< 3.8
    Constant = type("Constant", (expr,), {})


package_name = "patchwork"

with open(
    path.join(path.dirname(__file__), "README{extsep}rst".format(extsep=path.extsep)),
    "rt",
) as fh:
    long_description = fh.read()


def main():
    """Main function for setup.py; this actually does the installation"""
    with open(
        path.join(
            path.abspath(path.dirname(__file__)),
            "src",
            "patchwork",
            "_version{extsep}py".format(extsep=path.extsep),
        )
    ) as f:
        parsed_init = parse(f.read())

    __version__ = ".".join(
        map(
            lambda node: str(node.value if isinstance(node, Constant) else node.n),
            parsed_init.body[0].value.elts,
        )
    )

    setup(
        name=package_name,
        author="Jeff Forcier",
        author_email="jeff@bitprophet.org",
        version=__version__,
        url="https://www.fabfile.org",
        description=long_description[: long_description.find("\n")],
        long_description=long_description,
        long_description_content_type="text/x-rst",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: BSD License",
            "Operating System :: POSIX",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Topic :: Software Development",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Software Distribution",
            "Topic :: System :: Systems Administration",
        ],
        license="BSD-2-Clause",
        license_files=["LICENSE"],
        install_requires=["fabric>=2.2"],
        test_suite="tests",
        packages=[package_name],
        package_dir={package_name: path.join("src", package_name)},
    )


def setup_py_main():
    """Calls main if `__name__ == '__main__'`"""
    if __name__ == "__main__":
        main()


setup_py_main()
