from plone import api

from collective.contentsections.sections.base import BaseLinksSectionView
from collective.contentsections.sections.base import ISection


class FilesSectionView(BaseLinksSectionView):
    """FilesSection view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        brains = api.content.find(
            context=self.context,
            depth=1,
            portal_type="File",
            sort_on="getObjPositionInParent",
        )
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "url": brain.getURL(),
                "lead_image_url": f"{brain.getURL()}/@@images/image/{lead_image_scale}",
                "effective_date": brain.effective,
                "tags": brain.Subject,
                "mimetype_icon": f"mimetype-{brain.mime_type}",
            }
            for brain in brains
        ]
        return results
