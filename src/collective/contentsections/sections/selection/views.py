from collective.contentsections.sections.base import LinksSectionView
from plone import api


class SelectionSectionView(LinksSectionView):
    """Selection Section view"""

    def items(self):
        objects = [rel.to_object for rel in self.context.relations if not rel.isBroken()]
        results = [
            {
                "title": obj.title,
                "description": obj.description,
                "url": obj.absolute_url(),
                "lead_image_url": f"{obj.absolute_url()}/@@images/image/{self.context.lead_image_scale}",
                "effective_date": obj.effective if hasattr(obj, "effective") else None,
                "start_date": obj.start if hasattr(obj, "start") else None,
                "end_date": obj.start if hasattr(obj, "start") else None,
            }
            for obj in objects
        ]
        return results
