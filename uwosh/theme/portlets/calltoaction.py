#XXX Legacy!!! Remove at your own risk!!!
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

class ICallToAction(IPortletDataProvider):

    actions = schema.List(
        title = _(u"Call To Action"),
        description = _(u"""Specify each "Call To Action" on a line with the name and url separated by a "|".  
                            For example, "Link To Google|http://www.google.com" You can even add html in the name portion.
                            An example of one with html would be, "Check out this<br />Special Thing | http://www.google.com" """),
        required = True,
        value_type=schema.TextLine(
            title=_(u"Call to action"),
            constraint=re.compile(".*\|.*").match
        )
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
        return [action.split('|') for action in self.data.actions]

class AddForm(base.AddForm):
    form_fields = form.Fields(ICallToAction)
    
    label = _(u"Add Call To Action")
    description = _(u"This portlet allows you to add call to actions.")

    def create(self, data):
        return Assignment(actions = data.get('actions', []))

class EditForm(base.EditForm):
    form_fields = form.Fields(ICallToAction)
    
    label = _(u"Edit Call To Action")
    description = _(u"This portlet allows you to add call to actions.")
