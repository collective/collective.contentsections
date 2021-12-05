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
        fields=["hide_title", "width", "background_image", "css_classes"],
    )


class ILinksSection(ISection):
    """Shared base marker interface and schema for CollectionSection, SelectionSection and LinksSection"""

    group_size = schema.Choice(
        title=_("Group size"),
        values=[1, 2, 3, 4],
        default=3,
    )

    lead_image_scale = schema.Choice(
        title=_("Lead image size"),
        vocabulary="plone.app.vocabularies.ImagesScales",
        default="preview",
    )

    hide_lead_image = schema.Bool(
        title=_("Show items lead image"),
        required=False,
        default=False,
    )
    hide_description = schema.Bool(
        title=_("Show items description"),
        required=False,
        default=False,
    )
    hide_publication_date = schema.Bool(
        title=_("Show items publication date"),
        required=False,
        default=True,
    )

    model.fieldset(
        "layout",
        fields=[
            "group_size",
            "lead_image_scale",
            "hide_lead_image",
            "hide_description",
            "hide_publication_date",
        ],
    )


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


class LinksSectionView(SectionView):
    """Section view for CollectionSection, SelectionSection and LinksSection"""

    @property
    def items(self):
        return []

    @property
    def more_link_url(self):
        return None

    @property
    def more_link_text(self):
        return None


def reindex_parent_page(section, event):
    page = section.__parent__
    if page is not None:
        page.reindexObject()
