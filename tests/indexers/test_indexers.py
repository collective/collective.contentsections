# from bs4 import BeautifulSoup
# from plone import api

import pytest


class TestIndexers:
    @pytest.fixture(autouse=True)
    def _init(self, portal, contents):
        self.portal = portal
        self.contents = contents

    def test_searchabletext(self, contents):
        """ """
        # page = api.content.get(path="/plone/basic-page-1")
        # searchabletext = page.SearchableText()
        # TODO : check why the indexer is not called
