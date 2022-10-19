from collective.contentsections import _
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import Section
from plone import schema
from zope.interface import implementer


class ILocationsSection(ISection):
    """LocationsSection schema"""

    initial_zoom_level = schema.Choice(
        title=_("Initial zoom level"),
        values=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        required=False,
    )


@implementer(ILocationsSection)
class LocationsSection(Section):
    """LocationsSection content type"""
