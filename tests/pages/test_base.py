from AccessControl import Unauthorized
from plone import api
from plone.protect.authenticator import createToken

import json
import pytest


class TestBase:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents, http_request):
        self.portal = portal
        self.contents = contents
        self.request = http_request

    def test_base_page_template(self, contents, portal, request):
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
        request = portal.REQUEST
        request.form["_authenticator"] = createToken()
        request.method = "POST"
        request.environ["REQUEST_METHOD"] = "POST"
        request.form["section_id"] = "a-cards-section"
        request.form["delta"] = "2"
        current_order = [
            "a-cards-section",
            "a-collection-section",
            "a-contacts-section",
            "a-files-section",
            "a-html-section",
            "a-links-section",
            "another-links-section",
            "an-empty-locations-section",
            "a-locations-section",
            "a-selection-section",
            "a-text-section",
            "an-images-section",
        ]
        view_reorder()
        new_order = view_reorder.getOrdering().idsInOrder()
        assert new_order == current_order
        request.form["ordered_section_ids"] = json.dumps(current_order)
        view_reorder()
        new_order = view_reorder.getOrdering().idsInOrder()
        assert new_order == [
            "a-collection-section",
            "a-contacts-section",
            "a-cards-section",
            "a-files-section",
            "a-html-section",
            "a-links-section",
            "another-links-section",
            "an-empty-locations-section",
            "a-locations-section",
            "a-selection-section",
            "a-text-section",
            "an-images-section",
        ]

    def test_ipage(self, contents):
        """Test the IPage interface."""
        page = api.content.get(path="/plone/basic-page-1")
        assert page.canSetDefaultPage() is False
