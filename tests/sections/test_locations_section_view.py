from plone import api

import pytest


class TestLocationsSectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_locations_section_views(self, contents):
        """ """
        content = api.content.get(path="/plone/basic-page-1/a-locations-section")
        view = api.content.get_view(
            name="view",
            context=content,
        )
        assert (
            view.data_pat_leaflet
            == '{"fullscreencontrol": true, "zoomcontrol": true, "zoom": 10, "latitude": -40.64948618626043, "longitude": 45.22943849691794}'
        )
        assert view.center == (-40.64948618626043, 45.22943849691794)

        content = api.content.get(path="/plone/basic-page-1/an-empty-locations-section")
        view = api.content.get_view(
            name="view",
            context=content,
        )
        assert (
            view.data_pat_leaflet == '{"fullscreencontrol": true, "zoomcontrol": true}'
        )
        assert view.center == (0.0, 0.0)
