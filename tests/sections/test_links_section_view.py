import pytest


class TestLinksSectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_links_section_views(self, contents):
        """ """
        # content = api.content.get(path="/plone/basic-page-1/a-links-section")
        # view = api.content.get_view(
        #     name="card_view",
        #     context=content,
        # )
        # __import__("pdb").set_trace()
        # assert (
        #     view.data_pat_leaflet == '{"fullscreencontrol": true, "zoomcontrol": true}'
        # )
        # __import__("pdb").set_trace()
        # assert view.data_geojson.get("type") == "FeatureCollection"
        # TODO : why no latitude / longitude ?
