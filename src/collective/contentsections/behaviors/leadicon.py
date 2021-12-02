# -*- coding: utf-8 -*-
from collective.contentsections import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class ILeadIcon(Interface):
    "Marker interface"


@provider(IFormFieldProvider)
class ILeadIconBehavior(model.Schema):

    icon = schema.Choice(
        title=_("Lead Icon"),
        required=False,
        vocabulary="collective.contentsections.LeadIcons",
    )


@implementer(ILeadIconBehavior)
@adapter(IDexterityContent)
class LeadIcon(object):
    def __init__(self, context):
        self.context = context

    @property
    def icon(self):
        return self.context.icon

    @icon.setter
    def icon(self, value):
        self.context.icon = value
