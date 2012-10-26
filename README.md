Trac port of redmine A1 theme
=============================

Description
-----------

This is a port from redmine to trac of original theme A1 from Kirill Bezrukov 
for redmine. You can find the original theme on http://redminecrm.com, thanks
to him for his great work.

Get the source code
-------------------

This project is hosted by github, you can get the sources by using :

	$ git clone https://github.com/svalat/TracThemeRedmineA1.git

Or : 

	$ git clone git://github.com/svalat/TracThemeRedmineA1.git

Install the theme
-----------------

This theme may require presence of trac plugin themeengine :
http://trac-hacks.org/wiki/ThemeEnginePlugin

To use this theme, you need trac 0.12, other versions are not tested 
but may also work.

	$ cd 0.12
	$ python setup.py bdist_egg

You will get the egg file in dirst directory : dist/RedmineA1Theme-1.0-py2.7.egg.
Now just place this file in your trac plugin directory and enable your theme in 
conf/trac.ini :

	[theme]
	theme = redminea1
	
	[components]
	redminea1theme.theme.redminea1theme = enabled

You can found more details on trac plugin installation in trac documentation :
http://trac.edgewall.org/wiki/TracPlugins
