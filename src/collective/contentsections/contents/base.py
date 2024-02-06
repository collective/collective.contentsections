from Products.Five.browser import BrowserView
from zope.interface import Interface


class IElement(Interface):
    """Marker interface for element content type"""


class ElementView(BrowserView):
    """Element view"""

    def __call__(self):
        section = self.context.__parent__
        url = f"{section.absolute_url()}/folder_contents"
        self.request.response.redirect(url)
