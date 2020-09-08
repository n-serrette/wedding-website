import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",
                    default="../static/gallery/images")
parser.add_argument("-o", "--output",
                    default="../static/gallery/thumbnail")
parser.add_argument("-w", "--width", type=int,
                    default=200)
args = parser.parse_args()

sources = os.listdir(args.input)
for file in sources:
    img = Image.open(os.path.join(args.input, file))
    wpercent = (args.width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((args.width, hsize), Image.ANTIALIAS)
    img.save(os.path.join(args.output, os.path.basename(file)))
