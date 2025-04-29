from collective.contentsections.behaviors.leadicon import ILeadIcon
from plone import api

import pytest


BEHAVIOR = "collective.contentsections.leadicon"


CONTENT_TYPES = [
    "collective.contentsections.BasicPage",
    "collective.contentsections.Contact",
    "collective.contentsections.EventPage",
    "collective.contentsections.Location",
    "collective.contentsections.NewsPage",
    "collective.contentsections.TextSection",
    "Folder",
    "File",
    "Image",
    "Link",
]


class TestLeadIconBehavior:

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
                assert ILeadIcon.providedBy(content)

    # TODO : test icon()
