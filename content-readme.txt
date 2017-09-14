Calendar
-------

badadonf.95350@gmail.com
BEmgCjIXJ4Zm


https://github.com/fullcalendar/fullcalendar/releases/tag/v3.5.0

Update JS ref in calendrier.rst

:javascripts: fullcalendar-3.0.0/locale/fr.js

And then in pelican-bootstrap3/templates/base.html

    <link rel="stylesheet" href="/js/fullcalendar-3.5.0/fullcalendar.css" />
    <link rel="stylesheet" href="/js/fullcalendar-3.5.0/fullcalendar.print.css" media='print' />
    <script src='/js/fullcalendar-3.5.0/lib/moment.min.js'></script>
    <!--<script src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/jquery.min.js"></script>-->
    <script src='/js/fullcalendar-3.5.0/lib/jquery.min.js'></script>
    <script src='/js/fullcalendar-3.5.0/fullcalendar.js'></script>
    <script src='/js/fullcalendar-3.5.0/gcal.js'></script>

    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/qtip2/3.0.3/jquery.qtip.min.css" />
    <script src='http://cdnjs.cloudflare.com/ajax/libs/qtip2/3.0.3/jquery.qtip.min.js'></script>

pelican-bootstrap
-----------------

The pelican-themes repository is stored on GitHub with changes for badadonf:

cd /D D:\GitHub\badadonf
git clone https://github.com/geographika/pelican-themes

To update this:

cd /D D:\GitHub\badadonf\pelican-themes

git pull from upstream

Edited files:

base.html
footer.html
links.html



Bootstrap Links
---------------

     <p class="bg-info">On sera présent au Forum des Associations le Dimanche, Gymnase Lionel Terray, 
        le 10 Septembre 2017 de 10h à 18h!</p>