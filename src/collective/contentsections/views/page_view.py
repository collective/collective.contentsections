from Acquisition import aq_inner
from collective.contentsections import _
from plone.app.contenttypes.browser.folder import FolderView
from plone.app.contenttypes.browser.full_view import FullViewItem
from plone.dexterity.content import Container
from zope.interface import Interface
from zope.interface import implementer


class IPage(Interface):
    """Shared base marker interface and schema for Page content type"""


@implementer(IPage)
class Page(Container):
    """Shared base class for Page content types"""

    def canSetDefaultPage(self):
        return False


class PageView(FolderView):
    """Page view"""

    def __call__(self):
        # galleries_sections = self.context.listFolderContents(
        #     contentFilter={"portal_type": "imio.smartweb.SectionGallery"}
        # )
        # if len(galleries_sections) > 0:
        #     add_bundle_on_request(self.request, "spotlightjs")
        #     add_bundle_on_request(self.request, "flexbin")
        return self.index()

    def results(self, **kwargs):
        """
        Gets results for folder listings without taking care of friendly_types
        """
        # Extra filter
        kwargs.update(self.request.get("contentFilter", {}))
        kwargs.setdefault("batch", True)
        kwargs.setdefault("b_size", self.b_size)
        kwargs.setdefault("b_start", self.b_start)
        kwargs.setdefault("orphan", 1)

        listing = aq_inner(self.context).restrictedTraverse("@@folderListing", None)
        results = listing(**kwargs)
        return results

    @property
    def no_items_message(self):
        return _("There is no section on this page.")

    def get_section_classes(self, section):
        section_type = section.portal_type.split(".")[-1]
        section_type_class = f"section-{section_type.lower()}"
        return " ".join(["section", section_type_class, section.css_classes or "", section.css_width or ""])


class PageSectionView(FullViewItem):
    """Page view item"""
