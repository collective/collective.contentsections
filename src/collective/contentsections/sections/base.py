from collective.contentsections import _
from plone import schema
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from Products.Five.browser import BrowserView
from zope.interface import implementer


class ISection(model.Schema):
    """Shared base marker interface and schema for Sections"""

    title = schema.TextLine(
        title=_("Section title"),
    )
    hide_title = schema.Bool(
        title=_("Hide section title in page"),
        default=False,
    )
    background_image = NamedBlobImage(
        title=_("Background image"),
        required=False,
    )
    width = schema.Choice(
        title=_("Section width"),
        vocabulary="collective.contentsections.SectionWidths",
        default=12,
    )
    css_classes = schema.TextLine(
        title=_("CSS Classes"),
        required=False,
    )

    model.fieldset(
        "layout",
        label="Layout",
        fields=["width", "background_image", "css_classes"],
    )


class IBaseLinksSection(ISection):
    """Shared base marker interface and schema for CollectionSection, SelectionSection and LinksSection"""

    hide_item_lead_images = schema.Bool(
        title=_("Hide item lead images"),
        required=False,
        default=False,
    )
    hide_item_descriptions = schema.Bool(
        title=_("Hide item descriptions"),
        required=False,
        default=False,
    )
    hide_item_publication_dates = schema.Bool(
        title=_("Hide item publication dates"),
        required=False,
        default=True,
    )
    group_size = schema.Choice(
        title=_("Group size"),
        values=[1, 2, 3, 4],
        default=3,
    )

    model.fieldset(
        "layout",
        fields=[
            "group_size",
        ],
    )

    directives.order_after(group_size="width")


@implementer(ISection)
class Section(Container):
    """Shared base class for Sections"""

    def canSetDefaultPage(self):
        return False


class SectionView(BrowserView):
    """Section view"""

    def __call__(self):
        page = self.context.__parent__
        url = f"{page.absolute_url()}#section-{self.context.id}"
        self.request.response.redirect(url)


class BaseLinksSectionView(SectionView):
    """Shared section view for CollectionSection, SelectionSection and LinksSection"""

    @property
    def items(self):
        return []

    @property
    def more_link_url(self):
        return None

    @property
    def more_link_text(self):
        return None

    @property
    def item_lead_image_scale(self):
        layout = self.context.getLayout()
        section_size = self.context.width
        group_size = self.context.group_size
        cols = section_size / group_size
        if layout == "carousel_view" or "cards_view":
            if cols > 6:
                return "huge"
            elif cols > 3:
                return "large"
        elif layout == "listing_view":
            return "mini"
        return "preview"


def reindex_parent_page(section, event):
    page = section.__parent__
    if page is not None:
        page.reindexObject()
