#module/class imports 

from backend import SmartPlug 
from backend import SmartWashingMachine
from backend import SmartHome 
from tkinter import * 


#Global Variables
userSmartHome = SmartHome()
mainWin = Tk() 


#functions 
def setupHome(): 
    """
    Sets up the home class by adding in 5 of the required devices into the home object
    """
    washingMachine1 = SmartWashingMachine() 
    plug1 = SmartPlug()
    washingMachine2 = SmartWashingMachine()
    washingMachine3 = SmartWashingMachine() 
    plug2 = SmartPlug() 

    userSmartHome.addDevice(washingMachine1)
    userSmartHome.addDevice(plug1) 
    userSmartHome.addDevice(washingMachine2)
    userSmartHome.addDevice(washingMachine3)
    userSmartHome.addDevice(plug2)

def listSmartHomeDevices(): 

    #list Devices
    for deviceIndex in range(5):
        device = userSmartHome.getDevicesAt(deviceIndex) 

        #Device text creation 
        deviceTxt = Text(mainWin, height=2, width=55) 
        deviceTxt.insert("1.0", str(device)) 
        deviceTxt.grid(row=deviceIndex + 2, column=0, padx=10, pady=5) 


        #Device toggle button
        toggleBtn = Button(mainWin, text="Toggle this", command="")
        toggleBtn.grid(row=deviceIndex + 2, column=1, padx=10, pady= 5, sticky="e")

def setupMainWindow():
    """
    Setups the main window for the smart home app
    """

    mainWin.title("Smart Home") 
    mainWin.geometry("500x{}".format(7*55)) 
    mainWin.resizable(False, False)

    #column configuration
    mainWin.columnconfigure(index=0, weight=4)

    #list Devices
    deviceIndexList = len(userSmartHome.getDevices())
    for deviceIndex in range(1, deviceIndexList, 1):
        device = userSmartHome.getDevicesAt(deviceIndex) 

        #Device text creation 
        deviceTxt = Text(mainWin, height=2, width=55) 
        deviceTxt.insert("1.0", str(device)) 
        deviceTxt.grid(row=deviceIndex + 1, column=0, padx=10, pady=5) 

        def turnDeviceOnCommand():
            turnAllDevicesOn(deviceTxt)

        def turnDevicesOffCommand():
            turnAllDevicesOff(deviceTxt)


        #Device toggle button
        toggleBtn = Button(mainWin, text="Toggle this")
        toggleBtn.grid(row=deviceIndex + 2, column=1, padx=10, pady= 5, sticky="e")

    #Setup Devices On status
    numberOfDevicesOn = userSmartHome.getDeviceOnStatus() 
    deviceOnStatus = Label(mainWin,text="Number of Devices on: {}".format(numberOfDevicesOn))
    deviceOnStatus.grid(row=deviceIndexList + 2, column=0, padx= 15, pady= 10, sticky="nw") 
    deviceOnStatus.config(font=("TkDefaultFont", 12, "bold"))
             
            

    
    

 
    #button creation
    turnAllOffBtn = Button(mainWin, text="Turn all off", command=turnDevicesOffCommand) 
    turnAllOffBtn.grid(row= 0, column=0,padx=10 ,pady= 5 , sticky="nw") 
    
    turnAllOnBtn = Button(mainWin,text="Turn all on", command=turnDeviceOnCommand)
    turnAllOnBtn.grid(row=1, column=0, padx= 10, pady= 5, sticky="nw") 
    listSmartHomeDevices()

    mainWin.mainloop()

def turnAllDevicesOn(deviceTxt):
    userSmartHome.turnOnAll() 
    deviceTxt.delete("1.0","2.0")
    listSmartHomeDevices()  
    
def turnAllDevicesOff(deviceTxt):
    userSmartHome.turnOffAll() 
    deviceTxt.delete("1.0")
    listSmartHomeDevices() 

def toggleDevice(deviceTxt, deviceIndex):
    userSmartHome.toggleSwitch(deviceIndex)
    deviceTxt.delete("{}.0".format(deviceIndex)) 
    listSmartHomeDevices() 

def main():
    setupHome()
    setupMainWindow() 
    





#program run
main() 
