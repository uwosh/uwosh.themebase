from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
import re
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

from plone.memoize.instance import memoize
from Acquisition import aq_inner
from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletDataProvider
from widgets import CallToActionWidget

class ICallToAction(IPortletDataProvider):

    actions = schema.List(
        title = _(u"Call To Action"),
        description = _(u""" """),
        required = True
    )

class Assignment(base.Assignment):
    implements(ICallToAction)

    def __init__(self, actions=[]):
        self.actions = actions
        
    @property
    def title(self):
        return "Call To Action"

class Renderer(base.Renderer):   
    render = ViewPageTemplateFile('calltoaction.pt')

    @memoize
    def call_to_actions(self):
        return self.data.actions

class AddForm(base.AddForm):
    form_fields = form.Fields(ICallToAction)
    form_fields['actions'].custom_widget = CallToActionWidget
    
    label = _(u"Add Call To Action")
    description = _(u"This portlet allows you to add call to actions.")

    def create(self, data):
        return Assignment(actions = data.get('actions', []))

class EditForm(base.EditForm):
    form_fields = form.Fields(ICallToAction)
    form_fields['actions'].custom_widget = CallToActionWidget
    
    label = _(u"Edit Call To Action")
    description = _(u"This portlet allows you to add call to actions.")
    
