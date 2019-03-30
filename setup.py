import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="djangoless-signing",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="Same Django signing API but without Django",
    long_description=README,
    author="Fatih Kılıç",
    author_email="m.fatihklc0@gmail.com",
    url="https://github.com/FKLC/djangoless-signing",
    download_url="https://pypi.org/project/djangoless-signing/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
