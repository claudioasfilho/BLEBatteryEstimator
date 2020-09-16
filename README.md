# BLEBatteryEstimator

This is a battery estimator for the EFR32BG22 device.

The Advertising calculations were based on the AN1246 and Scanning and Connections were calculations actually done taking several measurements with the WSTK.

This also assumes a battery Drate of 40%, which also can be better tuned for your own battery.

To be included in future versions:

To allow other devices, like the BG21 or future Series 2 devices.

This was tested with Python 2.7.16 on MacOs
