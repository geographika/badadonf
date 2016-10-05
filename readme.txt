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
robocopy C:\Projects\badadonf\badadonf\website\output C:\Users\SG\Documents\Dropbox\Public\badadonf /MIR
robocopy C:\Projects\badadonf\badadonf\website\output C:\Users\seth\Dropbox\Public\badadonf /MIR

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
