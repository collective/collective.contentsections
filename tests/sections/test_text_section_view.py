from plone import api
from plone.namedfile.file import NamedBlobImage

import base64
import pytest


IMAGE_B64 = "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAADUlEQVR4nGP4DwQMDAAAAFAABaL95YQAAAAASUVORK5CYII="

WIDTH_TO_SCALE = {
    3: "preview",
    4: "teaser",
    6: "large",
    8: "larger",
    9: "larger",
    12: "huge",
}


class TestTextSectionViews:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents
        self.content = api.content.get(path="/plone/basic-page-1/a-text-section")
        self.content.image = NamedBlobImage(
            data=base64.b64decode(IMAGE_B64),
            filename="image.png",
        )

    @pytest.mark.parametrize("width,expected_scale", sorted(WIDTH_TO_SCALE.items()))
    def test_lead_image_scale(self, width, expected_scale):
        self.content.lead_image_width = width
        view = api.content.get_view(name="column_view", context=self.content)
        assert view.lead_image_scale == expected_scale

    @pytest.mark.parametrize("view_name", ["float_view", "column_view"])
    @pytest.mark.parametrize("alignment", ["left", "right", "top", "bottom"])
    def test_renders_for_all_alignments(self, view_name, alignment):
        self.content.lead_image_alignment = alignment
        self.content.lead_image_width = 6
        # Force this section's layout so the parent page picks the view under
        # test (SectionView.__call__ only redirects; the real markup is
        # produced by the parent page's rendering pipeline, see PageView /
        # PageSectionView / FullViewItem.item_macros).
        self.content.layout = view_name
        basic_page = api.content.get(path="/plone/basic-page-1")
        rendered = basic_page.restrictedTraverse("page_view")()
        assert "@@images/image/" in rendered
        assert "This is a text section!" in rendered
