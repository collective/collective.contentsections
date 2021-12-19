collective.contentsections
==========================

This product offers a block approach for Plone 6 Classic based entirely on Dexterity content types.
It is largely based on the code that was developed in the *imio.smartweb.core* product for the Walloon municipalities.

The approach in this product can be seen as a generalisation of the *Full content* view available in Plone on  *Folder* content type.

The plone site is seen as a folder hierarchy that contains pages.
A page is a folderish content type composed of sections.
A section can contain elements of the same type (File, Image, Link). Folders, pages, sections and elements are all Dexterity content types.

The section view view redirects to its position in its parent page view view.
Section content types are hidden from research but their contents are indexed in the *SearchableText* index of their parent page.

Images and files are seen as elements.
Images are only available in images sections and as lead image in all content types.
Files are only available in files sections.
Links are sometimes seen as elements of the links section and sometimes as redirect pages.

Features
--------

This product provides :

- basic schema and class for section content types
- *LeadIcon* vocabulary and behavior based on plone.icons registry records
- *TextSection* wich contains a simplified TinyMCE field and the behavior *LeadImage*. A *TextSection* contains only the lead image. No more image in TinyMCE text field.
- *HTMLSection* to integrate iframe from youtube, google map and other iframe providers. No more video, iframe in TinyMCE text field.
- *CollectionSection* to link a section with a collection.
- *SelectionSection* to link a section to other pages. The *SelectionSection* replace the *Related items* behavior.
- *CardsSection* content type based on a collective.z3cform.datagridfield field to make nice information blocks/links on a page
- *ImagesSection*, *LinksSection*, *FilesSection* folderish section content types to keep the site structured and facilitate the cup and paste of sections between pages.
- A *Page view* for folderish content types
- *BasicPage*, *EventPage* page content types

This product also provides a prototype of *row configuration* for when the editor wants multiple sections on the same row. It is inspired by the *Fieldset separator* concept used in *PloneformGen*. However, this prototype breaks the simplicity of editing and probably requires a refactoring or a switch to Volto :-)

This product fits Plone with:

- top position for *Toolbar position*
- use accordion instead of tabbing for edit forms
- new image sizes
- a new default page name *index*
- LeadImage on *File* and *Link* content types
- a profile to simplify TinyMCE interface

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

    make install
    make start

Demo content
------------

The file https://github.com/sverbois/collective.contentsections/blob/main/demo.json
contains some demo pages that can be loaded into the site using the *@@import_content* view of the *collective.exportimport* product. *collective.exportimport* is installed on the developement environment. You have to hide *Plone Leftcolumn* and *Plone Rightcolumn* portlets on your site to display the pages correctly.

TODO
----

- Tests, Tests, Tests
- Try to use *RelationChoice* in *CardsSection* but problem with *RelationChoice* field in *DataGridField* required a fallback to UUID *StaticCatalogVocabulary*
- A FormSection based on Easyform ?
- A focal point feature behavior activated on LeadImage

Previews
--------

![Preview 1](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview1.png)

![Preview 2](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview2.png)

![Preview 3](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview3.png)
