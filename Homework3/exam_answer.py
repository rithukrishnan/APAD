# The HWSet class holds general data about availability, capacity, inventory, and id information.
class DroneSet:

    # Initialize private attributes
    def __init__(self):
        self.__availability = 200
        self.__capacity = 200
        self.__checkOutQty = [0, 0, 0, 0]
        self.__checkOutId = -1

    # Getter methods for availability and capacity variables
    def get_availability(self):
        return self.__availability

    def get_capacity(self):
        return self.__capacity

    # Methods for check out and check in
    def check_out(self, qty):
        # Decrement availability by quantity
        self.__availability -= qty
        # Increment checkout id
        self.__checkOutId += 1
        # Set the value in the list to the quantity
        self.__checkOutQty[self.__checkOutId] = qty
        return self.__checkOutId

    def check_in(self, id, qty):
        # Checks if the idx is valid
        if id <= 3 and id >= 0:
            # Checks id qty matches the value in the list
            if self.__checkOutQty[id] is qty:
                # Increments availability by quantity
                self.__availability += qty
                return 0
            else:
                # Returns error
                return -1
        else:
            # Returns error
            return -1
