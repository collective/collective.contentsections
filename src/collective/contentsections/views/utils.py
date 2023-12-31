from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

MACROS_PAGE_TEMPLATE_PATH = "macros.pt"


class UtilsView(BrowserView):
    @property
    def macros(self):
        return ViewPageTemplateFile(MACROS_PAGE_TEMPLATE_PATH).macros
