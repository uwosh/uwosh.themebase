from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from uwosh.themebase.utils import getProperties
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from datetime import datetime
from Acquisition import aq_self

class Colophon(ViewletBase):

    render = ViewPageTemplateFile('colophon_viewlet.pt')

    def update(self):
        super(Colophon, self).update()
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        
        portal_root = self.portal_state.portal()
        self.copyright_holder = getattr(self.context, 'copyright_holder', None)
        self.help_url = getattr(self.context, 'uwosh_help_url', None)
        
        member = portal_root.portal_membership.getAuthenticatedMember()
        
        if member:
            self.simple_emergency_installed = portal_root.portal_quickinstaller.isProductInstalled('uwosh.simpleemergency')
            self.can_edit_simple_emergency = member.has_role(
                ['uwosh.simpleemergency: Emergency Message Manager', 
                 'Manager', 
                 'Owner'
                ]
            )
            self.has_manager_role = member.has_role(['Manager'])
        
        self.current_year = datetime.now().year

        
