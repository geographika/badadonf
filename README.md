## Saint Brice sous Foret Badminton Site

Source: https://github.com/geographika/badadonf
GitHub Pages site: https://geographika.github.io/badadonf/
URL: http://badadonf.fr/

## Setup

```
C:\Python310\python -m venv C:\VirtualEnvs\badadonf
C:\VirtualEnvs\badadonf\Scripts\activate.ps1

$PROJECT_ROOT="D:\GitHub\badadonf"

cd $PROJECT_ROOT

pip install  -r requirements.txt

git clone https://github.com/geographika/pelican-themes
git clone https://github.com/getpelican/pelican-plugins.git

# pelican plugins - need to update submodules too or lots are missing!

cd "$PROJECT_ROOT\pelican-plugins"
git submodule update --init
```

## Build

To build:

```
$WEB_PATH="$PROJECT_ROOT\website"
$MAGICK_HOME="C:\Program Files\ImageMagick-7.1.1-Q16-HDRI"

C:\VirtualEnvs\badadonf\Scripts\activate.ps1
cd $WEB_PATH
pelican content --debug
```

To view (easiest to keep this running in separate command window for hot reloading after new build):

```
$PROJECT_ROOT="D:\GitHub\badadonf"
$WEB_PATH="$PROJECT_ROOT\website"
C:\VirtualEnvs\badadonf\Scripts\activate.ps1
# note we should run listen from the /website path
cd $WEB_PATH
pelican --listen --port 8222 --autoreload
```

http://127.0.0.1:8222

## PDFs

Plugin

https://github.com/cmacmackin/pdf-img
http://stackoverflow.com/questions/32466112/imagemagick-convert-pdf-to-jpeg

Need both the following installed:

http://docs.wand-py.org/en/0.4.1/guide/install.html#install-imagemagick-windows

* Download link http://www.imagemagick.org/script/download.php

**Note** Make sure development headers are installed also. 

Also need to install: http://ghostscript.com/download/gsdnld.html
Or CRITICAL: FailedToExecuteCommand `"gswin64c.exe" 

```
set MAGICK_HOME="C:\Program Files\ImageMagick-7.1.0-Q16-HDRI"
```

```
No GhostScript: Exception TypeError: TypeError("object of type 'NoneType' has no len()",) in <bound method Image.__del__ of <wand.image.Image: (empty)>> ignored
```

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

```
    if ispiexif and settings['PHOTO_EXIF_KEEP'] and im.format in ('JPEG', 'MPO'):  # Only works with JPEG exif for sure.
```