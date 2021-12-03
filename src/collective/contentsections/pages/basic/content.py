from collective.contentsections.pages.base import IPage
from collective.contentsections.pages.base import Page
from plone.dexterity.content import Container
from zope.interface import implementer


class IBasicPage(IPage):
    """BasicPage schema"""


@implementer(IBasicPage)
class BasicPage(Page):
    """BasicPage class"""
