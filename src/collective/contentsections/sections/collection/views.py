from collective.contentsections.sections import SectionView


class CollectionSectionView(SectionView):
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
                "lead_image_url": f"{brain.getURL()}/@@images/image/large",
                "effective_date": brain.effective,
                "start_date": brain.start,
                "end_date": brain.end,
            }
            for brain in brains
        ]
        return results

    @property
    def all_items_link_url(self):
        return self.context.collection.to_object.absolute_url()

    @property
    def all_items_link_text(self):
        return self.context.collection_link_text

    @property
    def show_item_description(self):
        return self.context.show_description

    @property
    def show_item_lead_image(self):
        return self.context.show_lead_image

    @property
    def show_item_publication_date(self):
        return self.context.show_publication_date
