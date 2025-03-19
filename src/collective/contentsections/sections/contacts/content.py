from zope.interface import implementer

from collective.contentsections import _
from collective.contentsections.sections.base import IBaseGroupSection
from collective.contentsections.sections.base import Section


class IContactsSection(IBaseGroupSection):
    """ContactsSection schema"""


@implementer(IContactsSection)
class ContactsSection(Section):
    """ContactsSection content type"""
