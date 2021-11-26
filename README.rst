==========================
collective.contentsections
==========================

This product offers a block approach for Plone 6 Classic based entirely on Dexterity content types.
It is largely based on the code that was developed in the *imio.smartweb.core* product for the Walloon municipalities.

The plone site is seen as a folder hierarchy that contains pages. A page is composed of sections.
A section can contain elements of the same type. Folders, pages, sections and elements are all Dexterity content types.

Features
--------

It provides :

- Basic schema and class for section content types
- *BasicPage*, *EventPage* page content types
- *HTMLSection*, *TextSection*, *GallerySection* section content types
- *ImageElement*, *LinkElement* element content types


Installation
------------

Install collective.contentsections by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.contentsections


and then running ``bin/buildout``

