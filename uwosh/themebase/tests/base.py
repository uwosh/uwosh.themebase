import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

#import uwosh.default
    
from zope.app import zapi
from zope.configuration import xmlconfig
#from uwosh.core.utils.remoteservice import RemoteService


ztc.installProduct('uwosh.themebase')
ptc.setupPloneSite(products=('uwosh.themebase',))


class UWOshThemeTestCase(ptc.PloneTestCase):
    """
    Base Class for unit tests
    """
    
    
class UWOshThemeFunctionalTestCase(ptc.FunctionalTestCase):
    """
    Base class for functional integration tests 
    """