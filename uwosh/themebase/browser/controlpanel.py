from zope.interface import Interface, implements
from zope.component import adapts
from zope.formlib import form
from zope.schema import Choice
from zope.component import getMultiAdapter

from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from zope.component import getUtility
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from plone.app.controlpanel.form import ControlPanelForm
from zope.app.component.hooks import getSite
from uwosh.themebase.utils import getProperties, mf as _
from Products.CMFCore.utils import getToolByName
from uwosh.themebase.config import *
from uwosh.themebase.vocabularies import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from zope.schema.vocabulary import SimpleVocabulary
from Products.ATContentTypes.interface import IATFolder

class IThemeSchema(Interface):
    """
    Combined schema for the adapter lookup.
    """

#    image_folder = Choice(
#        title=_(u"Folder that holds all the rotating images"),
#        description=_(u"Find the content item in which you only want to search in"),
#        required=True,
#        source=SearchableTextSourceBinder({'object_provides' : IATFolder.__identifier__}, default_query='path:')
#    ) 

class ThemeControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IThemeSchema)

    def __init__(self, context):
        super(ThemeControlPanelAdapter, self).__init__(context)
        self.properties = getProperties()
    
    def get_image_folder(self):
        return self.properties.image_folder 
        
    def set_image_folder(self, value):
        self.properties.image_folder = value
    
    image_folder = property(get_image_folder, set_image_folder)            
    
class UWOshThemeConfigurationForm(ControlPanelForm):

    form_fields = form.Fields(IThemeSchema)
#    form_fields['image_folder'].custom_widget = UberSelectionWidget
    
    description = _(u"This is where you can configure UW Oshkosh specific plone settings.")
    form_name = _(u"UW Oshkosh Theme Configuration")
    label = _(u"UW Oshkosh Settings")

    def __init__(self, context, request):
        ControlPanelForm.__init__(self, context, request)