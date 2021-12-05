from collective.contentsections.sections import LinksSectionView


class CollectionSectionView(LinksSectionView):
    """Collection Section view"""

    def items(self):
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
                "lead_image_url": f"{brain.getURL()}/@@images/image/{self.item_lead_image_scale}",
                "effective_date": brain.effective,
                "start_date": brain.start,
                "end_date": brain.end,
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
