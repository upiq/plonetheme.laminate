# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.laminate.testing import PLONETHEME_LAMINATE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.laminate is properly installed."""

    layer = PLONETHEME_LAMINATE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.laminate is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.laminate'))

    def test_browserlayer(self):
        """Test that IPlonethemeLaminateLayer is registered."""
        from plonetheme.laminate.interfaces import (
            IPlonethemeLaminateLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeLaminateLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_LAMINATE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.laminate'])

    def test_product_uninstalled(self):
        """Test if plonetheme.laminate is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.laminate'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeLaminateLayer is removed."""
        from plonetheme.laminate.interfaces import \
            IPlonethemeLaminateLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeLaminateLayer, utils.registered_layers())
