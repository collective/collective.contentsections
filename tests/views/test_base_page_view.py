from bs4 import BeautifulSoup
from plone import api

import pytest


class TestPageView:
    @pytest.fixture(autouse=True)
    def _init(self, portal, http_request, contents):
        self.portal = portal
        self.request = http_request
        self.contents = contents
        page = api.content.get(path="/plone/basic-page-1")
        view = api.content.get_view(
            name="page_view",
            context=page,
        )
        self.soup = BeautifulSoup(view(), "html.parser")

    def test_basic_attributes(self):
        """Test the basic attributes of the page."""
        assert self.soup.find("title").text == "Basic page 1 — Plone site"
        assert self.soup.find("h1").text == "Basic page 1"
        assert self.soup.find(id="portal-logo").get("href") == "http://nohost/plone"

    def test_card_section(self):
        cards_section = self.soup.find("div", id="section-a-cards-section")
        cards = cards_section.find_all("div", class_="card")
        assert len(cards) == 2
        assert cards[0].find("p").text == "a news page in a card !"
        assert cards[1].find("a").get("href") == "http://nohost/plone/event-page-1"

    def test_collection_section(self):
        collection_section = self.soup.find("div", id="section-a-collection-section")
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

    def test_contacts_section(self):
        contacts_section = self.soup.find("div", id="section-a-contacts-section")
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

    def test_files_section(self):
        files_section = self.soup.find("div", id="section-a-files-section")
        assert files_section.find("h2").text == "A files section"
        file1 = files_section.find("article")
        assert (
            file1.find("a").get("href")
            == "http://nohost/plone/basic-page-1/a-files-section/a-file"
        )

    def test_html_section(self):
        # HTML section
        html_section = self.soup.find("div", id="section-a-html-section")
        assert html_section.find("h2").text == "A html section"
        assert html_section.find("iframe").get("src") == "https://www.imio.be"

    def test_images_section(self):
        images_section = self.soup.find("div", id="section-an-images-section")
        assert len(images_section.find_all("img")) == 3
        assert (
            images_section.find_all("img")[1].get("src")
            == "http://nohost/plone/basic-page-1/an-images-section/another-image/@@images/image/large"
        )

    def test_links_section(self):
        links_section = self.soup.find("div", id="section-a-links-section")
        assert links_section.find("h2").text == "A links section"
        links = links_section.find_all("div", class_="card")
        assert len(links) == 3
        assert links[0].find("a").get("href") == "https://www.imio.be"
        assert links[1].find("a").get("href") == "https://www.plone.org"
        assert links[2].find("a").get("href") == "http://nohost/plone/event-page-1"
        assert (
            links[0].find("img", class_="card-img-top").get("src")
            == "http://nohost/plone/basic-page-1/a-links-section/a-link/@@images/image/huge"
        )
        links_section2 = self.soup.find("div", id="section-another-links-section")
        links2 = links_section2.find_all("div", class_="card")
        assert (
            links2[0].find("img", class_="card-img-top").get("src")
            == "http://nohost/plone/basic-page-1/another-links-section/a-link-in-another-section/@@images/image/preview"
        )

    def test_locations_section(self):
        locations_section = self.soup.find("div", id="section-a-locations-section")
        assert locations_section.find("h2").text == "A locations section"
        patleaflet_html = """
        <div class="pat-leaflet" data-geojson='{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"color": "blue", "popup": "&lt;div&gt;&lt;div&gt;&lt;h5&gt;A location&lt;/h5&gt;&lt;/div&gt;&lt;/div&gt;"}, "geometry": {"type": "Point", "coordinates": [50.498973213459514, 4.719721850208658]}}, {"type": "Feature", "properties": {"color": "blue", "popup": "&lt;div&gt;&lt;div&gt;&lt;h5&gt;Another location&lt;/h5&gt;&lt;/div&gt;&lt;/div&gt;"}, "geometry": {"type": "Point", "coordinates": [39.95990378037637, -86.01869422272952]}}]}' data-pat-leaflet='{"fullscreencontrol": true, "zoomcontrol": true, "zoom": 10, "latitude": -40.64948618626043, "longitude": 45.22943849691794}'></div>
        """
        assert (
            locations_section.find("div", class_="pat-leaflet").prettify()
            == BeautifulSoup(patleaflet_html, "html.parser").prettify()
        )

    def test_selection_section(self):
        selection_section = self.soup.find("div", id="section-a-selection-section")
        assert selection_section.find("h2").text == "A selection section"
        selection1 = selection_section.find("div", class_="card")
        assert selection1.find("a").get("href") == "http://nohost/plone/event-page-1"

    def test_text_section(self):
        text_section = self.soup.find("div", id="section-a-text-section")
        assert text_section.find("h2").text == "A text section"
        assert text_section.find("p").text == "This is a text section!"
