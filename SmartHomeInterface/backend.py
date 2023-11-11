#List/Dictionaries 
washingModes = ["Daily wash", "Quick wash", "Eco"]

#Classes 

class SmartPlug():
    """
    Class representing smart plugs
    this class has the attributes switchedOn and consumptionRate
    Switched on is False by default
    Consumption Rate is by 0 by default minimum is 0 and maximum is 150 
    """

    def __init__(self):
        self.switchedOn = False
        self.consumptionRate = 0 
    
    #Accessor methods 

    def getSwitchedOn(self):

        """
        Returns the current status of the smartplug switch
        """
        return self.switchedOn 
    
    def getConsumptionRate(self):
        """
        Returns the current consumption rate of the smart plug
        """
        return self.consumptionRate  
    
    #String method
    def __str__(self):
        """
        Returns the current status on the smart plug switch and current consumption rate
        """
        if self.switchedOn == False:
            output = "Plug: off, {} consumption".format(self.consumptionRate)
        else:
            output = "Plug: on, {} consuption".format(self.consumptionRate) 
        
        return output
    
    #Mutator Methods 

    def toggleSwitch(self):
        """
        Toggles the current value of the smart plug switch 
        """

        if self.switchedOn == False:
            self.switchedOn = True
        else:
            self.switchedOn = False 
    
    def setConsumptionRate(self, consumptionRateInput):
        """
        Sets the value of the consumption rate as well as checks to ensure it remains within the set minimum and maximum values
        """

        while consumptionRateInput < 0 or consumptionRateInput > 150: #Check to ensure works as intended 
            consumptionRateInput = int(input("Please re-enter your consumption rate (Minimum value: 0 and Maximum value: 150): "))

        if consumptionRateInput >= 0 and consumptionRateInput <= 150: 
            self.consumptionRate = consumptionRateInput 

class SmartWashingMachine():

    """
    Class for Smart Washing machine
    Contains switchedOn attribute which is by default set to False
    Contains a washMode which by default is on Daily wash however it has 3 different options Daily wash, Quick wash and Eco
    """

    def __init__(self):
        
        self.switchedOn = False 
        self.washMode = "Daily wash"
    
    #Accessor methods 

    def getWashMode(self):
        """
        Returns the current washMode applied to the washing machine
        """
        return self.washMode 
    
    def getSwitchedOn(self):
        """
        Returns the washing Machine current switch status
        """
        return self.switchedOn

    #Mutator methods

    def toggleSwitch(self):
        """
        Toggles the current value of the Washing Machine switch 
        """

        if self.switchedOn == False:
            self.switchedOn = True 
        else:
            self.switchedOn = False 
    
    def setWashingMode(self, mode): 
        if mode in washingModes:
            self.washMode = mode 
        else:
            mode = input("The washing mode you have inputted is not valid please enter one of the following options (Daily wash, Quick Wash, Eco): ") 


    #str method

    def __str__(self): 
        """
        Returns the current status on the washing machine switch and current washing mode
        """
        if self.switchedOn == False:
            output = "Washing machine: off, wash mode: {}".format(self.washMode) 
        else:
            output = "Washing machine: on, wash mode: {}".format(self.washMode)
       
        return output

class SmartHome():
    """
    Class representing the smart home which harbours all smart devices
    There is one attribute which stores a list of all the devices added to the smart home
    By default the list is empty until devices are added in
    """
    def __init__(self):
        self.devices = [] 
    
    #Accessor methods
    def getDevices(self):
        """
        Returns a list of all devices within the smart home
        """
        return self.devices 

    def getDevicesAt(self, index):
        """
        Returns the device specified at given index
        """
        return self.devices[index] 

    def getDeviceOnStatus(self):
        devicesOn = 0 

        for index in range (len(self.getDevices())):
            device = self.getDevicesAt(index)
            if device.switchedOn == True:
                devicesOn = devicesOn + 1 

        devicesOn = str(devicesOn) 
        return devicesOn
    
    #Mutator methods 
    def addDevice(self, device):
        """
        Adds a smart plug or device to the list of smart home devices need to pass through the device   
        """
        self.devices.append(device) 
    
    def toggleSwitch(self,index):
        """
        Toggle the switch of the device provided through the index parameter 
        """
        self.devices[index].toggleSwitch() 
    
    def turnOnAll(self):
        """
        Toggle all devices switch to True 
        """
        for item in self.devices:
            if item.getSwitchedOn() == False:
                item.toggleSwitch() 
        
    def turnOffAll(self):
        """
        Toggle all devices switch to False 
        """
        for item in self.devices:
            if item.getSwitchedOn() == True:
                item.toggleSwitch() 

    #string method 
    def __str__(self):
        output = "Smart home devices: \n"
         
        for item in self.devices: 
            output = output + "{}\n".format(item)
            
        return output 

    
#functions 

def testSmartPlug():
    plug = SmartPlug()
    plug.toggleSwitch()

    print(plug.getSwitchedOn())
    print(plug.getConsumptionRate())

    plug.setConsumptionRate(100)
    print(plug.getConsumptionRate())

    print(plug) 

def testWashingMachine():
    washingMachine = SmartWashingMachine() 
    washingMachine.toggleSwitch() 

    print(washingMachine.getSwitchedOn()) 
    print(washingMachine.getWashMode()) 
    
    washingMachine.setWashingMode("Eco") 
    print(washingMachine.getWashMode()) 

    print(washingMachine) 

def testSmartHome(): 
    testingHome = SmartHome() 
    plug1 = SmartPlug() 
    plug2 = SmartPlug() 
    washingMachine1 = SmartWashingMachine() 

    plug2.toggleSwitch() 
    plug2.setConsumptionRate(45)
    washingMachine1.setWashingMode("Quick wash") 

    testingHome.addDevice(plug1) 
    testingHome.addDevice(plug2) 
    testingHome.addDevice(washingMachine1) 

    print(testingHome)
    testingHome.turnOnAll() 
    print(testingHome)
    
#Program runs 


