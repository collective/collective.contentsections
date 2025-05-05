from bs4 import BeautifulSoup
from plone import api

import pytest


class TestPageView:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_base_page_view(self, contents):
        """Test the base_page_view."""
        page = api.content.get(path="/plone/basic-page-1")
        view = api.content.get_view(
            name="page_view",
            context=page,
        )

        soup = BeautifulSoup(view(), "html.parser")

        # Check basic attributes
        assert soup.find("title").text == "Basic page 1 — Plone site"
        assert soup.find("h1").text == "Basic page 1"
        assert soup.find(id="portal-logo").get("href") == "http://nohost/plone"

        # Cards section
        cards_section = soup.find("div", id="section-a-cards-section")
        cards = cards_section.find_all("div", class_="card")
        assert len(cards) == 2
        assert cards[0].find("p").text == "a news page in a card !"
        assert cards[1].find("a").get("href") == "http://nohost/plone/event-page-1"

        # Collection section
        collection_section = soup.find("div", id="section-a-collection-section")
        assert collection_section.find("h2").text == "A collection section"
        collections = collection_section.find_all("div", class_="card")
        assert len(collections) == 3
        assert collections[2].find("a").get("href") == "http://nohost/plone/news-page-3"
        section_more = collection_section.find("div", class_="section-more-link")
        assert (
            section_more.find("a").get("href")
            == "http://nohost/plone/a-newspage-collection"
        )
        assert section_more.find("a").text == "See the collection"

        # Contacts section
        contacts_section = soup.find("div", id="section-a-contacts-section")
        assert contacts_section.find("h2").text == "A contacts section"
        contact1 = contacts_section.find("div", class_="card").prettify()
        contact1_html = """
            <div class="card text-center h-100">
            <div class="card-body">
            <h4 class="card-title">
            <span class="d-block">A contact</span>
            <span class="d-block fs-5">A contact subtitle</span>
            </h4>
            <p class="card-text">
            <a class="d-block" href="tel:+3223456789">+3223456789</a>
            <a class="d-block" href="mailto:a@contact.be">a@contact.be</a>
            </p>
            <p class="card-text">A contact description</p>
            </div>
            </div>
        """
        assert contact1 == BeautifulSoup(contact1_html, "html.parser").prettify()

        # File section
        files_section = soup.find("div", id="section-a-files-section")
        assert files_section.find("h2").text == "A files section"
        file1 = files_section.find("article")
        assert (
            file1.find("a").get("href")
            == "http://nohost/plone/basic-page-1/a-files-section/a-file"
        )
        # HTML section
        html_section = soup.find("div", id="section-a-html-section")
        assert html_section.find("h2").text == "A html section"
        assert html_section.find("iframe").get("src") == "https://www.imio.be"

        # Images section
        images_section = soup.find("div", id="section-an-images-section")
        assert len(images_section.find_all("img")) == 3
        assert (
            images_section.find_all("img")[1].get("src")
            == "http://nohost/plone/basic-page-1/an-images-section/another-image/@@images/image/large"
        )

        # Links section
        links_section = soup.find("div", id="section-a-links-section")
        assert links_section.find("h2").text == "A links section"
        links = links_section.find_all("div", class_="card")
        assert len(links) == 3
        assert links[0].find("a").get("href") == "https://www.imio.be"
        assert links[1].find("a").get("href") == "https://www.plone.org"
        assert links[2].find("a").get("href") == "http://nohost/plone/event-page-1"

        # Locations section
        locations_section = soup.find("div", id="section-a-locations-section")
        assert locations_section.find("h2").text == "A locations section"
        patleaflet_html = """
        <div class="pat-leaflet" data-geojson='{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"color": "blue", "popup": "&lt;div&gt;&lt;div&gt;&lt;h5&gt;A location&lt;/h5&gt;&lt;/div&gt;&lt;/div&gt;"}, "geometry": {"type": "Point", "coordinates": [50.498973213459514, 4.719721850208658]}}, {"type": "Feature", "properties": {"color": "blue", "popup": "&lt;div&gt;&lt;div&gt;&lt;h5&gt;Another location&lt;/h5&gt;&lt;/div&gt;&lt;/div&gt;"}, "geometry": {"type": "Point", "coordinates": [39.95990378037637, -86.01869422272952]}}]}' data-pat-leaflet='{"fullscreencontrol": true, "zoomcontrol": true, "zoom": 10, "latitude": -40.64948618626043, "longitude": 45.22943849691794}'></div>
        """
        assert (
            locations_section.find("div", class_="pat-leaflet").prettify()
            == BeautifulSoup(patleaflet_html, "html.parser").prettify()
        )

        # Selection section
        selection_section = soup.find("div", id="section-a-selection-section")
        assert selection_section.find("h2").text == "A selection section"
        selection1 = selection_section.find("div", class_="card")
        assert selection1.find("a").get("href") == "http://nohost/plone/event-page-1"

        # Text section
        text_section = soup.find("div", id="section-a-text-section")
        assert text_section.find("h2").text == "A text section"
        assert text_section.find("p").text == "This is a text section!"
