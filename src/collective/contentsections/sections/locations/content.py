from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from zope.interface import implementer


class ILocationsSection(ISection):
    """LocationsSection schema"""



@implementer(ILocationsSection)
class LocationsSection(Section):
    """LocationsSection content type"""
