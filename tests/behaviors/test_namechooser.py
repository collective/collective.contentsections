from collective.contentsections.behaviors.namechooser import INameFromUUID
from collective.contentsections.behaviors.namechooser import NameFromUUID
from plone import api

import pytest
import re


BEHAVIOR = "collective.contentsections.namefromuuid"
CONTENT_TYPES = [
    "collective.contentsections.CardsSection",
    "collective.contentsections.CollectionSection",
    "collective.contentsections.Contact",
    "collective.contentsections.ContactsSection",
    "collective.contentsections.FilesSection",
    "collective.contentsections.HTMLSection",
    "collective.contentsections.ImagesSection",
    "collective.contentsections.LinksSection",
    "collective.contentsections.Location",
    "collective.contentsections.LocationsSection",
    "collective.contentsections.SelectionSection",
    "collective.contentsections.TextSection",
    "File",
    "Image",
    "Link",
]


class TestNameChooserBehavior:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_behavior_enabled(self, get_behaviors):
        """Test if behavior is installed for content types."""
        for content_type in CONTENT_TYPES:
            assert BEHAVIOR in get_behaviors(content_type)

    def test_behavior_is_provided(self, contents):
        """Test if behavior is provided by test contents."""
        for uid in contents:
            content = api.content.get(UID=uid)
            if content.portal_type in CONTENT_TYPES:
                assert INameFromUUID.providedBy(content)

    def test_title(self, contents):
        """Test if title is generated correctly."""
        for uid in contents:
            content = api.content.get(UID=uid)
            if content.portal_type in CONTENT_TYPES:
                generated_name = NameFromUUID(content)
                prefix = content.portal_type.split(".")[-1].lower()
                assert re.match(rf"^{prefix}-[a-f0-9]{{32}}$", generated_name.title)
