from plone.app.vocabularies import catalog
from zope.interface import implements

class SearchableTextSourceBinder(catalog.SearchableTextSourceBinder):
    """
    Not used anymore
    """
    
    implements(catalog.IContextSourceBinder)
        
    def __call__(self, context):
        return catalog.SearchableTextSource(
            context.context, 
            base_query=self.query.copy(),
            default_query=self.default_query
        )
    
