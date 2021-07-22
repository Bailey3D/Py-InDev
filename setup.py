import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indev",
    version="0.0.1",
    author="Bailey3D",
    author_email="contact@bailey3d.com",
    description="Package containing basic development based stuff",
    long_description=long_description,
    url="https://github.com/BhMbOb/Py-InDev",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)