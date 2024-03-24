VERSION = "0.0.5"
DESCRIPTION = "St. Louis Federal Reserve FRED API"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import os
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt"), "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name = "fredx",
    version = VERSION,
    description = DESCRIPTION,

    long_description = long_description,
    long_description_content_type = "text/markdown",

    keywords = ["fred", "api", "federal reserve", "st. louis fed", "async"],
    author = "Ahmed Thahir",
    author_email = "ahmedthahir2002@gmail.com",
    url = "https://github.com/AhmedThahir/fredx",
    license = "MIT",
    packages = find_packages(),
    install_requires = requirements,
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Natural Language :: English",
    ],
)