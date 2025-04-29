from collective.contentsections.contents.base import IElement
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


class ILocation(model.Schema):
    """Location schema"""


@implementer(ILocation, IElement)
class Location(Item):
    """Location content type"""
