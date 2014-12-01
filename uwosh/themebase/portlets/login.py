from plone.app.portlets.portlets import login
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Renderer(login.Renderer):

    render = ViewPageTemplateFile('login.pt')
