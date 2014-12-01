from plone.memoize.instance import memoize

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.component import getMultiAdapter
from zLOG import LOG, WARNING
from Products.CMFCore.utils import getToolByName

class ManageLinks(BrowserView):
    """Manage rules in a the global rules container
    """
    
    template = ViewPageTemplateFile('managelinks.pt')
    errormsg = ""

    def __init__(self, request, context):
        super(ManageLinks, self).__init__(request, context)

    def __call__(self):
        self.select_portal_action = False
        self.select_portal_link = False
        self.edit_link = False
        
        if self.request.get('form.button.saveLink', None) is not None:
            self.saveLink()
        
        if self.request.get('action_id', None) is not None:
            if self.request.get('link_id', None) is not None:
                self.edit_link = True
            else:
                self.select_portal_link = True
        else:
            self.select_portal_action = True
            
        return self.template()
    
    def saveLink(self):
        pa = getToolByName(self.context, 'portal_actions')
        action = pa[self.request.get('action_id')][self.request.get('link_id')]
        
        action.manage_changeProperties(
            title=self.request.get('form.title'),
            url_expr='string: ' + self.request.get('form.url'),
            visible=self.request.get('form.visible') == 'on'
        )
        
    
    @memoize
    def portal_actions(self):
        
        return [('Top Level Navigation', 'top_level_navigation'), ('Audience Navigation', 'audience_navigation'), ('Titan Services', 'titan_services')]
        
    @memoize
    def get_links(self):
        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        return context_state.actions().get(self.request.get('action_id'), None)
        
    def get_link(self):
        pa = getToolByName(self.context, 'portal_actions')
        
        return pa[self.request.get('action_id')][self.request.get('link_id')]
        
