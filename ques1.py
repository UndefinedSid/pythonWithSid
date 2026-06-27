my_vehicle = input("Enter my_vehicle type (truck/bus/car/cycle/motorcycle/scooter): ").lower()

entry_hr = int(input("Enter entry hour: "))
entry_min = int(input("Enter entry minute: "))

exit_hr = int(input("Enter exit hour: "))
exit_min = int(input("Enter exit minute: "))

entry_total = entry_hr * 60 + entry_min
exit_total = exit_hr * 60 + exit_min

final_min = exit_total - entry_total

hr = final_min // 60
min = final_min % 60

print("Parking Time =", hr, "hours", min, "minutes")

charge = 0

if my_vehicle in ["truck", "bus"]:
    if hr <= 3:
        charge = hr * 20
    else:
        charge = (3 * 20) + ((hr - 3) * 30)

elif my_vehicle == "car":
    if hr <= 3:
        charge = hr * 10
    else:
        charge = (3 * 10) + ((hr - 3) * 20)

elif my_vehicle in ["cycle", "motorcycle", "scooter"]:
    if hr <= 3:
        charge = hr * 5
    else:
        charge = (3 * 5) + ((hr - 3) * 10)

else:
    print("Invalid my_vehicle type")

print("Parking Charge = Rs.", charge)