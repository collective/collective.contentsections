collective.contentsections
==========================

This product offers a block approach for Plone 6 Classic based entirely on Dexterity content types.
It is largely based on the code that was developed in the *imio.smartweb.core* product for the Walloon municipalities.

The approach in this product can be seen as a generalisation of the *Full content* view available in Plone on *Folder* content type.

The plone site is seen as a folder hierarchy that contains pages.
A page is a folderish content type composed of sections.
A section can contain elements of the same type (File, Image, Link, Location, Contact). Folders, pages, sections and elements are all Dexterity content types.

The section view view redirects to its position in its parent page view view.
Section content types are hidden from research but their contents are indexed in the *SearchableText* index of their parent page.

Images and files are seen as elements.
Images are only available in images sections and as lead image in all content types.
Files are only available in files sections.
Links are sometimes seen as elements of the links section and sometimes as redirect pages.

Here is a picture of the model.

![Archimate Model](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/model.png)

Features
--------

This product provides :

- basic schema and class for section content types
- *LeadIcon* vocabulary and behavior based on plone.icons registry records
- *collective.taxonomy.section_css_classes* taxonomy for available Section CSS Classes
- *TextSection* wich contains a simplified TinyMCE field and the behavior *LeadImage*. A *TextSection* contains only the lead image. No more image in TinyMCE text field.
- *HTMLSection* to integrate iframe from youtube, google map and other iframe providers. No more video, iframe in TinyMCE text field.
- *CollectionSection* to link a section with a collection.
- *SelectionSection* to link a section to other pages. The *SelectionSection* replace the *Related items* behavior.
- *CardsSection* content type based on a collective.z3cform.datagridfield field to make nice information blocks/links on a page
- *ImagesSection*, *LinksSection*, *FilesSection*, *LocationsSection*, *ContactsSection* folderish section content types to keep the site structured and facilitate the cut and paste of sections between pages.
- A *Page view* for folderish content types
- *BasicPage*, *EventPage* and *NewsPage* page content types to replace default Plone content types.

This product fits Plone with:

- a new default page name *index*
- LeadImage on *File* and *Link* content types
- a profile to simplify TinyMCE interface

Demo content
------------

The file https://github.com/sverbois/collective.contentsections/blob/main/demo.json
contains some demo pages that can be loaded into the site using the *@@import_content* view of the *collective.exportimport* product. *collective.exportimport* is installed on the developement environment. You have to hide *Plone Leftcolumn* and *Plone Rightcolumn* portlets on your site to display the pages correctly.

Choices/Beliefs
---------------

- We want a KISS solution.
- We want a solution for junior integrators.
- We believe that Plone Classic can be used to create beautiful sites in less than a day.

Possibilities
-------------

- If you activate workflow on sections, you can restrict access to certain sections of a page.
- As section are Dexterity content types, you can create a collection/faceted navigation of sections.

Dependencies
------------

This product depends on the following products: *collective.taxonomy*, *collective.z3cform.datagridfield*, *collective.geolocationbehavior*

Installation
------------

Install collective.contentsections by adding it to your buildout:

    [buildout]

    ...

    eggs =
        collective.contentsections


and then running ``bin/buildout``

Development
-----------

    git clone https://github.com/collective/collective.contentsections.git
    cd collective.contentsections
    make install
    make start

Credits
-------

Most ideas developed in this product come from people who worked at iMio on the imio.smartweb product family during the year 2021. This team was composed of:

- Christophe BOULANGER
- Elisabeth DONNAY
- Thomas LAMBERT
- Laurent LASUDRY
- Olivier SNICKERS
- Sébastien VERBOIS

Previews
--------

![Preview 1](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview1.png)

![Preview 2](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview2.png)

![Preview 3](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview3.png)

![Preview 4](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview4.png)

