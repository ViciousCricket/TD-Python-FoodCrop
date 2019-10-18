from abc import ABC, abstractmethod

class Describable(ABC):
    def __init__(self):
        super().__init__()



class FoodCropFactory :
    def __init__(self):
    def createVolume() -> Unit:
    def createPrice() -> Unit:
    def createWeight() -> Unit:
    def createSurface() -> Unit:
    def createCount() -> Unit:
    def createRatio() -> Unit:
    def createUnitRatio() -> Unit:
    def createCommodity() -> Commodity:
    def createIndicator() -> Indicator:
    
    
class FoodCropsDataset :
    def __init__(self):

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
