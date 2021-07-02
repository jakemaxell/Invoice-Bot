import tkinter as Tk
import csv
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import messagebox
from invoiceobject import *
from fordbotobject import *

# Function that asks the user to select a csv file
def askForFile():
    root = Tk()
    root.withdraw()

    filename = askopenfilename()
    return filename

# Function that writes over the initial csv file
def writeCSV(listOfInvoices, filename):
    header = ['Pro Number', 'Amount Billed', 'Amount Paid', 'Base Reason', 'Paid Date', 'Shipper Name', 'Disposition']
    data = [person.getProNumber(), person.getAmountBilled(), person.getAmountPaid(), person.getBaseReason(), person.getPaidDate(), person.getShipperName(), person.getDisposition()]

    with open(filename, 'w', newline = "") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(header)

        for x in listOfInvoices:
            data = [x.getProNumber(), x.getAmountBilled(), x.getAmountPaid(), x.getBaseReason(), x.getPaidDate(), x.getShipperName(), x.getDisposition()]
            writer.writerow(data)

        csvFile.close()