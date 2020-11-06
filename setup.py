import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="komeilparseh", # Replace with your own username
    version="0.75",
    author="Komeil Parseh",
    author_email="parsehkp@gmail.com",
    description="password maker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KomeilParseh/Password-Maker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)