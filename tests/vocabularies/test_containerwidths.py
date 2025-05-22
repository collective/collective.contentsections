from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabContainerWidths:
    name = "collective.contentsections.ContainerWidths"

    @pytest.fixture(autouse=True)
    def _vocab(self, get_vocabulary, portal):
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "token,title",
        [
            [12, "Container 100%"],
            [8, "Container 66%"],
            [6, "Container 50%"],
            [0, "Window 100%"],
        ],
    )
    def test_container_widths(self, token, title):
        term = self.vocab.getTerm(token)
        assert title == term.title
