from collective.contentsections.testing import ACCEPTANCE_TESTING
from collective.contentsections.testing import FUNCTIONAL_TESTING
from collective.contentsections.testing import INTEGRATION_TESTING
from plone import api
from pytest_plone import fixtures_factory

# from collective.geolocationbehavior.geolocation import IGeolocatable
from collective.contentsections.contents.location.content import ILocation
import pytest

pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (ACCEPTANCE_TESTING, "acceptance"),
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)


@pytest.fixture
def contents(portal) -> list:
    """Create test contents."""
    response = {}
    with api.env.adopt_roles(
        [
            "Manager",
        ]
    ):

        response = []

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

        news_page = api.content.create(
            container=portal,
            type="collective.contentsections.NewsPage",
            title="News page 1",
        )

        cards_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.CardsSection",
            title="A cards section",
        )

        collection_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.CollectionSection",
            title="A collection section",
        )

        contacts_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.ContactsSection",
            title="A contacts section",
        )

        contact1 = api.content.create(
            container=contacts_section,
            type="collective.contentsections.Contact",
            title="A contact",
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
        )

        html_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.HTMLSection",
            title="A html section",
        )

        links_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.LinksSection",
            title="A links section",
        )

        link1 = api.content.create(
            container=links_section,
            type="Link",
            title="A link",
        )

        locations_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.LocationsSection",
            title="A locations section",
        )

        location1 = api.content.create(
            container=locations_section,
            type="collective.contentsections.Location",
            title="A location",
        )
        ILocation(location1).latitude = 4.719721850208658
        ILocation(location1).longitude = 50.498973213459514
        # __import__("pdb").set_trace()
        # location1.geolocation.longitude = 50.498973213459514
        # location1.geolocation.latitude = 4.719721850208658
        location1.reindexObject(idxs=["latitude", "longitude"])

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
        )

        images_section = api.content.create(
            container=basic_page,
            type="collective.contentsections.ImagesSection",
            title="An images section",
        )

        image1 = api.content.create(
            container=images_section,
            type="Image",
            title="An image",
        )

        for content in [
            basic_page,
            event_page,
            news_page,
            cards_section,
            collection_section,
            contact1,
            contacts_section,
            files_section,
            html_section,
            links_section,
            location1,
            locations_section,
            selection_section,
            text_section,
            file1,
            images_section,
            image1,
            link1,
        ]:
            response.append(content.UID())
    return response


@pytest.fixture
def content(contents) -> dict:
    """Return one content item."""
    content_uid = [key for key in contents.keys()][0]
    brains = api.content.find(UID=content_uid)
    # __import__("pdb").set_trace()
    return brains[0].getObject()
