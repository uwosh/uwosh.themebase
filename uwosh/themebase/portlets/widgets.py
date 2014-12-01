from zope.schema.interfaces import ValidationError
from zope.component import getMultiAdapter

from zope.app.form.interfaces import WidgetInputError
from zope.app.form.browser.interfaces import \
    ISourceQueryView, ITerms, IWidgetInputErrorView
from zope.app.form.browser.widget import SimpleInputWidget
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from plone.app.vocabularies.interfaces import IBrowsableTerm

class CallToActionWidget(SimpleInputWidget):
    
    template = ViewPageTemplateFile('calltoactionwidget.pt')

    def __init__(self, field, request):
        
        SimpleInputWidget.__init__(self, field, request)
        

    def checkedCallToActions(self):
        """
        for backwards compatibility
        """
        if len(self._data) > 0:
            if type(self._data[0]) == tuple:
                return self._data
            else:
                new_data = []
                for d in self._data:
                    split_data = d.split("|")
                    new_data = (split_data[0], split_data[1], split_data[2])
                return new_data
        else:
            return []        
        self._data

    def actions(self):
        if self.request.form.has_key('updateSelection') or self.request.form.has_key('addRow'):
            return self.getInputValue()
        
        if type(self._data) == list:
            return self.checkedCallToActions()
        else:
            return []

    def __call__(self):
        return self.template(self)

    def getInputValue(self):
        form = self.request.form
        value = []
        number_of_actions = int(form['numberofactions'])
        
        for i in range(0, number_of_actions):
            keyname = 'actionname-%s' % i
            keylink = 'actionlink-%s' % i
            
            if form.has_key(keyname) and form.has_key(keylink):
                name = form[keyname]
                link = form[keylink]
            
                if len(name) > 0 and len(link) > 0:
                    
                    if form.has_key('actiondelete-%s' % i) and form['actiondelete-%s' % i] == "on":
                        pass
                    else:
                        if form.has_key('actionnewwindow-%s' % i) and form['actionnewwindow-%s' % i] == "on":
                            newwindow = form[('actionnewwindow-%s' % i)]
                            value.append((name, link, newwindow))
                        else:
                            value.append((name, link, "off"))

        return value

    def hasInput(self):
        form = self.request.form
        
        res = [k for k in form.keys() if 'actioname' in k or 'actionlink' in k or 'newwindow' in k]
        
        return len(res) > 0
    
