import setuptools

__project__ = "SysExpose"
__version__ = "0.0.1"
__description__ = "A python module to find system information, such as private/public ip"
__packages__ = ["SysExpose"]
__author__ = "Suraj Apps"
__url__ = "https://github.com/SurajApps/SysExpose"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: System Administrators",
    "Programming Language :: Python :: 3",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: System :: Hardware",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SysExpose-pkg-SurajApps",
    version="1.0",
    author=__author__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=__packages__,
    classifiers=__classifiers__,
    python_requires='>=3.6',
    install_requires=["requests", "psutil"]
)
