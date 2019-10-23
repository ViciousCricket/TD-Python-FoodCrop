from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class Describable(ABC):
    def __init__(self):
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

class Commodity(Describable) :
    def __init__(self, id : int, name : str, group : CommodityGroup):
        self.id = id
        self.__name = name
        
class MeasurementType :
    def __init__(self, id: int, description: str):
        self.id=id
        self.description=description
    
class Unit(ABC):
    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name
        self.id = id

class Indicator(Describable) :
    def __init__(self, id :str, frequency : int, frequencyDesc : str, geogLocation : str, indicatorGroup : IndicatorGroup, unit : Unit):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation

class Measurement :
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str, type: MeasurementType, commodity: Commodity, indicator: Indicator):
        self.__year=year
        self.__value=value
        self.__timeperiodld=timeperiodld
        self.__timeperiodDesc=timeperiodDesc





        

    
class FoodCropsDataset :
    def __init__(self):
        pass
    def load(self,datasetPath: str):
        pass
    def findMeasurements(self, commodityGroup:CommodityGroup = None, indicatorGroup:IndicatorGroup = None, geographicalLocation:str = None, unit:Unit = None) -> List[Measurement]:
        pass


class Volume(Unit):
    def __init__(self, id:int, name:str = "Volume"):
        super().__init__(id, "Volume")
        
class Surface(Unit):
    def __init__(self, id:int, name:str = "Surface"):
        super().__init__(id, "Surface")
        self.__name = name

class Price(Unit):
    def __init__(self, id:int, name:str):
        super().__init__(id,name)

class Weight(Unit):
    def __init__(self, id:int, name:str, multiplier:float):
        super().__init__(id,"Weight")
        self.__multiplier = multiplier
            
class Count(Unit):
    def __init__(self, id:int, name:str, what:str):
        super().__init__(id,"Count")
        self.__what = what
            
class Ratio(Unit):
    def __init__(self, id:int, name:str):
        super().__init__(id,"Ratio")
            
class UnitRatio(Ratio):
    def __init__(self, id:int, unit1:Unit, unit2:Unit):
        super().__init__(id)

    

    
class FoodCropFactory :
    def __init__(self):
        pass
    def createVolume(self,ID: int) -> Unit:
        pass
    def createPrice(self,ID: int) -> Unit:
        pass
    def createWeight(self,ID: int,weight : float) -> Unit:
        pass
    def createSurface(self,ID: int) -> Unit:
        pass
    def createCount(self,ID: int,what: str) -> Unit:
        pass
    def createRatio(self,ID: int) -> Unit:
        pass
    def createUnitRatio(self,ID: int,unit1: Unit,unit2: Unit) -> Unit:
        pass
    def createCommodity(self,group: CommodityGroup, ID: int, name: str) -> Commodity:
        pass
    def createIndicator(self,ID: int, frequency:int, freqDesc: str,geogLocation: str,indicatorGroup: IndicatorGroup,unit: Unit) -> Indicator:
        pass
    def createMeasurementType(self,ID: int,description: str) -> MeasurementType:
        pass
    def createMeasurement(self,ID: int,year: int,value: float,timeperiodId: int,timeperiodDesc: str,tipe: MeasurementType,commodity: Commodity,indicator: Indicator) -> Measurement:
        pass
