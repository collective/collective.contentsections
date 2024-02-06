from plone import schema
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.contents.base import IElement


class ILocation(model.Schema):
    """Location schema"""


@implementer(ILocation, IElement)
class Location(Item):
    """Location content type"""
