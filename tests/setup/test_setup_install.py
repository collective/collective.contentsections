from collective.contentsections import PACKAGE_NAME
from plone import api


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if collective.contentsections is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IBrowserLayer is registered."""
        from collective.contentsections.interfaces import IBrowserLayer

        assert IBrowserLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "1000"

    def test_registry(self, portal):
        """Test registry"""
        registry = {
            "plone.default_page": "index",
            "plone.displayed_types": [
                "collective.contentsections.BasicPage",
                "collective.contentsections.EventPage",
                "collective.contentsections.NewsPage",
            ],
            "plone.types_not_searched": [
                "collective.contentsections.CardsSection",
                "collective.contentsections.CollectionSection",
                "collective.contentsections.Contact",
                "collective.contentsections.ContactsSection",
                "collective.contentsections.FilesSection",
                "collective.contentsections.HTMLSection",
                "collective.contentsections.ImagesSection",
                "collective.contentsections.LinksSection",
                "collective.contentsections.Location",
                "collective.contentsections.LocationsSection",
                "collective.contentsections.SelectionSection",
                "collective.contentsections.TextSection",
                "Image",
                "Link",
            ],
            "plone.default_page_types": [
                "collective.contentsections.BasicPage",
            ],
            "geolocation.default_latitude": "50.3343019",
            "geolocation.default_longitude": "4.9862176",
            "plone.bundles/collective-contentsections-base.enabled": "True",
            "plone.bundles/collective-contentsections-base.csscompilation": "++plone++collective.contentsections/base.css",
            "plone.bundles/collective-contentsections-base.jscompilation": "++plone++collective.contentsections/base.js",
            "plone.bundles/collective-contentsections-base.load_defer": "True",
            "plone.bundles/collective-contentsections-edit.enabled": "True",
            "plone.bundles/collective-contentsections-edit.csscompilation": "++plone++collective.contentsections/edit.css",
            "plone.bundles/collective-contentsections-edit.jscompilation": "++plone++collective.contentsections/edit.js",
            "plone.bundles/collective-contentsections-edit.load_defer": "True",
            "plone.bundles/collective-contentsections-edit.expression": "python: member is not None",
            "plone.icon.contenttype/collective-contentsections-basicpage": "++plone++bootstrap-icons/file-earmark-text.svg",
            "plone.icon.contenttype/collective-contentsections-cardssection": "++plone++bootstrap-icons/card-heading.svg",
            "plone.icon.contenttype/collective-contentsections-collectionsection": "++plone++bootstrap-icons/file-earmark-richtext.svg",
            "plone.icon.contenttype/collective-contentsections-contact": "++plone++bootstrap-icons/file-person.svg",
            "plone.icon.contenttype/collective-contentsections-contactssection": "++plone++bootstrap-icons/people.svg",
            "plone.icon.contenttype/collective-contentsections-eventpage": "++plone++bootstrap-icons/calendar-date.svg",
            "plone.icon.contenttype/collective-contentsections-filessection": "++plone++bootstrap-icons/file-pdf.svg",
            "plone.icon.contenttype/collective-contentsections-htmlsection": "++plone++bootstrap-icons/file-code.svg",
            "plone.icon.contenttype/collective-contentsections-imagessection": "++plone++bootstrap-icons/image.svg",
            "plone.icon.contenttype/collective-contentsections-linkssection": "++plone++bootstrap-icons/link.svg",
            "plone.icon.contenttype/collective-contentsections-location": "++plone++bootstrap-icons/geo.svg",
            "plone.icon.contenttype/collective-contentsections-locationssection": "++plone++bootstrap-icons/globe.svg",
            "plone.icon.contenttype/collective-contentsections-newspage": "++plone++bootstrap-icons/file-earmark-richtext.svg",
            "plone.icon.contenttype/collective-contentsections-selectionsection": "++plone++bootstrap-icons/list-check.svg",
            "plone.icon.contenttype/collective-contentsections-textsection": "++plone++bootstrap-icons/file-earmark-richtext.svg",
        }
        # TODO : test values in tinymce.xml
        for key, value in registry.items():
            if isinstance(value, list):
                for item in value:
                    assert item in str(api.portal.get_registry_record(key))
            else:
                assert value in str(api.portal.get_registry_record(key))
