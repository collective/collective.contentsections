from collective.contentsections.pages.base import IPage
from collective.contentsections.pages.base import Page
from zope.interface import implementer


class INewsPage(IPage):
    """NewsPage schema"""


@implementer(INewsPage)
class NewsPage(Page):
    """NewsPage class"""
