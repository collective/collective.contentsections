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
    version="1.0.0a22",
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
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
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
        "plone.formwidget.geolocation >= 3.0.5",
        "collective.geolocationbehavior",
        "collective.taxonomy >= 3.0.0",
        "collective.z3cform.datagridfield >= 3.0.0",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
