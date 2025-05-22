from plone import api

import pytest


class TestLinkRedirectView:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_link_redirect_view(self, contents):
        """Test the element_view view."""
        link = api.content.get(path="/plone/basic-page-1/a-links-section/a-link")
        view = api.content.get_view(
            name="element_view",
            context=link,
        )
        view()
        assert view.request.response.status == 302
        assert (
            view.request.response.headers["location"]
            == "http://nohost/plone/basic-page-1/a-links-section/folder_contents"
        )
        with api.env.adopt_roles(
            [
                "Anonymous",
            ]
        ):
            view()
            assert view.request.response.status == 302
            assert view.request.response.headers["location"] == "https://www.imio.be"
