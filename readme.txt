Build
-----

To build:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican content

To view:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website\output
python -m pelican.server

http://localhost:8000/

Publish
-------

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican content
cd C:\Projects\badadonf\badadonf
python s3upload.py

http://stackoverflow.com/questions/1086240/how-can-i-update-files-on-amazons-cdn-cloudfront
https://console.aws.amazon.com/cloudfront/
Select, then click Invalidations tab
Enter "*"


Setup
-----

pip install pelican
pip install pillow
pip install fabric

To build initial website:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican-quickstart

Theme setup - see https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

cd C:\Projects\badadonf\badadonf\website\theme\
git clone https://github.com/getpelican/pelican-themes.git

Other Notes
-----------

http://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog#31270471
https://commons.wikimedia.org/wiki/File:Badminton_pictogram.svg

# add theme to project for easier editing

mklink /J "C:\Projects\badadonf\badadonf\pelican-bootstrap3" "C:\Projects\badadonf\pelican-themes\pelican-bootstrap3"

Git
---

Pelican plugins - need to update submodules too or lots are missing!
C:\Projects\badadonf\pelican-plugins

git.exe submodule update --init


PDFs
----

Plugin

https://github.com/cmacmackin/pdf-img
http://stackoverflow.com/questions/32466112/imagemagick-convert-pdf-to-jpeg

pip install wand
pip install bs4


http://docs.wand-py.org/en/0.4.1/guide/install.html#install-imagemagick-windows - not needed?
http://ghostscript.com/download/gsdnld.html

Interclub
---------

Get results from http://www.cdbvo.fr/vie-sportive/seniors/interclub-mixte-d3.html
