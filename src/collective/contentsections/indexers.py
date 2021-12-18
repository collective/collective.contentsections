from collective.contentsections.pages import IPage
from collective.contentsections.sections import ICardsSection
from collective.contentsections.sections import ISection
from collective.contentsections.sections import ITextSection
from plone import api
from plone.app.contenttypes.behaviors.richtext import IRichText
from plone.app.contenttypes.indexers import SearchableText
from plone.app.contenttypes.indexers import _unicode_save_string_concat
from plone.indexer.decorator import indexer
from Products.CMFPlone.utils import base_hasattr


def get_title_and_description_terms(obj):
    terms = []
    if not obj.hide_title:
        # Index visible title
        terms.append(obj.title)
    if base_hasattr(obj, "description") and obj.description:
        # Index description
        terms.append(obj.description)
    return terms


def get_elements_title_and_description_terms(section):
    terms = []
    brains = api.content.find(context=section, depth=1, object_provides=ISection)
    for b in brains:
        terms.append(b.Title)
        terms.append(b.Description)

    return terms


@indexer(ISection)
def get_section_searchabletext(section):
    terms = get_title_and_description_terms(section)
    terms.extend(get_elements_title_and_description_terms(section))
    return " ".join(terms)


@indexer(ITextSection)
def get_textsection_searchabletext(section):
    terms = get_title_and_description_terms(section)
    transforms = api.portal.get_tool("portal_transforms")
    text = IRichText(section).text
    raw = text.raw
    plain = transforms.convertTo("text/plain", raw, mimetype=text.mimeType).getData().strip()
    terms.append(plain)
    return " ".join(terms)


@indexer(ICardsSection)
def get_cardssection_searchabletext(section):
    terms = get_title_and_description_terms(section)
    if section.cards:
        for card in section.cards:
            terms.append(card["title"])
            terms.append(card["subtitle"])
            terms.append(card["description"])
    return " ".join(terms)


@indexer(IPage)
def get_page_searchabletext(page):
    """Compute SearchableText of IPage with SearchableText of its ISection"""
    terms = [_unicode_save_string_concat(SearchableText(page))]
    catalog = api.portal.get_tool("portal_catalog")
    brains = api.content.find(context=page, depth=1, object_provides=ISection)
    for brain in brains:
        indexes = catalog.getIndexDataForRID(brain.getRID())
        searchable_terms = indexes.get("SearchableText") or []
        terms.extend(searchable_terms)
    return " ".join(terms)
