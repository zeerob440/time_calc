'''
VERSION: Alpha 0, A weekly day shift time card calculator designed to run on desktop or a Casio fx-CG50 calculator.
time_calc.py simplifies an annoying task I have to complete once a week. 

FEATURES: time_calc can run on desktop or a Casio fx-CG50 calculator

REQs: Python 3.13 OR MicroPython 1.9.4| Casio fx-CG50| Desktop computer

Proudly Engineered by Zachary Roberts 15 OCT 2026

"A watched clock never ticks."
'''

# converts military time to decimal time
def miladec(time):
    time = (time // 100) + (time % 100) / 60
    return time

# decrement -= .50 time for days worked >= 6 hours
def lunch(mthirty):
    mthirty -= .50
    return mthirty

# convert decimal military time to standard military time
def decamil(time):
    hours = int(time)
    minutes = (time % 1) * 60
    return hours * 100 + minutes

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
            # Tuesday total hours
            tuetot = miladec(tueout) - miladec(tuein)
            if tuetot >= 6:
                tuetot = lunch(tuetot)
            break
        

        # Wednesday
        while True:
            wedin = input('WED TIMEIN ')
            wedin = float(wedin)
            if wedin == -1:
                wedtot = 0
                break
            if wedin == -2:
                wedtot = 8.0
                break
                                    
            wedout = input('WED TIMEOUT ')
            wedout = float(wedout)
            # Wednesday total hours
            wedtot = miladec(wedout) - miladec(wedin)
            if wedtot >= 6:
                wedtot = lunch(wedtot)
            break

        # Thursday
        while True:
            thrin = input('THR TIMEIN ')
            thrin = float(thrin)
            if thrin == -1:
                thrtot = 0
                break
            if thrin == -2:
                thrtot = 8.0
                break
                                            
            throut = input('THR TIMEOUT ')
            throut = float(throut)
                # Wednesday total hours
            thrtot = miladec(throut) - miladec(thrin)
            if thrtot >= 6:
                    thrtot = lunch(thrtot)
            break

        friin = input('FRI TIMEIN ')
        friin = float(friin)
        friin = miladec(friin)

        break
    
    except:
       print('INCORRECT CODE!')
       continue

# monday - thursday total worked hours 
m_fhrs = suntot + montot + tuetot + wedtot + thrtot
# print check for test
print('hours so far', m_fhrs) 

# remaining hours to work for the week
rehrs = 40 - m_fhrs
#print check
print('hours rmain', rehrs)

if rehrs >= 6:
    fri_l = .50
    # work until this time on Friday if >= 6 hours remain
    worktil = decamil((friin + rehrs + fri_l)) 

    print(worktil)
    # otherwise work until this time
elif rehrs <= 6:
    worktil = decamil((friin + rehrs))
    print(worktil)


