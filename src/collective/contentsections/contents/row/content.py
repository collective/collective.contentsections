from collective.contentsections import _
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.row import DictRow
from plone import schema
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope.interface import Interface
from zope.interface import implementer


class IColumn(Interface):
    """Column schema"""

    width = schema.Choice(
        title=_("Column width"),
        vocabulary="collective.contentsections.ColumnWidths",
    )
    css_classes = schema.TextLine(
        title=_("Column CSS Classes"),
        required=False,
        default="",
        missing_value="",
    )


class IRow(model.Schema):
    """Row schema"""

    columns = schema.List(
        title=_("Columns"),
        value_type=DictRow(title=_("Column"), schema=IColumn),
        min_length=1,
        missing_value=[],
    )
    column_alignment = schema.Choice(
        title=_("Column alignment"),
        vocabulary="collective.contentsections.ColumnAlignments",
        default="center",
    )
    is_full_width = schema.Bool(
        title=_("Full width"),
        default=False,
    )
    background_image = NamedBlobImage(
        title=_("Background image"),
        required=False,
    )
    css_classes = schema.TextLine(
        title=_("CSS Classes"),
        required=False,
        default="",
        missing_value="",
    )

    directives.widget("columns", DataGridFieldFactory)


@implementer(IRow)
class Row(Item):
    """Row class"""

    def Title(self):
        widths = [f"{col['width']}/12" for col in self.columns]
        return _("Row") + " " + " - ".join(widths)
