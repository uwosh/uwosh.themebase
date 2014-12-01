from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from plone.memoize.instance import memoize
from datetime import datetime
from Acquisition import aq_inner
from urllib import urlencode

class UWOshSearch(BrowserView):
    
    template = ViewPageTemplateFile('uwoshsearch.pt')

    def urlencodedGoogleSearch(self):
        return urlencode({
            'q' : self.request.get('SearchableText', self.request.get('q', "")),
            'cx' : '016914008736719096284:eascmls-b2u',
            'search_entire_campus' : "True"
        })

    def __call__(self):
        
        if self.request.form.has_key('search_entire_campus'):
            if self.request.form['search_entire_campus'] == 'on':
                #redirect on itself so we can get a unique search url to prevent caching
                self.request.response.redirect('uwosh-search?%s' % self.urlencodedGoogleSearch())
            else:
                return self.template()
            
        else:
            self.request.response.redirect('search?%s' % urlencode(self.request.form))