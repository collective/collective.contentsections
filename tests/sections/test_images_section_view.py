from plone import api

import pytest


class TestImagesSectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_images_section_views(self, contents):
        """ """
        content = api.content.get(path="/plone/basic-page-1/an-images-section")
        view = api.content.get_view(
            name="gallery_view",
            context=content,
        )
        assert view.items()[0].get("full_image_url") == (
            "http://nohost/plone/basic-page-1/an-images-section/an-image/@@images/image/huge"
        )
