from collective.contentsections.sections.text.content import ITextSection
from plone import api

import logging


logger = logging.getLogger("collective.contentsections.upgrades")


def upgrade_from_1000_to_1001(setup):
    """"""
    # Migrate ITextSection.lead_image_scale values to lead_image_width."""
    SCALE_TO_WIDTH = {
        "icon": 3,
        "tile": 3,
        "thumb": 3,
        "mini": 3,
        "preview": 4,
        "teaser": 6,
        "large": 8,
        "larger": 9,
        "great": 12,
        "huge": 12,
    }
    brains = api.content.find(object_provides=ITextSection.__identifier__)
    for brain in brains:
        obj = brain.getObject()
        scale = getattr(obj, "lead_image_scale", None)
        obj.lead_image_width = SCALE_TO_WIDTH.get(scale, 4)
        try:
            delattr(obj, "lead_image_scale")
        except AttributeError:
            pass
        obj.reindexObject()
    logger.info(
        "Migrated %s TextSection(s): lead_image_scale -> lead_image_width", len(brains)
    )
