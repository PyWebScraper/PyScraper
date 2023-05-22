from reportlab.pdfgen import canvas


def create_pdf(output_file, font='Sans', fontsize=12, start_location=700, *elements):

    '''
    Creates a PDF file with whatever elements the user wants to include. can f.ex be used to create a report.

    example use: create_pdf(output_file, font='Arial', fontsize=16, start_location=700, title, published_date, category)

    the order of which you add the different elements is the order they will be added.
    '''

    # Setup of the pdf file, and font(size)
    frame = canvas.Canvas(output_file)
    frame.setFont(font, fontsize)

    # Where we start "writing on the pdf page
    start_location = start_location

    # Iterate over the elements and write them to the pdf
    for element in elements:
        frame.drawString(50, start_location, str(element))
        start_location -= 20  # Decreases the Y coodrinate between each element.
    frame.save()