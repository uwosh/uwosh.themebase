from uwosh.themebase.utils import getProperties
from Products.CMFCore.utils import getToolByName
#from uwosh.core.utils import install

dependencies = [
#    'uwosh.default'
]

def setupVarious(context):

    if not context.readDataFile('uwosh.theme_various.txt'):
        return
        
    site = context.getSite()