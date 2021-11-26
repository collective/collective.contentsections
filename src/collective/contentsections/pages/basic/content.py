from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IBasicPage(model.Schema):
    """BasicPage schema"""


@implementer(IBasicPage)
class BasicPage(Container):
    """BasicPage class"""

    def canSetDefaultPage(self):
        return False
