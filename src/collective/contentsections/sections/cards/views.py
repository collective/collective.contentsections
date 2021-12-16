from collective.contentsections import _
from collective.contentsections.sections import SectionView
from plone import api


class CardsSectionView(SectionView):
    """Cards Section view"""

    @property
    def items(self):
        results = []
        for card in self.context.cards:
            relation_uid = card.get("relation_uid")
            remote_url = card.get("remote_url")
            if relation_uid:  # relation takes precedence over remote_url
                relation = api.content.get(UID=relation_uid) if relation_uid else None
                relation_link_url = relation.absolute_url() if relation else None
            elif remote_url:
                relation_link_url = remote_url
            else:
                relation_link_url = None

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
    def relation_link_text(self):
        text = self.context.relation_link_text
        return text if text else _("More information")
