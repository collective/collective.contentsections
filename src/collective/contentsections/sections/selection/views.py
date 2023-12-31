from plone import api

from collective.contentsections.sections.base import BaseLinksSectionView


class SelectionSectionView(BaseLinksSectionView):
    """Selection Section view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        objects = [rel.to_object for rel in self.context.relations if not rel.isBroken()]
        results = [
            {
                "title": obj.title,
                "description": obj.description,
                "url": obj.absolute_url(),
                "lead_image_url": f"{obj.absolute_url()}/@@images/image/{lead_image_scale}",
                "effective_date": obj.effective if hasattr(obj, "effective") else None,
                "start_date": obj.start.isoformat() if hasattr(obj, "start") else None,
                "end_date": obj.end.isoformat() if hasattr(obj, "end") else None,
                "tags": obj.subjects,
            }
            for obj in objects
        ]
        return results
