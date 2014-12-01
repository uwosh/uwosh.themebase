## Script (Python) ".createNewFrontPage"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
id = 'uwosh-front-page'
if container.hasObject('help'):
    return "You already have a 'help' page.  Click to <a href='help'>see the help page</a>, or return to your site's <a href='.'>front page</a>."
else:
    # rename the old front page to 'help', change its title
    try:
        container.manage_renameObject(id, 'help')
    except:
        container.manage_renameObject('welcome', 'help')
    helpdoc = getattr(container, 'help')
    helpdoc.setTitle('Getting Help with Plone at UW Oshkosh')
    container.reindexObject('help')
    # create the new front page
    container.invokeFactory(type_name="Document", id=id)
    doc = getattr(container, id)
    doc.setTitle("Welcome")
    editurl = doc.absolute_url() + '/edit'
    helpurl = container.absolute_url() + '/help'
    # set the body of the new front page
    doc.setText("<p>Welcome to your new web site!  Click to <a href='%s'>edit this page</a>.</p> <p>The old front page with links to UW Oshkosh Plone help resources is still available <a href='%s'>here</a>.</p>" % (editurl, helpurl))
    # publish the new frontpage
    doc.content_status_modify(workflow_action='publish')
    # make the default page the new front page
    container.setDefaultPage(id)

return container.restrictedTraverse(id)()
