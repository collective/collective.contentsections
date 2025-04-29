from plone import api

import pytest


class TestSelectionSectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_selection_section_views(self, contents):
        """Test selection section view"""
        content = api.content.get(path="/plone/basic-page-1/a-selection-section")
        view = api.content.get_view(
            name="card_view",
            context=content,
        )
        assert view.items[0].get("title") == "Event page 1"
