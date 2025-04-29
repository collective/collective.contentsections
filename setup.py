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
    version="2.0.0a2",
    description="A block approach for Plone 6 Classic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: Distribution",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Sébastien Verbois",
    author_email="sebastien.verbois@gmail.com",
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
    python_requires=">=3.10",
    install_requires=[
        "collective.geolocationbehavior >= 1.7.2",
        "collective.taxonomy >= 3.1.5",
        "collective.z3cform.datagridfield >= 3.0.3",
        "plone.api",
        "plone.distribution",
        "plone.formwidget.geolocation >= 3.0.7",
        "Products.CMFPlone",
        "setuptools",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.contenttypes [test]",
            "Products.CMFPlacefulWorkflow",  # needed for plone.app.testing.layers.PLONE_FIXTURE
            "pytest",
            "pytest-cov",
            "pytest-plone",
            "tox",
        ],
        "dev": [
            "i18ndude",
            "plone.exportimport",
            "plone.meta",
            "zest.releaser",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
