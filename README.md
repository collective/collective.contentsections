# collective.contentsections


[![PyPI](https://img.shields.io/pypi/v/collective.contentsections)](https://pypi.org/project/collective.contentsections/)
[![Python Version](https://img.shields.io/pypi/pyversions/collective.contentsections)](https://pypi.org/project/collective.contentsections/)
[![License](https://img.shields.io/pypi/l/collective.contentsections)](https://pypi.org/project/collective.contentsections/)
[![Status](https://img.shields.io/pypi/status/collective.contentsections)](https://pypi.org/project/collective.contentsections/)
[![Stars](https://img.shields.io/github/stars/collective/collective.contentsections?style=social)](https://github.com/collective/collective.contentsections/stargazers)


This product offers a block approach for Plone 6 Classic based entirely on Dexterity content types. It is largely based on the code that was developed in the *imio.smartweb.core* product for the Walloon municipalities.

The approach in this product can be seen as a generalisation of the *Full content* view available in Plone on *Folder* content type.

The Plone site is seen as a folder hierarchy that contains pages. A page is a folderish content type composed of sections. A section can contain elements of the same type (File, Image, Link, Location, Contact). Folders, pages, sections, and elements are all Dexterity content types.

The section view redirects to its position in its parent page view. Section content types are hidden from research, but their contents are indexed in the *SearchableText* index of their parent page.

Images and files are seen as elements. Images are only available in image sections and as the lead image in all content types. Files are only available in file sections. Links are sometimes seen as elements of the links section and sometimes as redirect pages.

Here is a picture of the model.

![Archimate Model](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/model.png)

## Compatibility

- Releases 1.x of collective.contentsections are for Plone 6.0
- Releases 2.x of collective.contentsections are for Plone 6.1

## Features

This product provides:

- Basic schema and class for section content types
- *LeadIcon* vocabulary and behavior based on plone.icons registry records
- *collective.taxonomy.section_css_classes* taxonomy for available section CSS classes
- *TextSection* which contains a simplified TinyMCE field and the behavior *LeadImage*. A *TextSection* contains only the lead image. No more image in TinyMCE text field.
- *HTMLSection* to integrate iframe from YouTube, Google Maps, and other iframe providers. No more video or iframe in TinyMCE text field.
- *CollectionSection* to link a section with a collection.
- *SelectionSection* to link a section to other pages. The *SelectionSection* replaces the *Related items* behavior.
- *CardsSection* content type based on a collective.z3cform.datagridfield field to make nice information blocks/links on a page.
- *ImagesSection*, *LinksSection*, *FilesSection*, *LocationsSection*, *ContactsSection* folderish section content types to keep the site structured and facilitate the cut and paste of sections between pages.
- A *Page view* for folderish content types.
- *BasicPage*, *EventPage*, and *NewsPage* page content types to replace default Plone content types.

This product fits Plone with:

- A new default page name *index*.
- *LeadImage* on *File* and *Link* content types.
- A profile to simplify the TinyMCE interface.

## Demo Content

The *collective.contentsections* product adds a *plone.distribution* "Plone Site (Content Sections)" with some demo pages.

## Choices/Beliefs

- We want a KISS solution.
- We want a solution for junior integrators.
- We believe that Plone Classic can be used to create beautiful sites in less than a day.

## Possibilities

- If you activate workflow on sections, you can restrict access to certain sections of a page.
- As sections are Dexterity content types, you can create a collection/faceted navigation of sections.

## Dependencies

This product depends on the following products: *collective.taxonomy*, *collective.z3cform.datagridfield*, *collective.geolocationbehavior*

## Installation

Install collective.contentsections by adding it to your buildout:

```ini
[buildout]
...

eggs =
    collective.contentsections
```

and then run `bin/buildout`.

## Development

###  Prerequisites

[uv](https://docs.astral.sh/uv/) 

See [installation guide](https://docs.astral.sh/uv/getting-started/installation/) )

### Environment initialization

```bash
git clone git@github.com:collective/collective.contentsections.git
cd collective.contentsections
make install
make start
```

## Tests

Tests are located inside `tests` folder. They can be run with tox.

```bash
make test
make coverage
make lint
```

## Internationalization

This product has been translated into:

- English
- French

To add a new language, you need a "PO file" inside the `locales` folder.

For example, to add German locales:

```bash
mkdir -p src/collective/collective.contentsections/locales/de/LC_MESSAGES
touch src/collective/collective.contentsections/locales/de/LC_MESSAGES/collective.contentsections.po
```

After that, you can update the file with:

```bash
make i18n
```

You will need to change `Language-Code` and `Language-Name` directives in the file.

## Credits

Most ideas developed in this product come from people who worked at iMio on the imio.smartweb product family during the year 2021. This team was composed of:

- Christophe BOULANGER
- Elisabeth DONNAY
- Thomas LAMBERT
- Laurent LASUDRY
- Olivier SNICKERS
- Sébastien VERBOIS

## Previews

![Preview 1](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview1.png)

![Preview 2](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview2.png)

![Preview 3](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview3.png)

![Preview 4](https://raw.githubusercontent.com/sverbois/collective.contentsections/main/docs/images/preview4.png)