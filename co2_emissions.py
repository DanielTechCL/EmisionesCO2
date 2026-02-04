while True:
    kilometers = input('This program says the CO2 emission per kilometer of the Hyundai Santa Fe 2018\nSay a number over 0 and the program will interptreted it in kilometers, or say stop to stop the program\n')
    if kilometers == "stop":
        break
    kilometers = float(kilometers)
    emissions = float(0.215 * kilometers)
    print('The emissions of CO2 that you made in your trable are', emissions, 'Kg of CO2')
    if kilometers <= 0:
        print("Say a number over 0")