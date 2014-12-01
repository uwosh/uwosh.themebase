import unittest
#from uwosh.requirements.tests.base import UWOshRequirementsTestCase
from Products.CMFCore.utils import getToolByName
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.component import getUtility

class TestSetup(UWOshRequirementsTestCase):
    """
    
    """
    
    def test_actionicon(self):
        ai = getToolByName(self.portal, 'portal_actionicons')
        iconInfo = ai.getActionInfo('controlpanel', 'uwosh.themebase.controlpanel.icon')
        
        self.assertEquals('uwosh theme control panel icon', iconInfo[0])
        self.assertEquals('product_icon.gif', iconInfo[2])
        
    def test_controlpanel_item_installed(self):
        cp = getToolByName(self.portal, 'portal_controlpanel')
        productsConfiglets = cp.enumConfiglets(group="Products")
        
        #not working...
        #self.failUnless('uwosh.requirements.configlet' in productsConfiglets )

    def test_default_css_added(self):
        pcss = getToolByName(self.portal, 'portal_css')
        
        self.failUnless('++resource++uwosh.themebase.styles/default.css' in [css.getId() for css in pcss.getResources()])
        
    def test_orange_css_added(self):
        pcss = getToolByName(self.portal, 'portal_css')

        self.failUnless('++resource++uwosh.themebase.styles/orange.css' in [css.getId() for css in pcss.getResources()])
        
    def test_red_css_added(self):
        pcss = getToolByName(self.portal, 'portal_css')

        self.failUnless('++resource++uwosh.themebase.styles/red.css' in [css.getId() for css in pcss.getResources()])
        
    def test_black_css_added(self):
        pcss = getToolByName(self.portal, 'portal_css')

        self.failUnless('++resource++uwosh.themebase.styles/black.css' in [css.getId() for css in pcss.getResources()])
        
    def test_blue_css_added(self):
        pcss = getToolByName(self.portal, 'portal_css')

        self.failUnless('++resource++uwosh.themebase.styles/blue.css' in [css.getId() for css in pcss.getResources()])
        
    def test_acs_css_added(self):
        pcss = getToolByName(self.portal, 'portal_css')

        self.failUnless('++resource++uwosh.themebase.styles/acs.css' in [css.getId() for css in pcss.getResources()])
        
    def test_banner_viewlet_added(self):
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portaltop"

        storage = getUtility(IViewletSettingsStorage)
        skinname = self.portal.getCurrentSkinName()
        
        self.failUnless('uwosh.themebase.banner' in storage.getOrder(manager, skinname))
        
    def test_banner_viewlet_shown(self):
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portaltop"

        storage = getUtility(IViewletSettingsStorage)
        skinname = self.portal.getCurrentSkinName()
        
        self.failUnless('uwosh.themebase.banner' not in storage.getHidden(manager, skinname))
        
    def test_footer_viewlet_added(self):
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"

        storage = getUtility(IViewletSettingsStorage)
        skinname = self.portal.getCurrentSkinName()

        self.failUnless('uwosh.themebase.footer' in storage.getOrder(manager, skinname))

    def test_footer_viewlet_shown(self):
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"

        storage = getUtility(IViewletSettingsStorage)
        skinname = self.portal.getCurrentSkinName()

        self.failUnless('uwosh.themebase.footer' not in storage.getHidden(manager, skinname))
        
    def test_plone_footer_viewlet_hidden(self):
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"

        storage = getUtility(IViewletSettingsStorage)
        skinname = self.portal.getCurrentSkinName()

        self.failUnless('plone.footer' in storage.getHidden(manager, skinname))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite