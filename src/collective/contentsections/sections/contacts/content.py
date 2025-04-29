from collective.contentsections.sections.base import IBaseGroupSection
from collective.contentsections.sections.base import Section
from zope.interface import implementer


class IContactsSection(IBaseGroupSection):
    """ContactsSection schema"""


@implementer(IContactsSection)
class ContactsSection(Section):
    """ContactsSection content type"""
