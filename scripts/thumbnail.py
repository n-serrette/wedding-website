import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", type=str)
parser.add_argument("-i", "--image", type=str,
                    default="../static/gallery/images")
parser.add_argument("-t", "--thumbnail", type=str,
                    default="../static/gallery/thumbnail")
parser.add_argument("-w", "--width", type=int,
                    default=200)
parser.add_argument("-o", "--optimize", action="store_true")
args = parser.parse_args()

sources = os.listdir(args.source)
for file in sources:
    if os.path.basename(file) == '.gitignore':
        continue
    img = Image.open(os.path.join(args.source, file))
    wpercent = (args.width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    resized = img.resize((args.width, hsize), Image.ANTIALIAS)
    resized.save(os.path.join(args.thumbnail, os.path.basename(file)),
                 optimize=args.optimize)
    img.save(os.path.join(args.image, os.path.basename(file)),
             optimize=args.optimize)
