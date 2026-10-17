'''
VERSION: Alpha 0, A weekly day shift time card calculator designed to run on desktop or a Casio fx-CG50 calculator.
time_calc.py simplifies an annoying task I have to complete once a week. This is optimized for a specif organization's business rules.

FEATURES: time_calc can run on desktop or a Casio fx-CG50 calculator| If >= 6 hrs worked It subtracts .5 hours/ 30min for lunch as per business rules.

REQs: Casio fx-CG50 with MicroPython 1.9.4 OR Desktop computer with Python (tested Python 3.13)

ASSUMPTIONS: 40-hour target workweek| Military time input (HHMM)|  -1 = No hours worked|  -2 = 8 hours PTO| Shifts do not cross midnight

Proudly Engineered by Zachary Roberts 16 OCT 2026

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
            # user menu
            print('IN MIL TIME')
            print('-1 = 0 HRS')
            print('-2 = 8 HRS PTO')

            sunin = input('SUN TIMEIN ')
            # input validation: 4 chars or sentinel only
            if len(sunin) != 4 and sunin not in ('-1', '-2'):
                raise ValueError
            sunin = float(sunin)
            if sunin == -1:
                suntot = 0
                break
            if sunin == -2:
                suntot = 8.0
                break
            
            sunout = input('SUN TIMEOUT ')
            if len(sunout) != 4:
                raise ValueError
            sunout = float(sunout)
            # sunday total hours
            suntot = miladec(sunout) - miladec(sunin)
            if suntot >= 6:
                suntot = lunch(suntot)
            break

        # Monday
        while True:
            monin = input('MON TIMEIN ')
            # input validation: 4 chars or sentinel only
            if len(monin) != 4 and monin not in ('-1', '-2'):
                raise ValueError
            monin = float(monin)
            if monin == -1:
                montot = 0
                break
            if monin == -2:
                montot = 8.0
                break
                    
            monout = input('MON TIMEOUT ')
            if len(monout) != 4:
                raise ValueError
            monout = float(monout)
            # sunday total hours
            montot = miladec(monout) - miladec(monin)
            if montot >= 6:
                    montot = lunch(montot)
            break

        # Tuesday
        while True:
            tuein = input('TUE TIMEIN ')
            # input validation: 4 chars or sentinel only
            if len(tuein) != 4 and tuein not in ('-1', '-2'):
                raise ValueError
            tuein = float(tuein)
            if tuein == -1:
                tuetot = 0
                break
            if tuein == -2:
                tuetot = 8.0
                break
                            
            tueout = input('TUE TIMEOUT ')
            if len(tueout) != 4:
                raise ValueError
            tueout = float(tueout)
            # Tuesday total hours
            tuetot = miladec(tueout) - miladec(tuein)
            if tuetot >= 6:
                tuetot = lunch(tuetot)
            break
        

        # Wednesday
        while True:
            wedin = input('WED TIMEIN ')
            # input validation: 4 chars or sentinel only 
            if len(wedin) != 4 and wedin not in('-1', '-2'):
                raise ValueError
            wedin = float(wedin)
            if wedin == -1:
                wedtot = 0
                break
            if wedin == -2:
                wedtot = 8.0
                break
                                    
            wedout = input('WED TIMEOUT ')
            if len(wedout) != 4:
                raise ValueError
            wedout = float(wedout)
            # Wednesday total hours
            wedtot = miladec(wedout) - miladec(wedin)
            if wedtot >= 6:
                wedtot = lunch(wedtot)
            break

        # Thursday
        while True:
            thrin = input('THR TIMEIN ')
            # input validation: 4 chars or sentinel only
            if len(thrin) != 4 and thrin not in ('-1', '-2'):
                raise ValueError
            thrin = float(thrin)
            if thrin == -1:
                thrtot = 0
                break
            if thrin == -2:
                thrtot = 8.0
                break
                                            
            throut = input('THR TIMEOUT ')
            if len(throut) != 4:
                raise ValueError
            throut = float(throut)
                # Wednesday total hours
            thrtot = miladec(throut) - miladec(thrin)
            if thrtot >= 6:
                    thrtot = lunch(thrtot)
            break

        friin = input('FRI TIMEIN ')
        if len(friin) != 4:
            raise ValueError
        friin = float(friin)
        friin = miladec(friin)

        break
    
    except:
       print('INCORRECT INPUT!')
       continue

# monday - thursday total worked hours 
m_fhrs = suntot + montot + tuetot + wedtot + thrtot

# remaining hours to work for the week
rehrs = 40 - m_fhrs
#print check
print('HRS REMAIN %.2f' % rehrs)

if rehrs >= 6:
    fri_l = .50
    # work until this time on Friday if >= 6 hours remain
    worktil = decamil((friin + rehrs + fri_l))
    # convert to int for std military time readability
    worktil = int(round(worktil))
    print('CLOCKOUT ' , worktil) 
    
    # otherwise work until this time
elif rehrs <= 6:
    worktil = decamil((friin + rehrs))
    # convert to int for std military time readability
    worktil = int(round(worktil))
    print('CLOCKOUT ',worktil)

print('PROGRAM COMPLETE')
    


