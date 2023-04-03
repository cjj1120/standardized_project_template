"""Python setup.py for standardized_project_template package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("standardized_project_template", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="standardized_project_template",
    version=read("standardized_project_template", "VERSION"),
    description="Awesome standardized_project_template created by cjj1120",
    url="https://github.com/cjj1120/standardized_project_template/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="cjj1120",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["standardized_project_template = standardized_project_template.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
