from collective.contentsections.sections.base import BaseLinksSectionView
from collective.contentsections.sections.base import ISection
from plone import api


class LinksSectionView(BaseLinksSectionView):
    """LinksSection view"""

    def items(self):
        lead_image_scale = self.item_lead_image_scale
        brains = api.content.find(context=self.context, depth=1, portal_type="Link")
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "url": brain.getRemoteUrl,
                "lead_image_url": f"{brain.getURL()}/@@images/image/{lead_image_scale}",
                "effective_date": None,
                "tags": brain.Subject,
            }
            for brain in brains
        ]
        return results
