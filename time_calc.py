# a weekly time calculator designed to run on desktop or a Casio FXCG50 calculator.

# converts military time to decimal time
def miladec(time):
    time = (time // 100) + (time % 100) / 60
    return time

# decrement -= .50 time for days worked >= 6 hours
def lunch(mthirty):
    mthirty -= .50
    return mthirty

while True:
    try:
        # input times in military time
        # input -1 for 0 hours worked
        # -2 for 8 hrs PTO

        # Sunday
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

        # Monday
        while True:
            monin = input('MON TIMEIN ')
            monin = float(monin)
            if monin == -1:
                montot = 0
                break
            if monin == -2:
                montot = 8.0
                break
                    
            monout = input('MON TIMEOUT ')
            monout = float(monout)
            # sunday total hours
            montot = miladec(monout) - miladec(monin)
            if montot >= 6:
                    montot = lunch(montot)
            break

        # Tuesday
        while True:
            tuein = input('TUE TIMEIN ')
            tuein = float(tuein)
            if tuein == -1:
                tuetot = 0
                break
            if tuein == -2:
                tuetot = 8.0
                break
                            
            tueout = input('TUE TIMEOUT ')
            tueout = float(tueout)
            # sunday total hours
            tuetot = miladec(tueout) - miladec(tuein)
            if tuetot >= 6:
                tuetot = lunch(tuetot)
            break
        

        # Wednesday
        

        wedin = input('WED TIMEIN ')
        wedin = float(wedin)
        wedout = input('WED TIMEOUT ')
        wedout = float(wedout)
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

# monday - thursday total worked hours 
m_fhrs = suntot + montot + tuetot + wedtot + thrtot 

# remaining hours to wor for the week
rehrs = 40 - m_fhrs

# work until this time on friday.
worktil = friin + rehrs

print(worktil)



