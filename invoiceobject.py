# Invoice Object
class Invoice:

    # Object Initializer
    def __init__(self, proNumber, amountBilled, amountPaid, baseReason, paidDate, shipperName, disposition):
        self.proNumber = proNumber
        self.amountBilled = amountBilled
        self.amountPaid = amountPaid
        self.baseReason = baseReason
        self.paidDate = paidDate
        self.shipperName = shipperName
        self.disposition = disposition

    # Print function
    def toString(self):
        print("Pro Number: " + self.proNumber)
        print("Amount Billed: " + self.amountBilled)
        print("Amount Paid: " + self.amountPaid)
        print("Base Reason: " + self.baseReason)
        print("Paid Date: " + self.paidDate)
        print("Shipper Name: " + self.shipperName)
        print("Disposition: " + self.disposition)

    # Getter methods
    def getDisposition(self):
        return self.disposition

    def getProNumber(self):
        return self.proNumber

    def getAmountBilled(self):
        return self.amountBilled

    def getAmountPaid(self):
        return self.amountPaid

    def getBaseReason(self):
        return self.baseReason

    def getPaidDate(self):
        return self.paidDate

    def getShipperName(self):
        return self.shipperName