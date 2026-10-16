from time_calc import lunch, miladec

while True:
            sunin = input('SUN TIMEIN ')
            sunin = float(sunin)
            if sunin == -1:
                suntot = 0
                break
            if sunin == -2:
                suntot = 8.0
                break
            
            sunout = input('SUN TIMEOUT ')
            sunout = float(sunout)
            # sunday total hours
            suntot = miladec(sunout) - miladec(sunin)
            if suntot >= 6:
                suntot = lunch(suntot)
            break
print(suntot)