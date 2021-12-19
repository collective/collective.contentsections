from setuptools import find_packages
from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)
setup(
    name="collective.contentsections",
    version="1.0.0a4",
    description="A block approach for Plone 6 Classic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Sébastien Verbois",
    author_email="sebastien.verbois@gmail.be",
    url="https://github.com/sverbois/collective.contentsections",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.contentsections",
        "Source": "https://github.com/sverbois/collective.contentsections",
        "Tracker": "https://github.com/sverbois/collective.contentsections/issues",
        # 'Documentation': 'https://collective.contentsections.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages(where="src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "plone.api",
        "plone.app.dexterity",
        "collective.z3cform.datagridfield",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
