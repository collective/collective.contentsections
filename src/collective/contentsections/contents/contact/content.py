from plone import schema
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.contents.base import IElement


class IContact(model.Schema):
    """Contact schema"""

    title = schema.TextLine(
        title=_("Title"),
        required=True,
    )
    subtitle = schema.TextLine(
        title=_("Subtitle"),
        required=False,
    )
    description = schema.Text(
        title=_("Description"),
        required=False,
    )
    email = schema.Email(
        title=_("Email"),
        required=False,
    )
    phone = schema.TextLine(
        title=_("Phone"),
        required=False,
    )


@implementer(IContact, IElement)
class Contact(Item):
    """Contact content type"""
