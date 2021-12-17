from Acquisition import aq_inner
from collective.contentsections import _
from collective.contentsections.contents import IRow
from collective.contentsections.sections import ISection
from plone import api
from plone.app.contenttypes.browser.full_view import FullViewItem
from plone.dexterity.content import Container
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from zope.interface import implementer


class IPage(Interface):
    """Shared base marker interface and schema for Pages"""


@implementer(IPage)
class Page(Container):
    """Shared base class for Pages"""

    def canSetDefaultPage(self):
        return False


class PageView(BrowserView):
    """Page view"""

    @property
    def items(self):
        item_brains = api.content.find(
            context=self.context,
            depth=1,
            object_provides=[ISection, IRow],
            sort_on="getObjPositionInParent",
        )
        items_objects = [b.getObject() for b in item_brains]
        return items_objects

    @property
    def rows(self):
        page_rows = []
        row_with_config = None
        for item in self.items:
            if IRow.providedBy(item):
                if row_with_config:
                    page_rows.append(row_with_config)
                row_with_config = {
                    "sections": [],
                    "config": item,
                }
            if ISection.providedBy(item):
                if not row_with_config:
                    page_rows.append({"sections": [item], "config": None})
                else:
                    row_with_config["sections"].append(item)
                    columns_number = len(row_with_config["config"].columns)
                    sections_number = len(row_with_config["sections"])
                    if columns_number == sections_number:
                        page_rows.append(row_with_config)
                        row_with_config = None
        if row_with_config:
            page_rows.append(row_with_config)

        return page_rows


class PageSectionView(FullViewItem):
    """Page view item"""


class PageTemplateView(BrowserView):
    def __call__(self):
        return ViewPageTemplateFile(self.template_name)

    @property
    def template_name(self):
        return "base_page_view.pt"

    @property
    def macros(self):
        return ViewPageTemplateFile(self.template_name).macros
