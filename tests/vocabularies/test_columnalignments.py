# from plone import api
# from zope.schema.vocabulary import SimpleVocabulary

# import pytest


# class TestVocabAvailableRoles:
#     name = "collective.contentsections.ColumnAlignments"

#     @pytest.fixture(autouse=True)
#     def _vocab(self, get_vocabulary, portal):
#         self.vocab = get_vocabulary(self.name, portal)

#     def test_vocabulary(self):
#         assert self.vocab is not None
#         assert isinstance(self.vocab, SimpleVocabulary)

#     @pytest.mark.parametrize(
#         "token",
#         [
#             "member",
#             "student",
#         ],
#     )
#     def test_token(self, token):
#         assert token in [x for x in self.vocab.by_token]

#     @pytest.mark.parametrize(
#         "token,title",
#         [
#             ["member", "Team Member"],
#             ["student", "Student"],
#         ],
#     )
#     def test_token_title(self, token, title):
#         term = self.vocab.getTerm(token)
#         assert title == term.title
