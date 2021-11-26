from setuptools import find_packages
from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)
setup(
    name="collective.contentsections",
    version="1.0a1",
    description="An add-on for Plone",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Sébastien Verbois",
    author_email="sebastien.verbois@gmail.be",
    url="https://github.com/collective/collective.contentsections",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.contentsections",
        "Source": "https://github.com/collective/collective.contentsections",
        "Tracker": "https://github.com/collective/collective.contentsections/issues",
        # 'Documentation': 'https://collective.contentsections.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "plone.api",
        "plone.app.dexterity",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
