from plone import api

from collective.contentsections.sections.base import BaseGroupSectionView


class ContactsSectionView(BaseGroupSectionView):
    """ContactsSection view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        brains = api.content.find(
            context=self.context,
            depth=1,
            portal_type="collective.contentsections.Contact",
            sort_on="getObjPositionInParent",
        )
        results = []
        for brain in brains:
            contact = brain.getObject()
            results.append(
                {
                    "title": contact.title,
                    "subtitle": contact.subtitle,
                    "description": contact.description,
                    "email": contact.email,
                    "phone": contact.phone,
                    "lead_image_url": f"{brain.getURL()}/@@images/image/{lead_image_scale}" if contact.image else None,
                    "lead_image_caption": contact.image_caption,
                }
            )
        return results
