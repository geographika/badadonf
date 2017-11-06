Setup
-----

pip install pelican
pip install pillow
pip install fabric

Or

pip install  -r D:\GitHub\badadonf\requirements.txt

To build initial website:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican-quickstart

Theme setup - see https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

cd /D D:\GitHub\badadonf
git clone https://github.com/geographika/pelican-themes
git clone https://github.com/getpelican/pelican-plugins.git

Pelican plugins - need to update submodules too or lots are missing!

cd /D D:\GitHub\badadonf\pelican-plugins
git submodule update --init

Other Notes
-----------

http://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog#31270471
https://commons.wikimedia.org/wiki/File:Badminton_pictogram.svg

# add theme to project for easier editing

mklink /J "D:\GitHub\badadonf\pelican-bootstrap3" "D:\GitHub\badadonf\pelican-themes\pelican-bootstrap3"

Build
-----

To build:

C:\VirtualEnvs\badadonf\Scripts\activate
cd /D D:\GitHub\badadonf\website
pelican content

To view (easiest to keep this running in separate command window for hot reloading after new build):

C:\VirtualEnvs\badadonf\Scripts\activate
cd /D D:\GitHub\badadonf\website\output
python -m pelican.server


http://localhost:8000/

Publish
-------

C:\VirtualEnvs\badadonf\Scripts\activate
cd /D D:\GitHub\badadonf\website
pelican content
cd /D D:\GitHub\badadonf\
python s3upload.py




**Update**

Use s3browser
Delete old site - NOT favicon.ico, bad-logs or badadonf-logs
Copy new one in
Apply "Read" and "Read Permissions" to "All Users" for all files except the logs

http://stackoverflow.com/questions/1086240/how-can-i-update-files-on-amazons-cdn-cloudfront
https://console.aws.amazon.com/cloudfront/
Select, then click Invalidations tab
Enter "*"

Test at https://badadonf.s3.amazonaws.com/index.html
Then http://badadonf.fr/

PDFs
----

Plugin

https://github.com/cmacmackin/pdf-img
http://stackoverflow.com/questions/32466112/imagemagick-convert-pdf-to-jpeg

pip install wand
pip install bs4

Need both the following installed:

http://docs.wand-py.org/en/0.4.1/guide/install.html#install-imagemagick-windows
http://ghostscript.com/download/gsdnld.html

set MAGICK_HOME="C:\Program Files\ImageMagick-6.9.9-Q8"

Error: TypeError: LoadLibrary() argument 1 must be string, not unicode
For fix see: https://stackoverflow.com/questions/42660590/install-wand-on-a-windows-machine
Edit wand/api.py

        try:
            tried_paths.append(libwand_path)
            libwand = ctypes.CDLL(str(libwand_path))
            if libwand_path == libmagick_path:
                libmagick = libwand
            else:
                tried_paths.append(libmagick_path)
                libmagick = ctypes.CDLL((libmagick_path))
        except (IOError, OSError):


No GhostScript: Exception TypeError: TypeError("object of type 'NoneType' has no len()",) in <bound method Image.__del__ of <wand.image.Image: (empty)>> ignored

Interclub
---------

Get results from http://www.cdbvo.fr/vie-sportive/seniors/interclub-mixte-d3.html


JS
--

Bootstrap Lightbox

https://github.com/ashleydw/lightbox/tree/master/dist
https://github.com/ashleydw/lightbox/releases
