"""
An existing connection was forcibly closed by the remote host

http://stackoverflow.25lm.com/questions/38123504/boto2-file-upload-does-not-works/38252179

Still not working

Then see: http://badadonf.s3-website-eu-west-1.amazonaws.com

Use http://docs.pythonboto.org/en/latest/s3_tut.html#s3-tut ?
"""

import os

aws_key = "AKIAITR2DQLRH4IGAJPA"
aws_secret = "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"

import glob2

from boto.s3.connection import S3Connection
from boto.s3.key import Key
conn = S3Connection(aws_key, aws_secret)

def get_files(fld):
    return glob2.glob(fld + '/**/*.*')

def upload(files, root_folder):
    rs = conn.get_all_buckets()
    mybucket = conn.get_bucket('badadonf') # Substitute in your bucket name
    keys = mybucket.list()

    #for k in keys:
    #    print k

    k = Key(mybucket)
    
    for fn in files:
        out_fn = fn.replace(root_folder, "").replace("\\","/")
        key = out_fn[1:]
        print key
        k.key = key
        k.set_contents_from_filename(fn)
        k.set_acl('public-read') # not working?

        #k.get_contents_to_filename('myfile.html')

if __name__ == "__main__":
    fld = r'C:\Projects\badadonf\badadonf\website\output'
    files = get_files(fld)
    #print files
    upload(files, fld)
    print("Done!")

# badadonf.s3-website-eu-west-1.amazonaws.com
