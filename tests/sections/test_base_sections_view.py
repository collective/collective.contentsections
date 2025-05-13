from collective.contentsections.sections.base import BaseGroupSectionView
from plone import api

import pytest


class TestBaseSections:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents, http_request):
        self.portal = portal
        self.contents = contents
        self.request = http_request

    def test_card_view(self, contents):
        """Test the card_view view."""
        section = api.content.get(path="/plone/basic-page-1/a-contacts-section")
        assert section.canSetDefaultPage() is False
        view = api.content.get_view(
            name="card_view",
            context=section,
        )
        view()
        assert view.request.response.status == 302
        assert (
            view.request.response.headers["location"]
            == "http://nohost/plone/basic-page-1#section-a-contacts-section"
        )

        assert view.items == [
            {
                "title": "A contact",
                "subtitle": "A contact subtitle",
                "description": "A contact description",
                "email": "a@contact.be",
                "phone": "+3223456789",
                "lead_image_url": None,
                "lead_image_caption": None,
            }
        ]

        assert view.groups == [
            [
                {
                    "title": "A contact",
                    "subtitle": "A contact subtitle",
                    "description": "A contact description",
                    "email": "a@contact.be",
                    "phone": "+3223456789",
                    "lead_image_url": None,
                    "lead_image_caption": None,
                }
            ]
        ]

        section_links = api.content.get(
            path="/plone/basic-page-1/a-links-section",
        )
        view_links = api.content.get_view(
            name="card_view",
            context=section_links,
        )

        assert view_links.more_link_url is None
        assert view_links.more_link_text is None

    def test_base_group_section_view_items(self, request):
        section = BaseGroupSectionView(self, request)
        assert section.items == []
