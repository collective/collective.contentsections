from plone.dexterity.content import Container
from zope.interface import Interface
from zope.interface import implementer


class IPage(Interface):
    """Shared base marker interface and schema for Pages"""


@implementer(IPage)
class Page(Container):
    """Shared base class for Pages"""

    def canSetDefaultPage(self):
        return False
