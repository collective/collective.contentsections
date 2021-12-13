from Products.Five.browser import BrowserView


class RowView(BrowserView):
    """Row view"""

    def __call__(self):
        page = self.context.__parent__
        url = f"{page.absolute_url()}#{self.context.id}"
        self.request.response.redirect(url)
