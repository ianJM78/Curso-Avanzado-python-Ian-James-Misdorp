from abc import ABC, abstractmethod


class PackedItem:
    def __init__(self, name : str , cost : float ) -> None:
        self.name = name
        self.cost = cost
    
    def getCost(self) -> float:
        """ Gets the cost of the item

        Returns:
            float: the cost of the item
        """
        return self.cost
    
    def getName(self) -> str:
        """ Gets the name of the item

        Returns:
            str: the name of the item
        """
        return self.name
    


class SHIPMENTS(ABC):
    def __init__(self, shipmentCost : float , shipmenntTime : float , Item :PackedItem ) -> None:
        self.shipmentCost = shipmentCost
        self.shipmenntTime = shipmenntTime
        self.Item = Item
    
    @abstractmethod
    def calculateCost(self) -> float:
        pass

    @abstractmethod
    def get_shipmentTime(self) -> float:
        pass







class StandardShipment(SHIPMENTS):

    def calculateCost(self) -> float:
        """ Calculates the cost of the shipment

        Returns:
            float: the cost of the shipment
        """
        return self.shipmentCost + self.Item.getCost()
    
    def get_shipmentTime(self) -> float:
        """ Gets the time of the shipment

        Returns:
            float: the time of the shipment
        """
        return self.shipmenntTime
    


class ExpressShipment(SHIPMENTS):

    def calculateCost(self) -> float:
        """ Calculates the cost of the shipment (2500 more than the standard)

        Returns:
            float: the cost of the shipment
        """
        return self.shipmentCost + self.Item.getCost() + 2500
    
    def get_shipmentTime(self) -> float:
        """ Gets the time of the shipment (2 hours less than the standard)

        Returns:
            float: the time of the shipment
        """
        return self.shipmenntTime - 2
    

class PersonalizedShipment(SHIPMENTS):
    def __init__(self, shipmentCost : float , shipmenntTime : float, distance : float) -> None:
        super().__init__(shipmentCost, shipmenntTime)
        self.distance = distance

    def calculateCost(self) -> float:
        """ Calculates the cost of the shipment (100 per km)

        Returns:
            float: the cost of the shipment
        """
        return self.shipmentCost + self.distance*100
    
    def get_shipmentTime(self) -> float:
        """ Gets the time of the shipment

        Returns:
            float: the time of the shipment
        """
        return self.shipmenntTime



# Main 

item = PackedItem("Item1", 1000)

while True:
    choice = input("Choose the type of shipment (1: Standard, 2: Express, 3: Personalized): ")
    if choice == "1":
        shipment = StandardShipment(500, 5, item)
        break
    elif choice == "2":
        shipment = ExpressShipment(500, 5, item)
        break
    elif choice == "3":
        distance = float(input("Enter the distance: "))
        shipment = PersonalizedShipment(500, 5, distance, item)
        break
    else:
        print("Invalid choice")

print(f"Item: {item.getName()}")
print(f"Total cost: {shipment.calculateCost()}")
print(f"Total time: {shipment.get_shipmentTime()}\n")
