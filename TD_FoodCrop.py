from abc import ABC, abstractmethod
from enum import Enum

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
    def createIndicator(self,ID: int, frequency: int, freqDesc: str,geogLocation: str,indicatorGroup: IndicatorGroup,unit: Unit) -> Indicator:
    def createMeasurementType(self,ID: int,description: str) -> MeasurementType:
    def createMeasurement(self,ID: int,year: int,value: float,timeperiodId: int,timeperiodDesc: str,tipe: MeasurementType,commodity: Commodity,indicator: Indicator) -> Measurement:
    
    
class FoodCropsDataset :
    def __init__(self):
    def load(self,datasetPath: str):
    def findMeasurements(self,commodityType: CommodityType = nil,indicatorGroup: IndicatorGroup = nil,geographicalLocation: str = nil,unit: Unit = nil) -> List[Measurement]:

class Measurement :
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str, type: MeasurementType, commodity: Commodity, indicator: Indicator):
        self.__year=year
        self.__value=value
        self.__timeperiodld=timeperiodld
        self.__timeperiodDesc=timeperiodDesc

class Commodity(Describable) :
    def __init__(self, id : int, name : str, group : CommodityGroup):
        seld.id = id
        self.__name = name
        
        
class Indicator(Describable) :
    def __init__(self, id :str, frequency : int, frequencyDesc : str, geogLocation : str, indicatorGroup : IndicatorGroup, unit : Unit):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation

class MeasurementType :
    def __init__(self, id: int, description: str):
        self.id=id
        self.description=description     

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
        
class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = "exports and imports"
    SUPPLY_AND_USE = "supply and use"
    PRICES = "prices"
    FEED_PRICE_RATIOS = "feed price ratios"
    QUANTITIES_FED = "quantities fed"
    TRANSPORTATION = "transportation"
    ANIMAL_UNIT_INDEXES = "animal unit indexes"
    
class CommodityGroup(Enum):
    CORN = "corn"
    BARLEY = "barley"
    OATS = "oats"
    SORGHUM = "sorghum"
    BYPRODUCT_FEEDS ="byproduct feeds"
    COARSE_GRAINS = "coarse grains"
    HAY = "hay"
    ANIMAL_PROTEIN_FEEDS = "animal protein feeds"
    GRAIN_PROTEIN_FEEDS = "grain protein feeds"
    PROCESSED_FEEDS = "processed feeds"
    ENERGY_FEEDS = "energy feeds"
    OTHER = "other"
