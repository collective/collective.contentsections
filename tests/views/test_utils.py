from plone import api

import pytest


class TestUtilsView:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_utilsview_macro(self, contents):
        """Test the macro method."""
        for uid in contents:
            content = api.content.get(UID=uid)
            view = api.content.get_view(
                name="collective_contentsections_utils",
                context=content,
            )
            assert (
                "collective.contentsections/src/collective/contentsections/views/macros.pt"
                in view.macros.template.filename
            )
