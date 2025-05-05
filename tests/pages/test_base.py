from AccessControl import Unauthorized
from plone import api

import pytest


class TestBase:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_base_page_template(self, contents):
        """Test the base_page_view."""
        page = api.content.get(path="/plone/basic-page-1")
        view = api.content.get_view(
            name="base_page_template",
            context=page,
        )
        assert view.template_name == "base_page_view.pt"
        assert view.macros.names == ["master"]
        assert view().id == "base_page_view.pt"

        view_reorder = api.content.get_view(
            name="reorder_sections",
            context=page,
        )
        with pytest.raises(Unauthorized) as exc:
            view_reorder()
        assert str(exc.value) == "Unauthorized()"

        # Test with Manager role
        # TODO : Check why this is not working
        # with api.env.adopt_roles(
        #     [
        #         "Manager",
        #     ]
        # ):
        #     view_reorder()

    def test_ipage(self, contents):
        """Test the IPage interface."""
        page = api.content.get(path="/plone/basic-page-1")
        assert page.canSetDefaultPage() is False
