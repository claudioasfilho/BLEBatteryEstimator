#BLE Battery Estimator

#This was based on AN1246 from Silicon Labs, parameters from the BG22 device transmitting at 0dbm
class BLEDevice:
    devwkupTime = 40E-6
    devwkupCurrent = 1E-3
    standbyTime = 363E-6
    standbyCurrent = 1.1E-3
    idleTime = 109E-6
    idleCurrent = 3.1E-3
    tx_1Time = 379E-6
    tx_1Current = 4.7E-3
    t_ifsTime = 137E-6
    t_ifsCurrent = 3.5E-3
    rx_1Time = 106E-6
    rx_1Current = 4.2E-3
    standby_idleTime = 178E-6
    standby_idleCurrent = 2.7E-3
    tx_2Time = tx_1Time #382E-6
    tx_2Current = tx_1Current #4.7E-3
    rx_2Time = rx_1Time #106E-6
    rx_2Current = rx_1Current #4.6E-3
    tx_3Time = tx_1Time #379E-6
    tx_3Current = tx_1Current #4.7E-3
    rx_3Time = rx_1Time #105E-6
    rx_3Current = rx_1Current #4.1E-3
    post_processTime = 205E-6
    post_processCurrent = 2.1E-3
    devsleepTime = 65E-6
    devsleepCurrent = 0.8E-3
    sleepCurrent = 1.3E-6
    AdvInterval = 4
    ConnectionTXDuration = 2.5E-3
    ConnectionInterval = 4
    ConnectionMeasuredI0dBm = (1.18E-3 + 1.17E-3 + 1.22E-3)/3
    ConnectionMeasuredI6dBm = (1.32E-3 + 1.17E-3 + 1.26E-3)/3
    ConnectionMeasuredI8dBm = (1.32E-3 + 1.17E-3 + 1.26E-3)/3

    ScannerMeasuredI = 2.2E-3

    def AdvInt(self, newValue):
        self.AdvInterval = newValue

    def AdvAvgI(self):
        totalActiveTime = self.devwkupTime + (self.standbyTime) + (self.idleTime) + (self.tx_1Time) + (self.t_ifsTime) + (self.rx_1Time) + (self.standby_idleTime) + (self.tx_2Time) + (self.t_ifsTime) + (self.rx_2Time) + (self.standby_idleTime) + (self.tx_3Time) + (self.t_ifsTime) + (self.rx_3Time) + (self.post_processTime) + (self.devsleepTime)
        sleepTime = self.AdvInterval - totalActiveTime
        area = (self.devwkupCurrent * self.devwkupTime) + (self.standbyCurrent * self.standbyTime) + (self.idleCurrent * self.idleTime) + (self.tx_1Current * self.tx_1Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_1Current * self.rx_1Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_2Current * self.tx_2Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_2Current * self.rx_2Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_3Current * self.tx_3Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_3Current * self.rx_3Time) + (self.post_processCurrent * self.post_processTime) + (self.devsleepCurrent * self.devsleepTime) + (self.sleepCurrent * sleepTime)
        totalTime = self.devwkupTime + (self.standbyTime) + (self.idleTime) + (self.tx_1Time) + (self.t_ifsTime) + (self.rx_1Time) + (self.standby_idleTime) + (self.tx_2Time) + (self.t_ifsTime) + (self.rx_2Time) + (self.standby_idleTime) + (self.tx_3Time) + (self.t_ifsTime) + (self.rx_3Time) + (self.post_processTime) + (self.devsleepTime) + (sleepTime)
        return area / totalTime

    def ConnAvgI(self, powerlevel):
        if powerlevel==0:
            connectionActiveCurrent = self.ConnectionMeasuredI0dBm
        if powerlevel==6:
            connectionActiveCurrent = self.ConnectionMeasuredI6dBm
        if powerlevel==8:
            connectionActiveCurrent = self.ConnectionMeasuredI8dBm

        totalActiveTime = self.ConnectionTXDuration
        sleepTime = self.ConnectionInterval - totalActiveTime
        totalTime = self.ConnectionInterval
        area = (totalActiveTime * connectionActiveCurrent) + (self.sleepCurrent * sleepTime)
        return area / totalTime

    def ScanAvgI(self):
        return self.ScannerMeasuredI


def printList(listOfOptions, choiceWrd):
    print choiceWrd
    for key, value in listOfOptions.items():
        print key,':',value

def menuOptions(listOfOptions, choiceWrd):
    result = None
    while result is None:
        val = raw_input (choiceWrd)
        if (val.islower()) == True:
            val = val.upper()
        if val in listOfOptions:
            optionSelected = listOfOptions.get(val)
            print "Option chosen %s " % optionSelected
            result = 1
        else:
            print "Choice not available \n\r"

    return optionSelected


parts = {
    "A" : "EFR32BG21",
    "B" : "EFR32BG22"
}
BG22PowerLevel = {
    "0" : "0dBm",
    "6" : "6dBm",
    "8" : "8dBm"
}

emptySoc0dBm = BLEDevice()


batterySize = input ("Type the Battery Size in mAh: ")
batterySize = batterySize * 1E-3
#printList(parts,"Choose which device do you want to estimate Power Consumption: \r")
#Choice = menuOptions(parts,"Enter your choice:")
AdvPercentage = float(input ("Percentage of the Duty Cycle in Advertisement mode: "))
if AdvPercentage > 0:
    #emptySoc0dBm.AdvInt(float(input ("Please type the Advertisement Interval in seconds: ")))
    emptySoc0dBm.AdvInterval = float(input ("Please type the Advertisement Interval in seconds: "))
    printList(BG22PowerLevel,"Choose PA Power level: \r")
    Choice = menuOptions(BG22PowerLevel,"Enter your choice:")
    if Choice == '0dBm':
        emptySoc0dBm.tx_1Current = 4.7E-3
        PALevel = 0
    if Choice == '6dBm':
        emptySoc0dBm.tx_1Current = 8.5E-3
        PALevel = 6
    if Choice == '8dBm':
        emptySoc0dBm.tx_1Current = 9.5E-3
        PALevel = 8

if AdvPercentage != 100:
    ScanPercentage = float(input ("Percentage of the Duty Cycle in Scanning mode: "))
    ConnPercentage = float(input ("Percentage of the Duty Cycle in Connection mode: "))
    emptySoc0dBm.ConnectionInterval = float(input ("Please type the Connection Interval in seconds: "))

else:
    ScanPercentage = 0
    ConnPercentage = 0



totalAvgI = ((emptySoc0dBm.AdvAvgI() * AdvPercentage) + (emptySoc0dBm.ScanAvgI() * ScanPercentage) + (emptySoc0dBm.ConnAvgI(PALevel) * ConnPercentage)) / 100
print("Total Average Current is %.3e A" % totalAvgI)

batteryLife = float(batterySize / (totalAvgI * 8760) * 0.6)

print("Total Estimated Battery Life is %f years /n" % batteryLife)
print("This calculation assumes a battery drate of 40%")
