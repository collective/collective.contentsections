from collective.contentsections.upgrades.upgrades import upgrade_from_1000_to_1001
from plone import api

import pytest


class TestMigrateLeadImageScaleToWidth:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents
        self.content = api.content.get(path="/plone/basic-page-1/a-text-section")

    @pytest.mark.parametrize(
        "scale,expected_width",
        [
            ("icon", 3),
            ("tile", 3),
            ("thumb", 3),
            ("mini", 3),
            ("preview", 4),
            ("teaser", 6),
            ("large", 8),
            ("larger", 9),
            ("great", 12),
            ("huge", 12),
            ("unknown-scale", 4),
        ],
    )
    def test_migrate_known_scale(self, scale, expected_width):
        self.content.lead_image_scale = scale
        upgrade_from_1000_to_1001(self.portal.portal_setup)
        assert self.content.lead_image_width == expected_width
        assert not hasattr(self.content, "lead_image_scale")

    def test_migrate_without_previous_scale(self):
        assert not hasattr(self.content, "lead_image_scale")
        upgrade_from_1000_to_1001(self.portal.portal_setup)
        assert self.content.lead_image_width == 4

    def test_migrate_replays_typeinfo_genericsetup_step(self):
        fti = self.portal.portal_types["collective.contentsections.TextSection"]
        # Simulate an older FTI, as it would be before this upgrade step runs.
        fti.default_view = "view"
        fti.view_methods = ("view",)
        self.portal.portal_setup.runAllImportStepsFromProfile(
            "profile-collective.contentsections.upgrades:to1001",
            purge_old=False,
            ignore_dependencies=True,
        )
        assert fti.default_view == "column_view"
        assert fti.view_methods == ("column_view", "float_view")
