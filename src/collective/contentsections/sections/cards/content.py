from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone import schema
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widgets.select import AjaxSelectFieldWidget
from plone.app.z3cform.widgets.select import SelectFieldWidget
from plone.autoform import directives
from zope.interface import Interface
from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section


class ICard(Interface):
    """Card schema"""

    title = schema.TextLine(
        title=_("Title"),
        required=False,
        default="",
        missing_value="",
    )
    subtitle = schema.TextLine(
        title=_("Subtitle"),
        required=False,
        default="",
        missing_value="",
    )
    description = schema.Text(
        title=_("Text"),
        required=False,
        default="",
        missing_value="",
    )
    icon = schema.Choice(
        title=_("Icon"),
        vocabulary="collective.contentsections.LeadIcons",
        required=False,
        default="",
        missing_value="",
    )
    relation_uid = schema.Choice(
        title=_("Selection"),
        vocabulary=StaticCatalogVocabulary({}, title_template="{brain.Type}: {brain.Title} at {path}"),
        required=False,
    )

    directives.widget("title", placeholder=_("Card title"))
    directives.widget("subtitle", placeholder=_("Card subtitle"))
    directives.widget("icon", SelectFieldWidget, pattern_options={"placeholder": _("Select an icon")})

    # SEE https://6.docs.plone.org/backend/relations.html#relation-fields-without-relations
    # Does not work in Plone 6.1
    # directives.widget(
    #     "relation_uid",
    #     AjaxSelectFieldWidget,
    #     vocabulary=StaticCatalogVocabulary({}, title_template="{brain.Type}: {brain.Title} at {path}"),
    #     pattern_options={
    #         "placeholder": _("Select a related content"),
    #         "minimumInputLength": 3,
    #         "ajax": {"quietMillis": 300},
    #     },
    # )


class ICardsSection(ISection):
    """CardsSection schema"""

    cards = schema.List(
        title=_("Cards"),
        value_type=DictRow(title=_("Card"), schema=ICard),
        min_length=1,
        missing_value=[],
    )
    group_size = schema.Choice(
        title=_("Group size"),
        values=[1, 2, 3, 4],
        default=3,
    )
    card_link_text = schema.TextLine(
        title=_("Card link text"),
        required=False,
    )

    directives.widget("cards", DataGridFieldFactory, allow_reorder=True)
    directives.order_after(group_size="hide_title")


@implementer(ICardsSection)
class CardsSection(Section):
    """CardsSection content type"""
