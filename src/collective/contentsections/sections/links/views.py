from plone import api
from plone.app.uuid.utils import uuidToURL

from collective.contentsections.sections.base import BaseLinksSectionView
from collective.contentsections.sections.base import ISection


class LinksSectionView(BaseLinksSectionView):
    """LinksSection view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        brains = api.content.find(
            context=self.context,
            depth=1,
            portal_type="Link",
            sort_on="getObjPositionInParent",
        )
        results = []
        for brain in brains:
            remote_url = brain.getRemoteUrl
            if "resolveuid" in remote_url:
                uid = remote_url.split("/")[-1]
                remote_url = uuidToURL(uid)
            results.append(
                {
                    "title": brain.Title,
                    "description": brain.Description,
                    "url": remote_url,
                    "lead_image_url": f"{brain.getURL()}/@@images/image/{lead_image_scale}",
                    "effective_date": None,
                    "tags": brain.Subject,
                }
            )
        return results
