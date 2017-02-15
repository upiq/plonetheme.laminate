# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.laminate


class PlonethemeLaminateLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.laminate)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.laminate:default')


PLONETHEME_LAMINATE_FIXTURE = PlonethemeLaminateLayer()


PLONETHEME_LAMINATE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_LAMINATE_FIXTURE,),
    name='PlonethemeLaminateLayer:IntegrationTesting'
)


PLONETHEME_LAMINATE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_LAMINATE_FIXTURE,),
    name='PlonethemeLaminateLayer:FunctionalTesting'
)


PLONETHEME_LAMINATE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_LAMINATE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeLaminateLayer:AcceptanceTesting'
)
