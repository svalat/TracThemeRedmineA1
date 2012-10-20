Trac port of redmine A1 theme
=============================

Description
-----------

This is a port from redmine to trac of original theme A1 from Kirill Bezrukov 
for redmine. You can found the original theme on http://redminecrm.com.

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

	$ [theme]
	$ theme = redminea1

You can found more details on trac plugin installation in trac documentation :
http://trac.edgewall.org/wiki/TracPlugins

Screenshots
-----------

Here some screenshot of this theme on trac 0.12 :

[[https://raw.github.com/wiki/svalat/TracThemeRedmineA1/screens/page-wiki.png|frame|300px]]
[[https://raw.github.com/wiki/svalat/TracThemeRedmineA1/screens/page-admin.png|frame|300px]]
[[https://raw.github.com/wiki/svalat/TracThemeRedmineA1/screens/page-timeline.png|frame|300px]]
[[https://raw.github.com/wiki/svalat/TracThemeRedmineA1/screens/page-search.png|frame|300px]]
