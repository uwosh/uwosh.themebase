all:
	cat Makefile
	@echo ""
	@echo "Don't forget to change the version number in setup.py, profiles/default/metadata.xml, and version.txt"

clean:
	rm -rf build dist

egg:
	python2.4 setup.py sdist upload -r http://plone2.webcluster.uwosh.edu:9082/sites1/ploneprojects/software/

dist4:
	python2.6 setup.py sdist upload -r ourbasket
