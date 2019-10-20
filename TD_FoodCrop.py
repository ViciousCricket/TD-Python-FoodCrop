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
    def __init__(self):
        super().__init__()

class Volume(Unit):
    def __init__(self):
        super().__init__()

class Surface(Unit):
    def __init__(self):
        super().__init__()

class Price(Unit):
    def __init__(self):
        super().__init__()

class Weight(Unit):
    def __init__(self):
        super().__init__()

class Count(Unit):
    def __init__(self):
        super().__init__()

class Ratio(Unit):
    def __init__(self):
        super().__init__()

class UnitRatio(Ratio):
    def __init__(self):
        super().__init__()
