from collective.contentsections import _
from collective.contentsections.sections import SectionView
from plone import api
from plone.app.uuid.utils import uuidToObject


class CardsSectionView(SectionView):
    """Cards Section view"""

    @property
    def items(self):
        results = []
        for card in self.context.cards:
            relation_uid = card.get("relation_uid")
            relation_unrestricted = (
                uuidToObject(relation_uid, unrestricted=True) if relation_uid else None
            )
            relation_restricted = (
                relation_unrestricted
                if relation_unrestricted
                and api.user.has_permission("View", obj=relation_unrestricted)
                else None
            )
            relation_link_url = (
                relation_restricted.absolute_url() if relation_restricted else None
            )
            results.append(
                {
                    "icon": card["icon"],
                    "title": card["title"],
                    "subtitle": card["subtitle"],
                    "description": card["description"],
                    "relation_link_url": relation_link_url,
                }
            )
        return results

    @property
    def card_link_text(self):
        text = self.context.card_link_text
        return text if text else _("More information")
