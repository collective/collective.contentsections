from collective.contentsections.sections.base import BaseLinksSectionView


class CollectionSectionView(BaseLinksSectionView):
    """Collection Section view"""

    @property
    def items(self):
        lead_image_scale = self.item_lead_image_scale
        brains = self.context.collection.to_object.results(
            batch=False,
            brains=True,
            limit=self.context.items_number,
        )
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

    @property
    def more_link_url(self):
        return self.context.collection.to_object.absolute_url()

    @property
    def more_link_text(self):
        return self.context.collection_link_text
