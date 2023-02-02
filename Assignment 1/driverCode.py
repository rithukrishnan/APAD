import hardwareSet

hwSet1 = hardwareSet.HWSet(250)
print("Total Capacity is units: ", hwSet1.get_capacity())

print("Total available units is : ", hwSet1.get_availability())

test = [20, 200]
for i in test:
    err = hwSet1.check_out(i)
    if err == 0:
        print("Total available units after checkout of : ", i, " is ", hwSet1.get_availability())
        print("Number of total checkedout units is ", hwSet1.get_checkedout_qty())
    else:
        print("Total available units after checkout of : ", i, " is ", hwSet1.get_availability())
        print("Number of total checkedout units is ", hwSet1.get_checkedout_qty())
        print("Couldnt checkout requested amount")

hwSet1.check_in(180)
print("Number units available after checkin is ", hwSet1.get_availability())