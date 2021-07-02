# Ford Bot Object
from invoiceobject import *
from functions import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time, csv, os

class Bot:

    # Makes the window headless
    myOptions = Options()
    #myOptions.add_argument('--headless')
    myOptions.add_argument('--disable-gpu')
    #myOptions.add_argument("--window-size=1325x744")

    # Chromedriver path and the initialized driver
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH, options = myOptions)
    driver.set_window_size(1800, 950)

    # List of invoices (beta-testing)
    invoices = []

    # Object initializer
    def __init__(self, username = "**********", password = "********", loginPage = "*************************", searchPage = "**************************"):
        self.username = username
        self.password = password
        self.loginPage = loginPage
        self.searchPage = searchPage

    # Reads in a CSV file and collects all data in the INVOICE# column
    def collectInvoiceList(self, file):
        with open(file) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                self.invoices.append(row["INVOICE#"])

        print(len(self.invoices))

    def getInvoiceSize(self):
        return len(self.invoices)

    # Function that forces the browser to wait until a class attribute has loaded
    def waitByClass(self, className):
        try:
            main = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, className)))
        except:
            self.driver.quit()

    # Function that forces the browser to wait until an id attribute has loaded
    def waitById(self, id):
        try:
            main = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id)))
        except:
            self.driver.quit()

    # Function that launches the browser and directs you to the login page
    def launch(self):
        self.driver.get(self.loginPage)

    # Function that logs you into the CassPort Portal
    def login(self):
        loginClass = "static-background"

        self.launch()
        self.waitByClass(loginClass)

        unHTML = self.driver.find_element_by_id("username")
        pwHTML = self.driver.find_element_by_id("password")

        unHTML.send_keys(self.username)
        pwHTML.send_keys(self.password)
        pwHTML.send_keys(Keys.RETURN)

    # Function that redirects you to the Invoices page
    def invoicePage(self):
        mainClass = "main"

        self.waitByClass(mainClass)
        self.driver.get(self.searchPage)

    # Function that searches for invoices and stores them appropriately
    def invoiceSearch(self, objList):
        invoiceID = "InquirySearchForm"
        filePlace = 1

        self.waitById(invoiceID)

        for invoiceNumber in (self.invoices):

            if(filePlace % 50 == 0):
                self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
                self.waitById(invoiceID)

            time.sleep(2)

            textField = self.driver.find_element_by_id("SearchInput")
            searchButton = self.driver.find_element_by_id("InquirySearch")

            #invoiceNumber = self.invoices[invoice]

            textField.send_keys(Keys.CONTROL, 'a')
            textField.send_keys(Keys.BACKSPACE)
            textField.send_keys(invoiceNumber)
            searchButton.click()

            self.waitById(invoiceID)

            resetLayout = self.driver.find_element_by_id("InquiryResultsGrid_DXCTMenu0_DXI0_T")
            resetLayout.click()

            time.sleep(3)

            self.waitById(invoiceID)

            filterButton = self.driver.find_element_by_id("InquiryResultsGrid_col13")
        # filterButton = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[3]/div/table/tbody/tr[2]/td[12]")
            #print(filterButton)
            filterButton.click()

            #filter = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[3]/div/table/tbody/tr[2]/td[12]/table/tbody/tr/td[1]")
            #filter.click()
            self.waitById(invoiceID)
            
            time.sleep(3)
            filterAgain = self.driver.find_element_by_id("InquiryResultsGrid_tcheader13")
            filterAgain.click()

            #filterButton.click()
            time.sleep(3)

            #os.system("pause")
            xPathIds = [
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[3]",
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[4]",
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[7]",
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[8]",
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[12]",
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[15]",
                "/html/body/div[3]/div[2]/form/table/tbody/tr/td/div[4]/table/tbody/tr[2]/td[17]"
            ]

            try:
                proNumber = self.driver.find_element_by_xpath(xPathIds[0])
                shipperName = self.driver.find_element_by_xpath(xPathIds[1])
                amountBilled = self.driver.find_element_by_xpath(xPathIds[2])
                amountPaid = self.driver.find_element_by_xpath(xPathIds[3])
                paidDate = self.driver.find_element_by_xpath(xPathIds[4])
                disposition = self.driver.find_element_by_xpath(xPathIds[5])
                baseReason = self.driver.find_element_by_xpath(xPathIds[6])

                newInvoice = Invoice(proNumber.text, amountBilled.text, amountPaid.text, baseReason.text, paidDate.text, shipperName.text, disposition.text)
                newInvoice.toString()
                print("---------------------------------------------------------------------------------------------------------------------------------------")

                #os.system("pause")

                print("Invoices Checked: " + str(filePlace) + "/" + str(len(self.invoices)))
                filePlace += 1
            
                if(newInvoice.getDisposition() != " "):
            
                    with open("values.txt", 'a') as file:
                        objList.append(newInvoice)
                        
                        file.write("Pro Number: " + newInvoice.getProNumber() + "\n")
                        file.write("Amount Billed: " + newInvoice.getAmountBilled() + "\n")
                        file.write("Amount Paid: " + newInvoice.getAmountPaid() + "\n")
                        file.write("Base Reason: " + newInvoice.getBaseReason() + "\n")
                        file.write("Paid Date: " + newInvoice.getPaidDate() + "\n")
                        file.write("Shipper Name: " + newInvoice.getShipperName() + "\n")
                        file.write("Disposition: " + newInvoice.getDisposition() + "\n")

                        file.close()
            except:
                newInvoice = Invoice(invoiceNumber, 0, 0, "An error occurred when parsing this invoice", "inconclusive", "Inconclusive", "An error occurred when parsing this invoice")
                objList.append(newInvoice)
        
        time.sleep(3)

        self.driver.save_screenshot("Screenshot.png")
        self.driver.quit()