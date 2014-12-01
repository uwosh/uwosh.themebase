from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from uwosh.themebase.utils import getProperties
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from plone.memoize.instance import memoize

class PathBar(ViewletBase):
    render = ViewPageTemplateFile('pathbar.pt')

    def update(self):
        super(PathBar, self).update()
        
        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        self.should_display = True
        
        if context_state.is_portal_root():
            self.should_display = False
            return
        
        self.navigation_root_url = self.portal_state.navigation_root_url()

        breadcrumbs_view = getMultiAdapter((self.context, self.request),
                                           name='breadcrumbs_view')
                                           
        self.breadcrumbs = breadcrumbs_view.breadcrumbs()
