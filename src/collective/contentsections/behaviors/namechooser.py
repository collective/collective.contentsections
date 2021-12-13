# -*- coding: utf-8 -*-

import uuid

from plone.app.content.interfaces import INameFromTitle
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


class INameFromUUID(Interface):
    """Marker interface to enable 'Name from uuid' behavior"""


@implementer(INameFromTitle)
@adapter(INameFromUUID)
class NameFromUUID(object):
    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        prefix = self.context.portal_type.split(".")[-1].lower()
        return f"{prefix}-{uuid.uuid4().hex}"
