from plone.app.z3cform.interfaces import IPloneFormLayer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer, IPloneFormLayer):
    """Marker interface that defines a browser layer."""
