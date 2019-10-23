from abc import ABC, abstractmethod

class Describable(ABC):
    def __init__(self):
        super().__init__()



class FoodCropFactory :
    def __init__(self):
    def createVolume(self,ID: int) -> Unit:
    def createPrice(self,ID: int) -> Unit:
    def createWeight(self,ID: int,weight : float) -> Unit:
    def createSurface(self,ID: int) -> Unit:
    def createCount(self,ID: int,what: str) -> Unit:
    def createRatio(self,ID: int) -> Unit:
    def createUnitRatio(self,ID: int,unit1: Unit,unit2: Unit) -> Unit:
    def createCommodity(self,group: CommodityGroup, ID: int, name: str) -> Commodity:
    def createIndicator(self,ID: int frequency: int, freqDesc: str,geogLocation: str,indicatorGroup: IndicatorGroup,unit: Unit) -> Indicator:
    def createMeasurementType(self,ID: int,description: str) -> MeasurementType:
    def createMeasurement(self,ID: int,year: int,value: float,timeperiodId: int,timeperiodDesc: str,tipe: MeasurementType,commodity: Commodity,indicator: Indicator) -> Measurement:
    
    
class FoodCropsDataset :
    def __init__(self):
    def load(self,datasetPath: str):
    def findMeasurements(self,commodityType: CommodityType = nil,indicatorGroup: IndicatorGroup = nil,geographicalLocation: str = nil,unit: Unit = nil) -> List[Measurement]:

class Measurement :
    def __init__(self):

class Commodity :
    def __init__(self):
    
class Indicator :
    def __init__(self):

class MeasurementType :
    def __init__(self):       

class Unit(ABC):
    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name
        self.id = id

class Volume(Unit):
    def __init__(self, id:int, name:str = "Volume"):
        super().__init__()
        
class Surface(Unit):
    def __init__(self, id:int, name:str = "Surface"):
        super().__init__()
        self.__name = name

class Price(Unit):
    def __init__(self, id:int, name:str):
        super().__init__()

class Weight(Unit):
    def __init__(self, id:int, name:str = "Weight", multiplier:float):
        super().__init__()
        self.__multiplier = multiplier
            
class Count(Unit):
    def __init__(self, id:int, name:str = "Count", what:str):
        super().__init__()
        self.__what = what
            
class Ratio(Unit):
    def __init__(self, id:int, name:str = "Ratio"):
        super().__init__()
            
class UnitRatio(Ratio):
    def __init__(self, id:int, unit1:Unit, unit2:Unit):
        super().__init__()
