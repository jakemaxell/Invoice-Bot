import csv
import tkinter as Tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from fordbotobject import *

# Function that asks the user to select a csv file
def askForFile():
    root = Tk()
    root.withdraw()

    filename = askopenfilename()
    return filename

# Function that writes over the initial csv file
def writeCSV(connection, curs, filename):
    sql_query = "SELECT * FROM invoices WHERE disposition != ' ';"
    curs.execute(sql_query)

    with open(filename, "w", newline = '') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([i[0] for i in curs.description])
        csvWriter.writerows(curs)