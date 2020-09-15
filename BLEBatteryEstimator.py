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
    totalActiveTime = devwkupTime + (standbyTime) + (idleTime) + (tx_1Time) + (t_ifsTime) + (rx_1Time) + (standby_idleTime) + (tx_2Time) + (t_ifsTime) + (rx_2Time) + (standby_idleTime) + (tx_3Time) + (t_ifsTime) + (rx_3Time) + (post_processTime) + (devsleepTime)
    sleepTime = AdvInterval - totalActiveTime
    ConnectionInterval = 1
    ConnectionMeasuredI0dBm = (1.31E-3 + 916.6E-6 + 1.21E-3)/3
    ScannerMeasuredI = 4.36E-3

    def AdvAvgI(self):
        area = (self.devwkupCurrent * self.devwkupTime) + (self.standbyCurrent * self.standbyTime) + (self.idleCurrent * self.idleTime) + (self.tx_1Current * self.tx_1Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_1Current * self.rx_1Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_2Current * self.tx_2Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_2Current * self.rx_2Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_3Current * self.tx_3Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_3Current * self.rx_3Time) + (self.post_processCurrent * self.post_processTime) + (self.devsleepCurrent * self.devsleepTime) + (self.sleepCurrent * self.sleepTime)
        totalTime = self.devwkupTime + (self.standbyTime) + (self.idleTime) + (self.tx_1Time) + (self.t_ifsTime) + (self.rx_1Time) + (self.standby_idleTime) + (self.tx_2Time) + (self.t_ifsTime) + (self.rx_2Time) + (self.standby_idleTime) + (self.tx_3Time) + (self.t_ifsTime) + (self.rx_3Time) + (self.post_processTime) + (self.devsleepTime) + (self.sleepTime)
        return area / totalTime

    def ConnAvgI(self, powerlevel):
        if powerlevel==0:
            return self.ConnectionMeasuredI0dBm
        else:
            return self.ConnectionMeasuredI0dBm

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


batterySize = input ("Type the Battery Size in mAh: ")
batterySize = batterySize * 1E-3
#printList(parts,"Choose which device do you want to estimate Power Consumption: \r")
#Choice = menuOptions(parts,"Enter your choice:")
AdvPercentage = float(input ("Percentage of the Duty Cycle in Advertisement mode: "))
ScanPercentage = float(input ("Percentage of the Duty Cycle in Scanning mode: "))
ConnPercentage = float(input ("Percentage of the Duty Cycle in Connection mode: "))


emptySoc0dBm = BLEDevice()
emptySoc8dBm = BLEDevice()
emptySoc6dBm = BLEDevice()

emptySoc8dBm.tx_1Current = 10E-3
emptySoc6dBm.tx_1Current = 8.5E-3

totalAvgI = ((emptySoc0dBm.AdvAvgI() * AdvPercentage) + (emptySoc0dBm.ScanAvgI() * ScanPercentage) + (emptySoc0dBm.ConnAvgI(0) * ConnPercentage)) / 100
print("Total Average Current is %.3e" % totalAvgI)

batteryLife = float(batterySize / (totalAvgI * 8760) * 0.7)

print("Total Estimated Battery Life in Years is %f" % batteryLife)
