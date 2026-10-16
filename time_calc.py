# a weekly time calculator designed to run on desktop or a CASIO FXCG50 calculator.

while True:
    try:

        sunin = input('SUN TIMEIN ')
        sunin = float(sunin)
        sunout = input('SUN TIMEOUT ')
        sunout = float(sunout)
        # sunday total hours
        suntot = sunout - sunin

        monin = input('MON TIMEIN ')
        monin = float(monin) 
        monout = input('MON TIMEOUT ')
        monout = float(monout)
        # mon hours total
        montot = monout - monin


        tuein = input('TUE TIMEIN ')
        tuein = float(tuein)
        tueout = input('TUE TIMEOUT ')
        tueout = float(tueout)
        # tue hours total
        tuetot = tueout - tuein

        # if tuetot >= 6 subtract half hour for lunch
        # replace with function for optimization.
        if tuetot >= 6:
            tuetot = tuetot - 30

        wedin = input('WED TIMEIN ')
        wedin = float(wedin)
        wedout = input('WED TIMEOUT ')
        wedout = float(wendout)
        # total hours wed
        wedtot = wedout - wedin

        thrin = input('THR TIMEIN ')
        thurin = float(thurin)
        throut = input('THR TIMEOUT ')
        throut = float(throut)
        # total hours Thrusday
        thrtot = throut - thurin

        friin = input('FRI TIMEIN ')
        friin = float(friin)

        break
    
    except:
       print('INCORRECT CODE!')
       continue

# monday - thursdat total worked hours 
m_fhrs = suntot + montot + tuetot + wedtot + thrtot 

# remaining hours to wor for the week
rehrs = 40 - m_fhrs

# work until this time on friday.
worktil = friin + rehrs

print(worktil)



