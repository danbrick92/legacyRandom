"""
Design Pattern: Factory Method
Pattern Type: Creational Pattern
Purpose: Create objects without exposing logic to client.
         Client uses common interface to create new object.
         Removes tight coupling with the class hierarchy of the library.
"""
class TwoWheeler():
    def printVehicle(self):
        print("Two Wheels!")

class ThreeWheeler():
    def printVehicle(self):
        print("Three Wheels!")

class FourWheeler():
    def printVehicle(self):
        print("Four Wheels!")

def Vehicle(num_wheels):
    if num_wheels == 2:
        return TwoWheeler()
    elif num_wheels == 3:
        return ThreeWheeler()
    elif num_wheels == 4:
        return FourWheeler()
    else:
        return None

if __name__ == '__main__':
    for i in range(2,5):
        veh = Vehicle(i)
        veh.printVehicle()