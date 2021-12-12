from collective.contentsections import _
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone import schema
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import Interface
from zope.interface import implementer


class IColumn(Interface):
    """Column schema"""

    width = schema.Choice(
        title=_("Column width"),
        vocabulary="collective.contentsections.ColumnWidths",
        required=False,
    )


class IRow(model.Schema):
    """Row schema"""

    columns = schema.List(
        title=_("Columns"),
        value_type=DictRow(title=_("Column"), schema=IColumn),
        missing_value=[],
        min_length=1,
    )

    is_full_width = schema.Bool(
        title=_("Full width"),
        default=False,
        missing_value=False,
    )

    directives.widget("columns", DataGridFieldFactory)


@implementer(IRow)
class Row(Item):
    """Row class"""

    def Title(self):
        return _("Configuration row")
