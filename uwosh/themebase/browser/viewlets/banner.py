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

class Banner(ViewletBase):
    render = ViewPageTemplateFile('banner_viewlet.pt')

    def update(self):
        super(Banner, self).update()
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')

        props = getToolByName(self.context, 'portal_properties')
        self.livesearch = props.site_properties.getProperty('enable_livesearch', False)
        self.search_campus = props.site_properties.getProperty('search_campus_by_default', True)
        
        if self.livesearch:
            self.search_input_id = "searchGadget"
        else:
            self.search_input_id = ""

        folder = context_state.folder()
        self.folder_path = '/'.join(folder.getPhysicalPath())

        self.audience_navigation = context_state.actions().get('audience_navigation', None)
        
        #depreciated things...
        self.top_level_navigation = []
        
    def random_image_js(self):
        """
        deprecated
        """
        return None
        
    def selected(self, url):
        """
        The idea behind this is that this url is going to be the same
        across all sites.  So we're unsure if it is selected
        """
        return self.context.absolute_url().strip().startswith(url.strip())
        
        