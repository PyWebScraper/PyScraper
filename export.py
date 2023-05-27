from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import FigureCanvasPdf
import matplotlib.pyplot as mpl
from printing import *

def create_pdf(output_file, font='Helvetica', fontsize=12, start_location_y_position=700, *elements):

   # Creates a PDF file with whatever elements the user wants to include. can f.ex be used to create a report.

    #example use: create_pdf(output_file, font='Arial', fontsize=16, start_location=700, title, published_date, category)

    #the order of which you add the different elements is the order they will be added.

    # Setup of the pdf file, and font(size)
    frame = canvas.Canvas(output_file)
    frame.setFont(psfontname="Helvetica", size=12)

    # Where we start "writing on the pdf page
    start_location_y = start_location_y_position

    # Iterate over the elements and write them to the pdf
    for element in elements:
        if isinstance(element, str) and element.startswith("Image: "):
            #figure_frame = FigureCanvasPdf(element)
            #figure_frame.print_figure("temp.pdf")
            image_path = element[7:]
            frame.drawImage(image_path, 50, start_location_y)
            #frame.drawImage("temp.pdf", 50, start_location_y)
            start_location_y -= element.bbox.height + 20
        frame.drawString(50, start_location_y, str(element))
        start_location_y -= 20  # Decreases the Y coodrinate between each element.
    frame.save()
