from collective.contentsections.pages.base import IPage
from collective.contentsections.pages.base import Page
from plone.autoform import directives
from zope.interface import implementer


class IEventPage(IPage):
    """EventPage schema"""

    directives.omitted("hide_title")


@implementer(IEventPage)
class EventPage(Page):
    """EventPage class"""
