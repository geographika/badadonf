pip install pelican
pip install pillow
pip install fabric

To build initial website:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican-quickstart


To build:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican content

To view:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website\output
python -m pelican.server

http://localhost:8000/



Theme setup - see https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

cd C:\Projects\badadonf\badadonf\website\theme\
git clone https://github.com/getpelican/pelican-themes.git


Publish:

#C:\VirtualEnvs\badadonf\Scripts\activate
#cd C:\Projects\badadonf\badadonf\website\output
#pelican content -s publishconf.py


Instead use:

C:\VirtualEnvs\badadonf\Scripts\activate
cd C:\Projects\badadonf\badadonf\website
pelican content
robocopy C:\Projects\badadonf\badadonf\website\output C:\Users\SG\Documents\Dropbox\Public\badadonf /MIR

robocopy C:\Projects\badadonf\badadonf\website\output C:\Users\seth\Dropbox\Public\badadonf /MIR

http://www.dropboxwiki.com/tips-and-tricks/host-websites-with-dropbox

If you own a domain, you can create a CNAME record that points to dl.dropbox.com. From this, you can create links such 
as dl.domain.com/u/[DropboxID]/pic.png. For more information, see here: http://forums.dropbox.com/topic.php?id=7897&replies=17.



http://bit.ly/badadonf

https://www.maketecheasier.com/4-ways-to-host-your-website-on-dropbox/

Create the .htaccess file on the root folder of your domain and enter the following information:

RedirectMatch 301 /site(.*) https://dl.dropbox.com/u/1234567/site/$1


Other Notes
-----------

http://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog#31270471
https://commons.wikimedia.org/wiki/File:Badminton_pictogram.svg


https://github.com/wrobstory/pelican_dynamic/blob/master/pelican_dynamic.py