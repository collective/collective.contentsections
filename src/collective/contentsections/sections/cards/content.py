from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone import schema
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope.interface import Interface
from zope.interface import implementer


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
        vocabulary=StaticCatalogVocabulary({}),
        required=False,
    )
    remote_url = schema.TextLine(
        title=_("Remote url"),
        required=False,
        default="",
        missing_value="",
    )

    directives.widget("title", placeholder=_("Card title"))
    directives.widget("subtitle", placeholder=_("Card subtitle"))
    directives.widget("icon", SelectFieldWidget, pattern_options={"placeholder": _("Select an icon")})
    directives.widget("remote_url", placeholder=_("Remote url"))

    # SEE https://training.plone.org/5/mastering-plone/relations.html?highlight=catalogsource#using-different-widgets-for-relations
    directives.widget(
        "relation_uid",
        AjaxSelectFieldWidget,
        vocabulary=StaticCatalogVocabulary({}, title_template="{brain.Type}: {brain.Title} at {path}"),
        pattern_options={
            "placeholder": _("Select a related content"),
            "minimumInputLength": 3,
            "ajax": {"quietMillis": 300},
        },
    )


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
    relation_link_text = schema.TextLine(
        title=_(u"Text for the link to the related content"),
        required=False,
    )

    directives.widget("cards", DataGridFieldFactory, allow_reorder=True)
    directives.order_before(group_size="is_full_width")


@implementer(ICardsSection)
class CardsSection(Section):
    """CardsSection content type"""
