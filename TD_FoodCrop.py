from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import pandas as pd

# Fonction qui nous permet de réaliser l'intersection de deux listes, qui nous servira pour la méthode de recherche
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3  

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
    FEED_GRAINS = "Feed grains"
    ANIMAL_PROTEIN_FEEDS = "Animal protein feeds"
    GRAIN_PROTEIN_FEEDS = "Grain protein feeds"
    PROCESSED_FEEDS = "Processed feeds"
    ENERGY_FEEDS = "Energy feeds"
    OTHER = "Other"

class Commodity(Describable) :
    def __init__(self, id : int, name : str, group : CommodityGroup):
        self.id = id
        self.__name = name
        self.__group = group
 
    def Describe(self) -> str :
        res = "nom : "+ self.__name + " commodity group:" + self.__group.value
        return res     
    
class Unit(ABC):
    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name
        self.id = id
    
    def Describe(self) -> str :
        res = "nom :" + self.name
        return res

class Indicator(Describable) :
    def __init__(self, id :str, frequency : int, frequencyDesc : str, geogLocation : str, indicatorGroup : IndicatorGroup, unit : Unit):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit
    
    def Describe(self) -> str :
        res = "index :" + str(self.indicatorGroup) + " unité :" + self.unit.Describe() + " fréquence :" + str(self.__frequency) + self.__frequencyDesc + " geolocalisation :" + self.__geogLocation
        return res

