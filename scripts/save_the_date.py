import argparse
import io
import uuid
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape


def readExcludePassword(file_path):
    password = set()
    with open(file_path, "r") as file:
        password = set([line.rstrip() for line in file if line.rstrip()])
    return password


def genPassword(count, excluded=set()):
    password = set()
    while len(password) < count:
        newPass = str(uuid.uuid4())[0:6]
        if newPass not in excluded:
            password.add(newPass)
    return password


def generateOverlay(password):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=landscape(A4))
    can.setFont("Helvetica", 15)
    can.drawCentredString(687, 42, str(password))
    can.save()
    packet.seek(0)
    return PdfFileReader(packet)


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",
                    default="save_the_date.pdf")
parser.add_argument("-o", "--output",
                    default="save_the_date_generated.pdf")
parser.add_argument("-op", "--outpass",
                    default="password.txt")
parser.add_argument("-c", "--count", type=int,
                    default=1)
parser.add_argument("-e", "--exclude")
args = parser.parse_args()


excludedPass = set()
if args.exclude:
    excludedPass = readExcludePassword(args.exclude)

passSet = genPassword(args.count, excludedPass)
output = PdfFileWriter()

with open(args.input, "rb") as file:
    for password in passSet:
        overlay = generateOverlay(password)
        source_pdf = PdfFileReader(file)
        page = source_pdf.getPage(3)
        page.mergePage(overlay.getPage(0))
        output.addPage(page)

    with open(args.output, "wb") as outputStream:
        output.write(outputStream)

with open(args.outpass, "w") as passFile:
    passFile.write("\n".join(set.union(passSet, excludedPass)))
