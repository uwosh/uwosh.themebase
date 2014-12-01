from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from uwosh.themebase.utils import getProperties
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager

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

class MainImage(ViewletBase):
    render = ViewPageTemplateFile('mainimage_viewlet.pt')

    def update(self):
        super(MainImage, self).update()
        
        #XXX the order in which these are called is important!
        self.images = self.get_images()
        self.image_urls = self.get_image_urls()
        self.javascript = self.random_image_js()
        self.hasImages = len(self.images) > 0
        
    def get_min_height(self):
        """
        Right now if you don't set the min-height on the container,
        it does a little jarring when the js sets the image.
        So this prevents it....
        """
        if not self.hasImages:
            return 0
        else:
            height = self.images[0].getHeight()
            for image in self.images[1:]:
                im_height = image.getHeight()
                if im_height < height:
                    height = im_height
                    
            return height
        
    def style(self):
        return 'min-height:%spx' % self.get_min_height()
        
    def random_image_js(self):
        """
        only reason we're doing it this way is because if the page is cached, you'll never get a new image to show....
        still shows image if user does not have js
        could just do it the easy way and not do it through js.  The page will be cached so the image won't be
        rotated as often--might not be a problem since they hardly ever have more than one image in there anyway...
        """
        return """
            <script type="text/javascript">
                var image_urls = [%s];
                jq('#mainImage').append("<img alt='generic banner image' src='" + image_urls[Math.floor(Math.random()*image_urls.length)] + "' />");
            </script>
        """ % (
            ','.join(map(lambda x: '"' + x + '"', self.image_urls))
        )
        
    def get_images(self):
        try:
            image_folder = self.context.unrestrictedTraverse('main-images')
        except:
            return []

        return [image_folder[id] for id in image_folder.objectIds() if image_folder[id].portal_type == "Image"]
        
    def get_image_urls(self):
        if hasattr(self, 'images') and type(self.images) == list:
            return [image.absolute_url() for image in self.images]
        else:
            return []
