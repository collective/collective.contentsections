from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabLeadIcons:
    name = "collective.contentsections.LeadIcons"

    @pytest.fixture(autouse=True)
    def _vocab(self, get_vocabulary, portal):
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "key,record",
        [
            ["0-circle", "Bootstrap Icon 0-circle"],
            ["0-circle-fill", "Bootstrap Icon 0-circle-fill"],
            ["0-square", "Bootstrap Icon 0-square"],
            ["0-square-fill", "Bootstrap Icon 0-square-fill"],
            ["zoom-in", "Bootstrap Icon zoom-in"],
            ["zoom-out", "Bootstrap Icon zoom-out"],
        ],
    )
    def test_column_alignments(self, key, record):
        term = self.vocab.getTerm(key)
        assert term.title == record
