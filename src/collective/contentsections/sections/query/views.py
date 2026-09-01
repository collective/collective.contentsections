from collective.contentsections.sections.base import BaseLinksSectionView
from plone.app.contenttypes.behaviors.collection import ICollection


class QuerySectionView(BaseLinksSectionView):
    """Query Section view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        collection = ICollection(self.context)
        brains = collection.results(batch=False, brains=True, limit=collection.limit)
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "url": brain.getURL(),
                "lead_image_url": f"{brain.getURL()}/@@images/image/{lead_image_scale}",
                "effective_date": brain.effective,
                "start_date": brain.start.isoformat(),
                "end_date": brain.end.isoformat(),
                "tags": brain.Subject,
            }
            for brain in brains
        ]
        return results
