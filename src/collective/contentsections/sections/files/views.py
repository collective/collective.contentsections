from collective.contentsections.sections.base import BaseLinksSectionView
from collective.contentsections.sections.base import ISection
from plone import api


class FilesSectionView(BaseLinksSectionView):
    """FilesSection view"""

    def items(self):
        brains = api.content.find(context=self.context, depth=1, portal_type="File")
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "url": brain.getURL(),
                "lead_image_url": f"{brain.getURL()}/@@images/image/{self.item_lead_image_scale}",
                "effective_date": brain.effective,
            }
            for brain in brains
        ]
        return results
