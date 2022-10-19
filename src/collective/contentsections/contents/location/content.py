from collective.contentsections import _
from plone import schema
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


class ILocation(model.Schema):
    """Location schema"""


@implementer(ILocation)
class Location(Item):
    """Location content type"""
