==========================
collective.contentsections
==========================

This product offers a block approach for Plone 6 Classic based entirely on Dexterity content types.
It is largely based on the code that was developed in the *imio.smartweb.core* product for the Walloon municipalities.

The plone site is seen as a folder hierarchy that contains pages. A page is composed of sections.
A section can contain elements of the same type. Folders, pages, sections and elements are all Dexterity content types.

Images and files are seen as elements. Images are only available in images sections and as lead image in all content types.
Files are only available in files sections.
Links are sometimes seen as elements of the links section and sometimes as redirect pages.

Features
--------

This product provides :

- Basic schema and class for section content types
- *LeadIcon* vocabulary and behavior based on plone.icons registry records
- *HTMLSection*, *TextSection*, *CollectionSection* content types
- *CardsSection* content type based on a collective.z3cform.datagridfield field
- *ImagesSection*, *LinksSection*, *FilesSection* folderish section content types
- A *Page view* for folderish content types
- *BasicPage*, *EventPage* page content types

This product fits Plone with:

- new image sizes
- a new default page name *index*

Installation
------------

Install collective.contentsections by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.contentsections


and then running ``bin/buildout``

