from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
from Phidgets.Devices.RFID import RFID

class RFIDObject:
    def __init__(self):
        self.InitRFID()

    def InitRFID(self):
        try:
            self.RFIDEnabled=False
            self.rfid = RFID()
            self.rfid.setOnAttachHandler(self.RFIDAttached)
            self.rfid.setOnDetachHandler(self.RFIDDetached)
            self.rfid.setOnTagHandler(self.RFIDNewTag)
            self.rfid.openPhidget()
            print ('here')
        except RuntimeError as e:
            self.Log("Runtime Exception creating RFID: %s" % e.details)
            self.Log("Exiting....")
            exit(1)        
        
    def RFIDAttached(self,e):
        self.RFIDEnabled=True
        print "Found RFID"
        self.rfid.setAntennaOn(True)
        
    def RFIDDetached(self,e):
        self.RFIDEnabled=False
        print "RFID Detached"

    def RFIDNewTag(self,e):
        self.RFIDButtonHit=True
        print "RFID tag %s"%e.tag
        

