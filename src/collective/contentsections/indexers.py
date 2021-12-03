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
        # Index description withould bold
        terms.append(obj.description.replace("**", ""))
    return terms


@indexer(ISection)
def get_section_searchabletext(obj):
    terms = get_title_and_description_terms(obj)
    return " ".join(terms)


@indexer(ITextSection)
def get_textsection_searchabletext(obj):
    terms = get_title_and_description_terms(obj)
    transforms = api.portal.get_tool("portal_transforms")
    text = IRichText(obj).text
    raw = text.raw
    plain = transforms.convertTo("text/plain", raw, mimetype=text.mimeType).getData().strip()
    terms.append(plain)
    return " ".join(terms)


@indexer(ICardsSection)
def get_cardssection_searchabletext(obj):
    terms = get_title_and_description_terms(obj)
    for card in obj.cards:
        terms.append(card["title"])
        terms.append(card["subtitle"])
        terms.append(card["description"])
    return " ".join(terms)


@indexer(IPage)
def get_page_searchabletext(obj):
    """Compute SearchableText of IPage with SearchableText of its ISection"""
    terms = [_unicode_save_string_concat(SearchableText(obj))]
    catalog = api.portal.get_tool("portal_catalog")
    brains = api.content.find(context=obj, depth=1, object_provides=ISection)
    for brain in brains:
        indexes = catalog.getIndexDataForRID(brain.getRID())
        searchable_terms = indexes.get("SearchableText") or []
        terms.extend(searchable_terms)
    return " ".join(terms)
