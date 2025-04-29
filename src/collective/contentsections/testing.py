from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import collective.contentsections  # noQA
import collective.geolocationbehavior  # noQA
import collective.taxonomy  # noQA
import collective.z3cform.datagridfield  # noQA


class Layer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.contentsections)
        self.loadZCML(package=collective.z3cform.datagridfield)
        self.loadZCML(package=collective.taxonomy)
        self.loadZCML(package=collective.geolocationbehavior)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.contentsections:default")


FIXTURE = Layer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="collective.contentsectionsLayer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="collective.contentsectionsLayer:FunctionalTesting",
)
