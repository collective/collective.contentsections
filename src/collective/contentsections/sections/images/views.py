from plone import api

from collective.contentsections.sections.base import BaseLinksSectionView
from collective.contentsections.sections.base import ISection
from collective.contentsections.sections.base import SectionView


class ImagesSectionView(BaseLinksSectionView):
    """ImagesSection view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        brains = api.content.find(
            context=self.context,
            depth=1,
            portal_type="Image",
            sort_on="getObjPositionInParent",
        )
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "url": None,  # TODO
                "lead_image_url": f"{brain.getURL()}/@@images/image/{lead_image_scale}",
                "effective_date": brain.effective,
                "tags": [],
            }
            for brain in brains
        ]
        return results


class ImagesSectionGalleryView(SectionView):
    """ImagesSection gallery view"""

    def items(self):
        brains = api.content.find(
            context=self.context,
            depth=1,
            portal_type="Image",
            sort_on="getObjPositionInParent",
        )
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "full_image_url": f"{brain.getURL()}/@@images/image/huge",
                "preview_image_url": f"{brain.getURL()}/@@images/image/preview",
            }
            for brain in brains
        ]
        return results
