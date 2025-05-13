from plone import api

import pytest


class TestBaseContent:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_element_view(self, contents):
        """Test the element_view view."""
        contact = api.content.get(
            path="/plone/basic-page-1/a-contacts-section/a-contact"
        )
        view = api.content.get_view(
            name="element_view",
            context=contact,
        )
        view()
        assert view.request.response.status == 302
        assert (
            view.request.response.headers["location"]
            == "http://nohost/plone/basic-page-1/a-contacts-section/folder_contents"
        )
