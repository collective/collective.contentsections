from collective.contentsections import _
from collective.contentsections.sections.base import ILinksSection
from collective.contentsections.sections.base import Section
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import implementer


class ISelectionSection(ILinksSection):
    """SelectionSection schema"""

    relations = RelationList(
        title=_(u"Items"),
        value_type=RelationChoice(
            title=_(u"Item"),
            vocabulary=StaticCatalogVocabulary({}),
        ),
    )

    directives.widget(
        "relations",
        AjaxSelectFieldWidget,
        vocabulary=StaticCatalogVocabulary({}, title_template="{brain.Type}: {brain.Title} at {path}"),
        pattern_options={
            "placeholder": _("Select items"),
            "minimumInputLength": 3,
            "ajax": {"quietMillis": 300},
        },
    )


@implementer(ISelectionSection)
class SelectionSection(Section):
    """SelectionSection content type"""
