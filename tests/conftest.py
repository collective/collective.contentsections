from collective.contentsections.testing import FUNCTIONAL_TESTING
from collective.contentsections.testing import INTEGRATION_TESTING
from plone import api
from plone.app.textfield.value import RichTextValue
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.namedfile.file import NamedBlobFile
from plone.namedfile.file import NamedBlobImage
from pytest_plone import fixtures_factory
from z3c.relationfield import RelationValue
from zope.component import getUtility
from zope.intid.interfaces import IIntIds

import base64
import pytest


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)

BEHAVIOR = "collective.contentsections.leadicon"


CONTENT_TYPES = [
    "collective.contentsections.BasicPage",
    "collective.contentsections.Contact",
    "collective.contentsections.EventPage",
    "collective.contentsections.Location",
    "collective.contentsections.NewsPage",
    "collective.contentsections.TextSection",
    "Folder",
    "File",
    "Image",
    "Link",
]


@pytest.fixture
def contents(portal, get_fti) -> dict:
    """Create test contents."""
    response = {}
    with api.env.adopt_roles(
        [
            "Manager",
        ]
    ):

        # enable collective.contentsections.leadicon behavior for some content types
        for content_type in CONTENT_TYPES:
            fti = get_fti(content_type)
            if BEHAVIOR not in fti.behaviors:
                fti.behaviors = fti.behaviors + (BEHAVIOR,)

        collection_query = [
            {
                "i": "path",
                "o": "plone.app.querystring.operation.string.relativePath",
                "v": "..::1::1",
            },
            {
                "i": "portal_type",
                "o": "plone.app.querystring.operation.selection.any",
                "v": ["collective.contentsections.NewsPage"],
            },
        ]

        collection1 = api.content.create(
            container=portal,
            type="Collection",
            title="A newspage collection",
            description="A collection gathering newspages",
            query=collection_query,
        )
        basic_page = api.content.create(
            container=portal,
            type="collective.contentsections.BasicPage",
            title="Basic page 1",
        )

        event_page = api.content.create(
            container=portal,
            type="collective.contentsections.EventPage",
            title="Event page 1",
        )

        news_page_1 = api.content.create(
            container=portal,
            type="collective.contentsections.NewsPage",
            title="News page 1",
        )

        news_page_2 = api.content.create(
            container=portal,
            type="collective.contentsections.NewsPage",
            title="News page 2",
        )

        news_page_3 = api.content.create(
            container=portal,
            type="collective.contentsections.NewsPage",
            title="News page 3",
        )

        cards_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.CardsSection",
            title="A cards section",
        )
        cards_section.cards = [
            {
                "description": "a news page in a card !",
                "icon": "0-circle-fill",
                "relation_uid": news_page_1.UID(),
                "subtitle": "card subtitle is here",
                "title": "A card",
            },
            {
                "description": "an event page in a card !",
                "icon": "backpack3-fill",
                "relation_uid": event_page.UID(),
                "subtitle": "another card subtitle is here",
                "title": "Another card",
            },
        ]

        collection_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.CollectionSection",
            title="A collection section",
            collection_link_text="See the collection",
        )

        intids = getUtility(IIntIds)
        collection_section.collection = RelationValue(intids.getId(collection1))
        collection_section.reindexObject()

        contacts_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.ContactsSection",
            title="A contacts section",
            description="A contacts section description",
        )

        contact1 = api.content.create(
            container=contacts_section,
            type="collective.contentsections.Contact",
            title="A contact",
            subtitle="A contact subtitle",
            phone="+3223456789",
            email="a@contact.be",
            description="A contact description",
        )

        files_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.FilesSection",
            title="A files section",
        )

        file1 = api.content.create(
            container=files_section,
            type="File",
            title="A file",
            file=NamedBlobFile(
                data="This is a test file",
                contentType="application/text",
                filename="test.txt",
            ),
        )

        html_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.HTMLSection",
            title="A html section",
            html='<iframe src="https://www.imio.be"></iframe>',
        )

        links_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.LinksSection",
            title="A links section",
            group_size=1,
        )

        link1 = api.content.create(
            container=links_section,
            type="Link",
            title="A link",
            remoteUrl="https://www.imio.be",
            description="A link description",
        )

        link2 = api.content.create(
            container=links_section,
            type="Link",
            title="Another link",
            remoteUrl="https://www.plone.org",
            description="Another link description",
        )

        link3 = api.content.create(
            container=links_section,
            type="Link",
            title="A link with resolveuid",
            remoteUrl=f"http://nohost/plone/resolveuid/{api.content.get_uuid(obj=event_page)}",
        )

        links_section2 = api.content.create(
            container=basic_page,
            type="collective.contentsections.LinksSection",
            title="Another links section",
            group_size=6,
        )

        link4 = api.content.create(
            container=links_section2,
            type="Link",
            title="A link in another section",
            remoteUrl="https://www.github.com/collective/collective.contentsections",
        )

        empty_locations_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.LocationsSection",
            title="An empty locations section",
        )

        locations_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.LocationsSection",
            title="A locations section",
            initial_zoom_level=10,
        )

        location1 = api.content.create(
            container=locations_section,
            type="collective.contentsections.Location",
            title="A location",
        )
        location1.geolocation = Geolocation(
            latitude=4.719721850208658,
            longitude=50.498973213459514,
        )

        location1.reindexObject()

        location2 = api.content.create(
            container=locations_section,
            type="collective.contentsections.Location",
            title="Another location",
        )
        location2.geolocation = Geolocation(
            latitude=-86.01869422272952,
            longitude=39.95990378037637,
        )

        location2.reindexObject()

        selection_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.SelectionSection",
            title="A selection section",
        )

        api.relation.create(
            source=selection_section, target=event_page, relationship="relations"
        )

        text_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.TextSection",
            title="A text section",
            text=RichTextValue(
                "<p>This is a text section!</p>", "text/html", "text/x-html-safe"
            ),
        )

        images_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.ImagesSection",
            title="An images section",
        )

        image1_b64 = (
            "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAADUlEQVR4nGP4DwQMDAAAAFAA"
            "BaL95YQAAAAASUVORK5CYII="
        )

        image2_b64 = (
            "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAADUlEQVR4nGP48f///wYABJ0C"
            "fbtgXRAAAAAASUVORK5CYII="
        )

        image3_base64 = (
            "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAADUlEQVR4nGPw4f///wYABJ4C"
            "fbxQ96QAAAAASUVORK5CYII="
        )

        image1 = api.content.create(
            container=images_section,
            type="Image",
            title="An image",
        )

        image2 = api.content.create(
            container=images_section,
            type="Image",
            title="Another image",
        )

        image3 = api.content.create(
            container=images_section,
            type="Image",
            title="A third image",
        )
        image1.image = NamedBlobImage(
            data=base64.b64decode(image1_b64),
            contentType="image/png",
            filename="image1.png",
        )
        image2.image = NamedBlobImage(
            data=base64.b64decode(image2_b64),
            contentType="image/png",
            filename="image2.png",
        )
        image3.image = NamedBlobImage(
            data=base64.b64decode(image3_base64),
            contentType="image/png",
            filename="image3.png",
        )
        image1.reindexObject()
        image2.reindexObject()
        image3.reindexObject()

        basic_page.reindexObject()

        catalog = api.portal.get_tool("portal_catalog")
        catalog.clearFindAndRebuild()

        for content in [
            basic_page,
            event_page,
            news_page_1,
            news_page_2,
            news_page_3,
            cards_section,
            collection1,
            collection_section,
            contact1,
            contacts_section,
            files_section,
            html_section,
            links_section,
            links_section2,
            locations_section,
            location1,
            selection_section,
            text_section,
            file1,
            images_section,
            image1,
            image2,
            image3,
            link1,
            link2,
            link3,
            link4,
            location1,
            location2,
            empty_locations_section,
        ]:
            response[content.UID()] = content.title
    return response