class Measurement :
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str, commodity: Commodity, indicator: Indicator):
        self.__year=year
        self.__value=value
        self.__timeperiodld=timeperiodld
        self.__timeperiodDesc=timeperiodDesc
        self.indicator = indicator
        self.commodity = commodity
    
    def Describe(self) -> str :
        res = "année : " + str(self.__year) + "\n valeur :" + str(self.__value) + "\n time periode :" + str(self.__timeperiodld) + self.__timeperiodDesc + "\n commodity :" + self.commodity.Describe() + "\n indicator :" + self.indicator.Describe()
        return res
        
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
        
    def affiche(self):
        print(len(self.commodityRegistry))
        print(len(self.indicatorsRegistry))
        print(len(self.unitsRegistry))
        print(len(self.measurementsRegistry))
        print(self.measurementsRegistry[2].Describe())
        
        #Toutes les méthodes create suivent le même principe : on vérifie que l'ID est bien dans le dictionnaire, sinon on la rajoute
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

    def createWeight(self,ID: int, mult:float) -> Unit:
        if ID in self.unitsRegistry.keys():
            return self.unitsRegistry[ID]
        else:
            self.unitsRegistry[ID] = Weight(ID, mult)
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

    
class FoodCropsDataset :

    def __init__(self, factory : FoodCropFactory):
        self.factory = factory
        self.commodityGroupIndex = dict()
        self.indicatorGroupIndex = dict()
        self.geographicalLocationIndex = dict()
        self.unitIndex = dict()
        self.measurementListe = []
        
    #Initialisation du fichier et récupération des mesures (measurements)
    def load(self,datasetPath: str):
        
        dataframe = pd.read_csv(datasetPath)
    
        price = []
        volume = ["Million bushels", "Bushels","Gallons","1,000 liters"]
        weight = ["1,000 metric tons","Million metric tons", "1,000 tons","Ton"]
        surface = ["Million acres","1,000 acres","1,000 hectare"]
        count = ["Million animal units","Index (1984=100)","Carloads originated"]
        ratio = ["Bushels per acre","Metric tons per hectare","Cents per pound","Dollars per cwt","Dollars per short ton","Ratio","Dollars per bushel","Dollars per ton","Tons per acre"]
        
        for index, row in dataframe.iterrows():
            
            id_u = row["SC_Unit_ID"]
            name_u = row["SC_Unit_Desc"]
            if name_u in volume :
                unit = self.factory.createVolume(id_u)
            if name_u in price :
                unit = self.factory.createPrice(id_u)
            if name_u in weight :
                mult = 0
                if (name_u == "1,000 metric tons" or name_u == "1,000 tons"): 
                    mult = 1000
                if (name_u == "Million metric tons"):
                    mult = 1000000
                unit = self.factory.createWeight(id_u, mult)
            if name_u in surface :
                unit = self.factory.createSurface(id_u)
            if name_u in count :
                unit = self.factory.createCount(id_u, name_u)
            if name_u in ratio :
                unit = self.factory.createRatio(id_u)
                
            
            
            id_ind = row["SC_Attribute_ID"]
            id_freq = row["SC_Frequency_ID"]
            freq_name = row["SC_Frequency_Desc"]
            geo_name = row["SC_GeographyIndented_Desc"]
            id_group_ind = row["SC_Group_ID"]
            name_ig = row["SC_Group_Desc"]
            indicator = self.factory.createIndicator(id_ind, id_freq, freq_name, geo_name, id_group_ind, unit)
            
            name_cg = row["SC_GroupCommod_Desc"]
            id_c = row["SC_Commodity_ID"]
            name_c = row["SC_Commodity_Desc"]
            for a in CommodityGroup :
                if name_cg == a.value :
                        commodity = self.factory.createCommodity(a, id_c, name_c)
            
            
            year = row["Year_ID"]
            value = row["Amount"]
            tp_id = row["Timeperiod_ID"]
            tp_d = row["Timeperiod_Desc"]
            measurement = self.factory.createMeasurement(index, year, value, tp_id, tp_d, commodity, indicator)

            #Création des dictionnaires de mesures pour faciliter la recherche
            if geo_name not in self.geographicalLocationIndex.keys() :
                self.geographicalLocationIndex[geo_name] = []
                
            if name_u not in self.unitIndex.keys() :
                self.unitIndex[name_u] = []
            
            if name_ig not in self.indicatorGroupIndex.keys() :
                self.indicatorGroupIndex[name_ig] = []
            
            if name_cg not in self.commodityGroupIndex.keys() :
                self.commodityGroupIndex[name_cg] = []

            a = self.unitIndex[name_u]
            self.unitIndex[name_u] = a + [measurement]
            
            a = self.geographicalLocationIndex[geo_name]
            self.geographicalLocationIndex[geo_name] = a + [measurement]

            a = self.commodityGroupIndex[name_cg]
            self.commodityGroupIndex[name_cg] = a + [measurement]

            a = self.indicatorGroupIndex[name_ig]
            self.indicatorGroupIndex[name_ig] = a + [measurement]
            
            self.measurementListe.append(measurement)
               

    def findMeasurements(self, commodityGroup:CommodityGroup = None, indicatorGroup:IndicatorGroup = None, geographicalLocation:str = None, unit:Unit = None) -> List[Measurement]:
        
        if commodityGroup == None :
            CG = self.measurementListe
        else :
            CG = self.commodityGroupIndex[commodityGroup.value]

            
        if indicatorGroup == None :
            IG = self.measurementListe
        else :
            IG = self.indicatorGroupIndex[indicatorGroup.value]
        
        
        if geographicalLocation == None :
            GL = self.measurementListe
        else :
            GL = self.geographicalLocationIndex[geographicalLocation]
        
        if unit == None :
            U = self.measurementListe
        else :
            U = self.unitIndex[unit]
        res = intersection(intersection(CG, IG),intersection(GL,U))
        
        for i in res :
            print(i.Describe()+"\n"+"\n")
        
        

fcf = FoodCropFactory()
FCD = FoodCropsDataset(fcf)
FCD.load(r"C:\Users\hello\Documents\documents_scolaires\MINES_ALES_2A\S7\2IA\python\FeedGrains_complet.csv")
FCD.findMeasurements(CommodityGroup.COARSE_GRAINS, IndicatorGroup.QUANTITIES_FED, "United States", "Dollars per bushel")
