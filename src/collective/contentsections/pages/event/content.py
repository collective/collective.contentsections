from collective.contentsections.pages.base import IPage
from collective.contentsections.pages.base import Page
from zope.interface import implementer


class IEventPage(IPage):
    """EventPage schema"""


@implementer(IEventPage)
class EventPage(Page):
    """EventPage class"""
