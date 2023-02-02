class HWSet:

    def __init__(self, qty: int):
        # Checking if input quantity value is negative
        if qty < 0:
            raise ValueError('Capacity can not be negative')
        self.capacity = qty
        self.available = qty
        self.checked_out_list = 0

    def AddCheckoutQty(self, qty):
        # This function keeps increasing the count of checked out quantity.
        self.checked_out_list += qty

    # Get functions to return availability, capacity and checked-out quantity values
    def get_availability(self):
        return self.available

    def get_capacity(self):
        return self.capacity

    def get_checkedout_qty(self):
        return self.checked_out_list

    def check_out(self, qty):
        # Checking for negative values
        if qty < 0:
            return -2
        # Checking if the requested quantity is greater than available
        if qty > self.available:
            # Storing the excess in the 'extra' variable
            extra = qty - self.available
            # Checking out the remaining available units
            self.AddCheckoutQty(self.available)
            self.available -= self.available
            # Returning -1 to indicate that the quantity requested was greater than available.
            return -1
        # If requested quantity is less than available then go through traditional reduction
        self.available -= qty
        self.AddCheckoutQty(qty)
        return 0

    def check_in(self, qty):
        # Checking for negative values
        if qty < 0:
            return -2
        # Increasing the available units based on the check in value.
        self.available += qty
        # Should this also increase the limit of 'capacity' in future?
        return 0
