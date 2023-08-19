from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from Products.Five.browser import BrowserView
from zope.interface import implementer

from collective.contentsections import _


class ISection(model.Schema):
    """Shared base marker interface and schema for Sections"""

    title = schema.TextLine(
        title=_("Section title"),
    )
    hide_title = schema.Bool(
        title=_("Hide section title in page"),
        required=False,
        default=False,
    )
    container_width = schema.Choice(
        title=_("Container width"),
        vocabulary="collective.contentsections.ContainerWidths",
        default=12,
    )
    background_image = NamedBlobImage(
        title=_("Background image"),
        required=False,
    )
    css_classes = schema.List(
        title=_("CSS Classes"),
        value_type=schema.Choice(
            vocabulary="collective.taxonomy.section_css_classes",
        ),
        required=False,
        missing_value=[],
    )

    directives.widget(css_classes=SelectFieldWidget)

    model.fieldset(
        "layout",
        label="Layout",
        fields=["container_width", "background_image", "css_classes"],
    )


class IBaseGroupSection(ISection):
    """Shared base marker interface and schema for group sections"""

    group_size = schema.Choice(
        title=_("Group size"),
        values=[1, 2, 3, 4, 6],
        default=3,
    )

    directives.order_after(group_size="hide_title")


class IBaseLinksSection(IBaseGroupSection):
    """Shared base marker interface and schema for link type sections"""

    hide_item_titles = schema.Bool(
        title=_("Hide item titles"),
        required=False,
        default=False,
    )
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


class BaseGroupSectionView(SectionView):
    """Shared section view for group sections"""

    @property
    def items(self):
        return []

    @property
    def groups(self):
        items = self.items
        size = self.context.group_size
        return [items[i : i + size] for i in range(0, len(items), size)]

    @property
    def item_lead_image_scale(self):
        layout = self.context.getLayout()
        group_size = self.context.group_size
        cols = 12 / group_size
        if layout == "list_view":
            return "thumb"
        if cols > 6:
            return "huge"
        elif cols > 3:
            return "large"
        return "preview"


class BaseLinksSectionView(BaseGroupSectionView):
    """Shared section view for link type sections"""

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
