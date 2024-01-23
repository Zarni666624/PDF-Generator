# BY Zarni Win
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter, A4
from random import *

try:
    shutil.rmtree('worksheets')
except:
    pass
a = 1
try:
    os.mkdir('worksheets')
except:
    pass


class Interface(BoxLayout):
    def pdf(self):
        try:
            sh = int(self.ids.textInput1.text)
            nod = int(self.ids.textInput2.text)
            op = self.ids.textInput3.text
            for aa in range(sh):
                if op == "x":
                    op = chr(215)
                my_path = 'worksheets\\my_pdf{}.pdf'.format(aa + 1)
                c = canvas.Canvas(my_path, pagesize=A4)
                c.translate(inch, inch)
                for i in range(3):
                    c.setFont('Helvetica', 15)
                    for ii in range(4):
                        if op == "-":
                            m = randint(10 ** (nod - 1), 10 ** nod - 1)
                            c.drawString(2.5 * i * inch, (2.5 * ii + 1) * inch,
                                         '  {}'.format(randint(m, 10 ** nod - 1)))
                            c.drawString(2.5 * i * inch, (2.5 * ii + .75) * inch,
                                         " -{}".format(randint(10 ** (nod - 1), m)))
                        else:
                            c.drawString(2.5 * i * inch, (2.5 * ii + 1) * inch,
                                         '  {}'.format(randint(10 ** (nod - 1), 10 ** nod - 1)))
                            c.drawString(2.5 * i * inch, (2.5 * ii + .75) * inch,
                                         "{}{}".format(op, randint(10 ** (nod - 1), 10 ** nod - 1)))
                        c.line(2.5 * i * inch, (2.5 * ii + .75) * inch - 3, (2.5 * i + .125 * (nod + 1)) * inch,
                               (2.5 * ii + .75) * inch - 3)
                c.drawString(0, 9.5 * inch, "Name:")
                c.line(0.65 * inch, 9.5 * inch, 2.5 * inch, 9.5 * inch)
                c.drawString(3 * inch, 9.5 * inch, "Class:")
                c.line(3.65 * inch, 9.5 * inch, 5.5 * inch, 9.5 * inch)
                c.line(-.5 * inch, .3 * inch, 7 * inch, .3 * inch)
                c.drawImage('By.jpg', 5.5 * inch, -.001 * inch, 1.75 * inch, .25 * inch)
                c.showPage()
                c.save()
        except:
            self.ids.textInput1.text = "Error"
            self.ids.textInput2.text = ""
            self.ids.textInput3.text = ""
            self.ids.button.text = 'Create pdf!'


class MwgApp(App):
    pass


MwgApp().run()
