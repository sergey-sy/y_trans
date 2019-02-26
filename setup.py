import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="y_trans",
    version="0.0.1b",
    author="sergey-sy",
    author_email="maiyashik@gmail.com",
    description="Machine translation with Yandex.Translate API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sergey-sy/y_trans",
    download_url="https://github.com/sergey-sy/y_trans/archive/v0.0.1b.tar.gz",
    keywords=["yandex", "yandex translate", "yandex translator", "translator"],
    scripts=["bin/y_trans"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
