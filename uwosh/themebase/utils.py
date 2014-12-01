from zope.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
#from uwosh.core.utils import *
from zope.i18nmessageid import MessageFactory
mf = MessageFactory('uwosh.themebase')

def getProperties():
    return retrieve('uwosh_theme_properties').properties
