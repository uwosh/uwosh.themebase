
import uwosh
import legacy

#uwosh.theme = legacy


def initialize(context):
    """
    
    """
    from Products.CMFCore import DirectoryView

    # This is required.
    # For some reason you cannot register a skin
    # directory for a non-theme product through
    # zcml
    DirectoryView.registerDirectory('skins', globals())