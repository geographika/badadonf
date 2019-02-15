Setup
-----

C:\Python27\Scripts\virtualenv C:\VirtualEnvs\badadonf
C:\VirtualEnvs\badadonf\Scripts\activate

python -m pip install pip -U
pip install pelican
pip install pillow
pip install bs4
pip install wand

REM pip install fabric

Or

pip install  -r C:\Code\badadonf\requirements.txt
pip install  -r D:\GitHub\badadonf\requirements.txt

To build initial website:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican-quickstart

Theme setup - see https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

SET PROJECT_ROOT=D:\GitHub\badadonf
SET PROJECT_ROOT=C:\Code\badadonf

cd /D %PROJECT_ROOT%
git clone https://github.com/geographika/pelican-themes
git clone https://github.com/getpelican/pelican-plugins.git

Pelican plugins - need to update submodules too or lots are missing!

cd /D %PROJECT_ROOT%\pelican-plugins
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

SET WEB_PATH=C:\Code\badadonf\website
SET WEB_PATH=D:\GitHub\badadonf\website

C:\VirtualEnvs\badadonf\Scripts\activate
cd /D %WEB_PATH%
pelican content

To view (easiest to keep this running in separate command window for hot reloading after new build):

SET WEB_PATH=D:\GitHub\badadonf\website
C:\VirtualEnvs\badadonf\Scripts\activate
cd /D %WEB_PATH%\output
python -m pelican.server


http://localhost:8000/

Publish
-------

Use s3browser
Delete old site - NOT favicon.ico or badadonf-logs
Copy new one in from ``D:\GitHub\badadonf\website\output``
Apply "Read" to "All Users" for all files except the logs (select all then right-click permissions)

DON't DO FOLLOWING AS IT COST 200EUR WHEN DONE TOO MUCH!
LET SITE UPDATE OVERNIGHT...OR JUST INVALIDATE /pages files (select and right-click)

http://stackoverflow.com/questions/1086240/how-can-i-update-files-on-amazons-cdn-cloudfront
https://console.aws.amazon.com/cloudfront/
Select, then click Invalidations tab
Enter "*"

Test at https://badadonf.s3.amazonaws.com/index.html

http://badadonf.s3-website-eu-west-1.amazonaws.com/

Then http://badadonf.fr/

PDFs
----

Plugin

https://github.com/cmacmackin/pdf-img
http://stackoverflow.com/questions/32466112/imagemagick-convert-pdf-to-jpeg

pip install wand
pip install bs4
pip install piexif

Need both the following installed:

http://docs.wand-py.org/en/0.4.1/guide/install.html#install-imagemagick-windows
+ Download link http://www.imagemagick.org/script/download.php
http://ghostscript.com/download/gsdnld.html ??

**Note** Make sure development headers are installed also. 

set MAGICK_HOME="C:\Program Files\ImageMagick-7.0.8-Q16"

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

Get results from https://www.cdbvo.fr/vie-sportive/seniors/interclub-mixte-d4.html


JS
--

Bootstrap Lightbox

https://github.com/ashleydw/lightbox/tree/master/dist
https://github.com/ashleydw/lightbox/releases

Photos
------

For Canon:

    if ispiexif and settings['PHOTO_EXIF_KEEP'] and im.format in ('JPEG', 'MPO'):  # Only works with JPEG exif for sure.