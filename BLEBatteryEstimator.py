#BLE Battery Estimator

class Advertisement:
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
    AdvInterval = 1
    totalActiveTime = devwkupTime + (standbyTime) + (idleTime) + (tx_1Time) + (t_ifsTime) + (rx_1Time) + (standby_idleTime) + (tx_2Time) + (t_ifsTime) + (rx_2Time) + (standby_idleTime) + (tx_3Time) + (t_ifsTime) + (rx_3Time) + (post_processTime) + (devsleepTime)
    sleepTime = AdvInterval - totalActiveTime

    def Average(self):
        area = (self.devwkupCurrent * self.devwkupTime) + (self.standbyCurrent * self.standbyTime) + (self.idleCurrent * self.idleTime) + (self.tx_1Current * self.tx_1Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_1Current * self.rx_1Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_2Current * self.tx_2Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_2Current * self.rx_2Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_3Current * self.tx_3Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_3Current * self.rx_3Time) + (self.post_processCurrent * self.post_processTime) + (self.devsleepCurrent * self.devsleepTime) + (self.sleepCurrent * self.sleepTime)
        totalTime = self.devwkupTime + (self.standbyTime) + (self.idleTime) + (self.tx_1Time) + (self.t_ifsTime) + (self.rx_1Time) + (self.standby_idleTime) + (self.tx_2Time) + (self.t_ifsTime) + (self.rx_2Time) + (self.standby_idleTime) + (self.tx_3Time) + (self.t_ifsTime) + (self.rx_3Time) + (self.post_processTime) + (self.devsleepTime) + (self.sleepTime)
        return area / totalTime

class Connectable:
    devwkupTime = 40E-6
    devwkupCurrent = 1E-3
    standbyTime = 363E-6
    standbyCurrent = 1.1E-3
    idleTime = 109E-6
    idleCurrent = 3.1E-3
    tx_1Time = 379E-6
    tx_1Current = 4.6E-3
    t_ifsTime = 137E-6
    t_ifsCurrent = 3.5E-3
    rx_1Time = 106E-6
    rx_1Current = 4.1E-3
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
    AdvInterval = 1
    totalActiveTime = devwkupTime + (standbyTime) + (idleTime) + (tx_1Time) + (t_ifsTime) + (rx_1Time) + (standby_idleTime) + (tx_2Time) + (t_ifsTime) + (rx_2Time) + (standby_idleTime) + (tx_3Time) + (t_ifsTime) + (rx_3Time) + (post_processTime) + (devsleepTime)
    sleepTime = AdvInterval - totalActiveTime

    def Average(self):
        area = (self.devwkupCurrent * self.devwkupTime) + (self.standbyCurrent * self.standbyTime) + (self.idleCurrent * self.idleTime) + (self.tx_1Current * self.tx_1Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_1Current * self.rx_1Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_2Current * self.tx_2Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_2Current * self.rx_2Time) + (self.standby_idleCurrent * self.standby_idleTime) + (self.tx_3Current * self.tx_3Time) + (self.t_ifsCurrent * self.t_ifsTime) + (self.rx_3Current * self.rx_3Time) + (self.post_processCurrent * self.post_processTime) + (self.devsleepCurrent * self.devsleepTime) + (self.sleepCurrent * self.sleepTime)
        totalTime = self.devwkupTime + (self.standbyTime) + (self.idleTime) + (self.tx_1Time) + (self.t_ifsTime) + (self.rx_1Time) + (self.standby_idleTime) + (self.tx_2Time) + (self.t_ifsTime) + (self.rx_2Time) + (self.standby_idleTime) + (self.tx_3Time) + (self.t_ifsTime) + (self.rx_3Time) + (self.post_processTime) + (self.devsleepTime) + (self.sleepTime)
        return area / totalTime

emptySoc8dBm = Advertisement()
#emptySoc8dBm.tx_1Time = 300E-6
emptySoc8dBm.tx_1Current = 10E-3

emptySoc6dBm = Advertisement()
#emptySoc6dBm.tx_1Time = 300E-6
emptySoc6dBm.tx_1Current = 8.5E-3

emptySoc0dBm = Advertisement()
#emptySoc0dBm.tx_1Time = 300E-6
#emptySoc0dBm.tx_1Current = 4.1E-3


print("emptySoc0dBm %.2e" % emptySoc0dBm.Average())
print("emptySoc6dBm %.2e" % emptySoc6dBm.Average())
print("emptySoc8dBm %.2e" % emptySoc8dBm.Average())
