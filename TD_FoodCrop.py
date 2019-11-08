from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import pandas as pd

class Describable(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def Describe(self) -> str :
            pass

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
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str, commodity: Commodity, indicator: Indicator):
        self.__year=year
        self.__value=value
        self.__timeperiodld=timeperiodld
        self.__timeperiodDesc=timeperiodDesc





        

    
class FoodCropsDataset :
    
    def __init__(self):
        pass
    
    
    def load(self,datasetPath: str):
        dataframe = pd.read_csv(datasetPath)
        for index, row in dataframe.iterrows():
            column_value = row["SC_Commodity_ID"]
            create 
                
            
                
    def findMeasurements(self, commodityGroup:CommodityGroup = None, indicatorGroup:IndicatorGroup = None, geographicalLocation:str = None, unit:Unit = None) -> List[Measurement]:
        pass


FCD = FoodCropsDataset()
FCD.load(r"C:\Users\hello\Documents\documents_scolaires\MINES_ALES_2A\S7\2IA\python\FeedGrains.csv")


class Volume(Unit):
    def __init__(self, id:int):
        super().__init__(id, "Volume")
        
class Surface(Unit):
    def __init__(self, id:int):
        super().__init__(id, "Surface")

class Price(Unit):
    def __init__(self, id:int):
        super().__init__(id,"Price)

class Weight(Unit):
    def __init__(self, id:int, multiplier:float):
        super().__init__(id, "Weight")
        self.__multiplier = multiplier
            
class Count(Unit):
    def __init__(self, id:int, what:str):
        super().__init__(id,"Count")
        self.__what = what
            
class Ratio(Unit):
    def __init__(self, id:int):
        super().__init__(id,"Ratio")
            
class UnitRatio(Ratio):
    def __init__(self, id:int, unit1:Unit, unit2:Unit):
        super().__init__(id)

    

    
class FoodCropFactory :
    
    commodityRegistry = dict()
    
        def __init__(self):
        self.commodityRegistry = dict()
        self.indicatorsregistry = dict()
        self.unitsRegistry = dict()
        self.measurementsTypeRegistry = dict()
        
    def createVolume(self,ID: int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Volume(ID)


    def createWeight(self,ID: int, weight:float) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Weight(ID, weight)
            
            
    def createSurface(self, ID:int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Surface(ID)
            
            
    def createCount(self, ID:int, what:str) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Count(ID,what)
    
    
    def createRatio(self, ID:int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Ratio(ID)
    
    
    def createUnitRatio(self, ID:int, unit1:Unit, unit2:Unit) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = UnitRatio(ID, unit1, unit2)
    
    def createCommodity(self, group:CommodityGroup, ID:int, name:str) -> Commodity:
        if ID in self.commodityRegistry.keys():
            return self.commodityRegistry[ID]
        else:
            self.commodityRegistry[ID] = Commodity(ID, name, group)


    def createIndicator(self, ID:int, frequency:int, freqDesc:str, geogLocation:str, indicatorGroup:IndicatorGroup, unit:Unit) -> Indicator:
        if ID in self.indicatorsregistry.keys():
            return self.indicatorsregistry[ID]
        else:
            self.indicatorsregistry[ID] = indicatorsregistry(ID, frequency, freqDesc, geogLocation, indicatorGroup, unit)


    def createMeasurement(self, ID:int, year:int, value:float, timeperiodId:int, timeperiodDesc:str, commodity:Commodity, indicator:Indicator) -> Measurement:
        if ID in self.measurementsTypeRegistry.keys():
            return self.measurementsTypeRegistry[ID]
        else:
            self.measurementsTypeRegistry[ID] = Measurement(ID, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
