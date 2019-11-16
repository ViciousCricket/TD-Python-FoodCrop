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
    EXPORTS_AND_IMPORTS = "Exports and imports"
    SUPPLY_AND_USE = "Supply and use"
    PRICES = "Prices"
    FEED_PRICE_RATIOS = "Feed price ratios"
    QUANTITIES_FED = "Quantities fed"
    TRANSPORTATION = "Transportation"
    ANIMAL_UNIT_INDEXES = "Animal unit indexes"
    
class CommodityGroup(Enum):
    CORN = "Corn"
    BARLEY = "Barley"
    OATS = "Oats"
    SORGHUM = "Sorghum"
    BYPRODUCT_FEEDS ="Byproduct feeds"
    COARSE_GRAINS = "Coarse grains"
    HAY = "Hay"
    ANIMAL_PROTEIN_FEEDS = "Animal protein feeds"
    GRAIN_PROTEIN_FEEDS = "Grain protein feeds"
    PROCESSED_FEEDS = "Processed feeds"
    ENERGY_FEEDS = "Energy feeds"
    OTHER = "Other"

class Commodity(Describable) :
    def __init__(self, id : int, name : str, group : CommodityGroup):
        self.id = id
        self.__name = name
 
    def Describe(self) -> str :
        return "s"       
    
class Unit(ABC):
    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name
        self.id = id
    
    def Describe(self) -> str :
        return "s"

class Indicator(Describable) :
    def __init__(self, id :str, frequency : int, frequencyDesc : str, geogLocation : str, indicatorGroup : IndicatorGroup, unit : Unit):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation
    
    def Describe(self) -> str :
        return "s"

class Measurement :
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str, commodity: Commodity, indicator: Indicator):
        self.__year=year
        self.__value=value
        self.__timeperiodld=timeperiodld
        self.__timeperiodDesc=timeperiodDesc
    
    def Describe(self) -> str :
        return "s"
        
class Volume(Unit):
    def __init__(self, id:int):
        super().__init__(id, "Volume")
    
class Surface(Unit):
    def __init__(self, id:int):
        super().__init__(id, "Surface")

class Price(Unit):
    def __init__(self, id:int):
        super().__init__(id,"Price")

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
        super().__init__(id, "UnitRatio")



class FoodCropFactory :
    
    def __init__(self):
        self.commodityRegistry = dict()
        self.indicatorsRegistry = dict()
        self.unitsRegistry = dict()
        self.measurementsRegistry = dict()
        
    def createVolume(self,ID: int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Volume(ID)
            return self.unitsRegistry[ID]

    def createPrice(self,ID: int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Price(ID)
            return self.unitsRegistry[ID]

    def createWeight(self,ID: int, weight:float) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Weight(ID, weight)
            return self.unitsRegistry[ID]
            
    def createSurface(self, ID:int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Surface(ID)
            return self.unitsRegistry[ID]
            
    def createCount(self, ID:int, what:str) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Count(ID,what)
            return self.unitsRegistry[ID]
    
    def createRatio(self, ID:int) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Ratio(ID)
            return self.unitsRegistry[ID]
    
    def createUnitRatio(self, ID:int, unit1:Unit, unit2:Unit) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = UnitRatio(ID, unit1, unit2)
            return self.unitsRegistry[ID]
    
    def createCommodity(self, group:CommodityGroup, ID:int, name:str) -> Commodity:
        if ID in self.commodityRegistry.keys():
            return self.commodityRegistry[ID]
        else:
            self.commodityRegistry[ID] = Commodity(ID, name, group)
            return self.commodityRegistry[ID]


    def createIndicator(self, ID:int, frequency:int, freqDesc:str, geogLocation:str, indicatorGroup:IndicatorGroup, unit:Unit) -> Indicator:
        if ID in self.indicatorsRegistry.keys():
            return self.indicatorsRegistry[ID]
        else:
            self.indicatorsRegistry[ID] = Indicator(ID, frequency, freqDesc, geogLocation, indicatorGroup, unit)
            return self.indicatorsRegistry[ID]

    def createMeasurement(self, ID:int, year:int, value:float, timeperiodId:int, timeperiodDesc:str, commodity:Commodity, indicator:Indicator) -> Measurement:
       self.measurementsRegistry[ID] = Measurement(ID, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
       return self.measurementsRegistry[ID]

        
fcf = FoodCropFactory()        

    
class FoodCropsDataset :

    def __init__(self):
        pass
    
    def load(self,datasetPath: str):
        dataframe = pd.read_csv(datasetPath)
        
        liste = []
        price = []
        volume = ["Million bushels", "Bushels","Gallons","1,000 liters"]
        weight = ["1,000 metric tons","Million metric tons", "1,000 tons","Ton"]
        surface = ["Million acres","1,000 acres","1,000 hectare"]
        count = ["Million animal units","Index (1984=100)","Carloads originated"]
        ratio = ["Bushels per acre","Metric tons per hectare","Cents per pound","Dollars per cwt","Dollars per short ton","Ratio","Dollars per bushel","Dollars per ton","Tons per acre"]
        
        for index, row in dataframe.iterrows():
#            name_u = row["SC_Unit_Desc"]
#            if name_u not in liste :
#                liste.append(name_u)
#                print (name_u)
#        print(liste)
            
        
            id_u = row["SC_Unit_ID"]
            name_u = row["SC_Unit_Desc"]
            if name_u in volume :
                unit = fcf.createVolume(id_u)
            if name_u in price :
                unit = fcf.createPrice(id_u)
            if name_u in weight :
                unit = fcf.createWeight(id_u, 5)
            if name_u in surface :
                unit = fcf.createSurface(id_u)
            if name_u in count :
                unit = fcf.createCount(id_u, "d")
            if name_u in ratio :
                unit = fcf.createRatio(id_u)
                
            
            
            id_ind = row["SC_Attribute_ID"]
            id_freq = row["SC_Frequency_ID"]
            freq_name = row["SC_Frequency_Desc"]
            geo_name = row["SC_GeographyIndented_Desc"]
            id_group_ind = row["SC_Group_ID"]
            indicator = fcf.createIndicator(id_ind, id_freq, freq_name, geo_name, id_group_ind, unit)
            
            name_cg = row["SC_GroupCommod_Desc"]
            id_c = row["SC_Commodity_ID"]
            name_c = row["SC_Commodity_Desc"]
            for a in CommodityGroup :
                if name_cg == a.value :
                        commodity = fcf.createCommodity(a, id_c, name_c)
            
            year = row["Year_ID"]
            value = row["Amount"]
            tp_id = row["Timeperiod_ID"]
            tp_d = row["Timeperiod_Desc"]
            fcf.createMeasurement(index, year, value, tp_id, tp_d, commodity, indicator)
            
            
                
    def findMeasurements(self, commodityGroup:CommodityGroup = None, indicatorGroup:IndicatorGroup = None, geographicalLocation:str = None, unit:Unit = None) -> List[Measurement]:
        pass

FCD = FoodCropsDataset()
FCD.load(r"C:\Users\hello\Documents\documents_scolaires\MINES_ALES_2A\S7\2IA\python\FeedGrains.csv")

    

    
