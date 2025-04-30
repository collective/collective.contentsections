from plone import api

import pytest


class TestUtilsView:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_base_page_view(self, contents):
        """Test the base_page_view."""
        page = api.content.get(path="/plone/basic-page-with-text-section")
        view = api.content.get_view(
            name="page_view",
            context=page,
        )
        assert "<p>This is text section two!</p>" in view()
