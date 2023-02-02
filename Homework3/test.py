

# The HWSet class holds general data about availability, capacity, inventory, and id information.
class DroneSet:

    # Initialize private attributes
    def __init__(self):
        self.availability = 200
        self.capacity = 200
        self.checkOutQty = [0, 0, 0, 0]
        self.checkOutId = -1

    # Getter methods for availability and capacity variables
    def get_availability(self):
        return self.availability

    def get_capacity(self):
        return self.capacity

    # Methods for check out and check in
    def check_out(self, qty):
        # Decrement availability by quantity
        self.availability -= qty
        # Increment checkout id
        self.checkOutId += 1
        # Set the value in the list to the quantity
        self.checkOutQty[self.checkOutId] = qty
        return self.checkOutId

    def check_in(self, id, qty):
        # Checks if the idx is valid
        if id <= 3 and id >= 0:
            # Checks id qty matches the value in the list
            if self.checkOutQty[id] is qty:
                # Increments availability by quantity
                self.availability += qty
                return 0
            else:
                # Returns error
                return -1
        else:
            # Returns error
            return -1

    #assert hasattr(ds1, '_DroneSet__availability')
    #assert hasattr(ds1, '_DroneSet__capacity')
    #assert hasattr(ds1, '_DroneSet__checkOutQty')
    #assert hasattr(ds1, '_DroneSet__checkOutId')