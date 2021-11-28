from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope.interface import implementer


class ICollectionSection(ISection):
    """CollectionSection schema"""

    collection = RelationChoice(
        title=_(u"Collection"),
        source=CatalogSource(),
    )
    items_number = schema.Int(
        title=_(u"Number of items to display"),
        min=1,
        max=12,
    )
    group_size = schema.Choice(
        title=_(u"Group size"),
        values=[1, 2, 3, 4],
    )
    collection_link_text = schema.TextLine(
        title=_(u"Text for the link to the collection"),
        required=False,
    )
    show_lead_image = schema.Bool(
        title=_(u"Show items lead image"),
        required=False,
    )
    show_description = schema.Bool(
        title=_(u"Show items description"),
        required=False,
    )
    show_publication_date = schema.Bool(
        title=_(u"Show items publication date"),
        required=False,
    )

    directives.widget(
        "collection",
        RelatedItemsFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={"selectableTypes": ["Collection"], "favorites": []},
    )
    model.fieldset(
        "layout",
        fields=[
            "show_lead_image",
            "show_description",
            "show_publication_date",
        ],
    )


@implementer(ICollectionSection)
class CollectionSection(Section):
    """CollectionSection content type"""
