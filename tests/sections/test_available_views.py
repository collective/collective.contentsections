from plone import api
from zope.interface import implementedBy

import pytest


VIEWS = {
    "ICardsSection": [
        "view",
    ],
    "ICollectionSection": [
        "card_view",
        "card_carousel_view",
        "carousel_view",
        "list_view",
    ],
    "IContactsSection": [
        "card_view",
    ],
    "IFilesSection": [
        "card_view",
        "card_carousel_view",
        "carousel_view",
        "list_view",
    ],
    "IHTMLSection": [
        "view",
    ],
    "IImagesSection": [
        "card_view",
        "card_carousel_view",
        "carousel_view",
        "gallery_view",
    ],
    "ILinksSection": [
        "card_view",
        "card_carousel_view",
        "carousel_view",
        "list_view",
    ],
    "ILocationsSection": [
        "view",
    ],
    "ISelectionSection": [
        "card_view",
        "card_carousel_view",
        "carousel_view",
        "list_view",
    ],
    "ITextSection": [
        "view",
    ],
}


class TestAvailableSectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_section_views(self, contents):
        """Test the macro method."""
        for uid in contents:
            content = api.content.get(UID=uid)
            for iface in implementedBy(content.__class__):
                views = VIEWS.get(iface.getName(), [])
                for view in views:
                    assert content.restrictedTraverse(view) is not None
