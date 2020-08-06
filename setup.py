import setuptools

# TODO: actually use this to make this project available in pip

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="password-validator-weiyanli-chen",
    version="0.0.1",
    author="York Chen",
    author_email="york.chen.hz@hotmail.com",
    description="a CLI tool to validate your password",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cwyl02/password_validator",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: TODO",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
