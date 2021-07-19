# Ford Invoice Project
# Created by: Jacob Maxwell
# Start date: 6/24/2021
# Last updated: 7/14/2021
# CassPort credentials: (username, password, url) >> (BUCHANANC1, Red5454*, https://my.cassport.com/CassPort/#/)
# Purpose: Create a bot that checks the statuses on invoices and returns the statuses and
#          any errors
import tkinter as Tk
from tkinter import Toplevel
from fordbotobject import *
from functions import askForFile

# Initiates the window
root = Tk()
root.withdraw()

# Selecting a csv file and storing invoices
invoices = []
invoiceCSVFile = askForFile()

# Timer function
starttime = time.time()

# Structure of the bot and the pop up notice
bot = Bot()
bot.collectInvoiceList(invoiceCSVFile)

completionTime = round(bot.getInvoiceSize() / 4, 1)
message = "There are " + str(bot.getInvoiceSize()) + " invoices. This process with take approximately " + str(completionTime) + " minutes to complete (depending on internet speed). When you are ready to begin please press 'OK'."
messagebox.showinfo("Processing Invoices", message)

bot.login()
bot.invoicePage()
bot.invoiceSearch(invoiceCSVFile)
bot.closeWindow()

# Completion message
endtime = (time.time() - starttime)
totalTime = str(round((endtime / 60), 2))
message = "The program took " + totalTime + " minutes to complete. All rejected invoices has been saved over your original CSV file."
texto = Toplevel(root)
texto.withdraw()

messagebox.showinfo("Finished processing invoices", message, parent = texto)