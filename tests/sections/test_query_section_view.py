from plone import api

import pytest


class TestQuerySectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_query_section_views(self, contents):
        """Test query section view"""
        content = api.content.get(path="/plone/basic-page-1/a-query-section")
        view = api.content.get_view(
            name="card_view",
            context=content,
        )
        assert view.items[0].get("title") == "News page 1"
        assert len(view.items) == 3
