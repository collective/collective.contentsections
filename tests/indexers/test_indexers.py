from collective.contentsections.indexers import get_elements_title_and_description_terms
from collective.contentsections.indexers import get_title_and_description_terms
from collective.contentsections.sections import ISection
from plone import api
from zope.interface import alsoProvides

import pytest


class TestIndexers:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_get_title_and_description_terms(self):
        section = api.content.get(path="/plone/basic-page-1/a-contacts-section")
        assert get_title_and_description_terms(section) == [
            "A contacts section",
            "A contacts section description",
        ]

    def test_get_elements_title_and_description_terms(self):
        section = api.content.get(path="/plone/basic-page-1/a-links-section")
        link1 = api.content.get(path="/plone/basic-page-1/a-links-section/a-link")
        link2 = api.content.get(path="/plone/basic-page-1/a-links-section/another-link")
        alsoProvides(link1, ISection)
        alsoProvides(link2, ISection)
        assert get_elements_title_and_description_terms(section) == [
            "A link",
            "A link description",
            "Another link",
            "Another link description",
        ]
