from Acquisition import aq_inner
from collective.contentsections import _
from collective.contentsections.sections import ISection
from plone import api
from plone.app.contenttypes.browser.folder import FolderView
from plone.app.contenttypes.browser.full_view import FullViewItem
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


class PageView(FolderView):
    """Page view"""

    @property
    def sections(self):
        section_brains = api.content.find(
            context=self.context,
            depth=1,
            object_provides=ISection,
            sort_on="getObjPositionInParent",
        )
        section_objects = [b.getObject() for b in section_brains]
        return section_objects

    @property
    def rows(self):
        page_rows = [[section] for section in self.sections]
        return page_rows


class PageSectionView(FullViewItem):
    """Page view item"""
