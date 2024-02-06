from plone import api
from plone.app.contenttypes.browser.link_redirect_view import LinkRedirectView


class ElementView(LinkRedirectView):
    """Element view"""

    def __call__(self):
        if api.user.has_permission("Modify portal content", user=api.user.get_current(), obj=self.context):
            section = self.context.__parent__
            url = f"{section.absolute_url()}/folder_contents"
            self.request.response.redirect(url)
        super().__call__()
