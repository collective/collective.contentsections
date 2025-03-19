from plone import schema
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widgets.relateditems import RelatedItemsFieldWidget
from plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.sections.base import IBaseLinksSection
from collective.contentsections.sections.base import Section


class ICollectionSection(IBaseLinksSection):
    """CollectionSection schema"""

    collection = RelationChoice(
        title=_("Collection"),
        source=CatalogSource(),
    )
    items_number = schema.Int(
        title=_("Number of items to display"),
        min=1,
        max=12,
    )
    collection_link_text = schema.TextLine(
        title=_("Text for the link to the collection"),
        required=False,
        default="",
        missing_value="",
    )

    directives.widget(
        "collection",
        RelatedItemsFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={"selectableTypes": ["Collection"], "favorites": []},
    )

    directives.order_after(collection="hide_title")
    directives.order_after(items_number="collection")


@implementer(ICollectionSection)
class CollectionSection(Section):
    """CollectionSection content type"""
