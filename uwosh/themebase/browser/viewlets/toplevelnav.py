from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from uwosh.themebase.utils import getProperties
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from plone.memoize.instance import memoize

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the vielwet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p

class TopLevelNav(ViewletBase):
    render = ViewPageTemplateFile('toplevelnav_viewlet.pt')

    def update(self):
        super(TopLevelNav, self).update()
        
        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        actions = context_state.actions()
        self.top_level_navigation = actions.get('top_level_navigation', None)
        
        self.titan_services = actions.get('titan_services', [])
        
        if len(self.titan_services) > 0:
            self.has_titan_services = True
        else:
            self.has_titan_services = False
        