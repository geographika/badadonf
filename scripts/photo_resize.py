from PIL import Image
import PIL
import os
import functools
from PIL import ExifTags
import piexif

# 1024, 768, 80
# https://www.daveperrett.com/articles/2012/07/28/exif-orientation-handling-is-a-ghetto/

def image_transpose_exif(im):
    exif_orientation_tag = 0x0112 # contains an integer, 1 through 8
    exif_transpose_sequences = [  # corresponding to the following
        [],
        [Image.FLIP_LEFT_RIGHT],
        [Image.ROTATE_180],
        [Image.FLIP_TOP_BOTTOM],
        [Image.FLIP_LEFT_RIGHT, Image.ROTATE_90],
        [Image.ROTATE_270],
        [Image.FLIP_TOP_BOTTOM, Image.ROTATE_90], #6 
        [Image.ROTATE_90],
    ]

    try:
        seq = exif_transpose_sequences[im._getexif()[exif_orientation_tag] - 1]
    except Exception:
        raise
        return im
    else:
        return functools.reduce(lambda im, op: im.transpose(op), seq, im)

size = (1024, 1024)

fld = r"D:\GitHub\badadonf\website\content\images\gallery\badadonf9"

infile = os.path.join(fld, "2017-11-19 19.23.07.jpg")
outfile = os.path.join(fld, "2017-11-19 19.23.07b.jpg")

maxsize = (1028, 1028)

im = Image.open(infile)
print(im.format)

print(im._getexif().items())
exif=dict((ExifTags.TAGS[k], v) for k, v in im._getexif().items() if k in ExifTags.TAGS)
print(exif)

#im.thumbnail(maxsize, PIL.Image.ANTIALIAS)
im = image_transpose_exif(im)
im.save(outfile, "JPEG")
print("Done!")