from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from uwosh.themebase.utils import getProperties
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
import math
from datetime import date

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

class Footer(ViewletBase):

    render = ViewPageTemplateFile('footer_viewlet.pt')

    def update(self):
        super(Footer, self).update()
        self.year = date.today().year

    # def update(self):
    #     super(Footer, self).update()
        # context_state = getMultiAdapter((self.context, self.request),
        #                                 name=u'plone_context_state')

        # links = context_state.actions().get('audience_navigation', [])
        # links.extend(context_state.actions().get('top_level_navigation', []))
        
        # #get three columns with the correct amount of columns in each...
        # size = len(links)
        # first_pivot = int(math.ceil(float(size)/3))
        # second_pivot = int(math.ceil(float(size-first_pivot)/2)) + first_pivot
        
        # self.link_sets = [
        #     links[:first_pivot],
        #     links[first_pivot:second_pivot],
        #     links[second_pivot:]
        # ]
        
