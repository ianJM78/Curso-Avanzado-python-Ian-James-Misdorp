



class Hand: 

    def __init__(self, max_weight : int):
        self.max_weight = max_weight
    
    def canLift(self, objectWeight : int) -> bool:
        """ Defines if the hand can lift the object

        Args:
            objectWeight (int): the weight of the object

        Returns:
            bool: True if the hand can lift the object, False otherwise
        """
        if self.max_weight >= objectWeight:
            return True
        else:
            False
    
    def updateWeight(self,update : int) -> None:
        """ Updates the max weight of the hand

        Args:
            update (int): the new max weight
        """
        self.max_weight = update


#! Debido a que se necesitan dos manos, no es posible hacer una herencia de una clase abstracta, ya que sino se tendrian que definir dos clases mano, que tendrian el mismo codigo

class Person():
    def __init__(self,leftHand : Hand, rightHand : Hand):
        self.leftHand = leftHand    
        self.rightHand = rightHand
        self.total_maxweight = self.leftHand.max_weight + self.rightHand.max_weight
        


    def Lifting(self, objectWeight : int) -> str:
        if self.leftHand.canLift(objectWeight) :
            return "Can lift with left hand"
        if self.rightHand.canLift(objectWeight):
            return "Can lift with right hand"
        if self.total_maxweight >= objectWeight :
            return "Can lift with both hands"
        
        return "Can't lift the object"


# Set up the person and test the lifting
person = Person(Hand(10),Hand(20))
print(person.Lifting(10))
print(person.Lifting(15))
print(person.Lifting(30))
print(person.Lifting(40))