name = "vector3d"
v = "1.0.0"
author = "Cyrmax"
email = "bkm.grotschool@yandex.ru"
description = "Vector3D is a small package for processing 3D vector in decartian system and some vector-related function, such as distance between two points, angle between vectors, ETC"
url = "https://github.com/kirill-belousov/vector3d"

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=v,
    author=author,
    author_email=email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)