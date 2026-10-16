# a weekly time calculator designed to run on desktop or a CASIO FXCG50 calculator.

while True:
    try:

        sunin = input('SUN TIMEIN ')
        sunin = float(sunin)
        sunout = input('SUN TIMEOUT ')
        sunout = float(sunout)

        monin = input('MON TIMEIN ')
        monin = float(monin) 
        monout = input('MON TIMEOUT ')
        monout = float(monout)

        tuein = input('TUE TIMEIN ')
        tuein = float(tuein)
        tueout = input('TUE TIMEOUT ')
        tueout = float(tueout)

        wedin = input('WED TIMEIN ')
        wedin = float(wedin)
        wedout = input('WED TIMEOUT ')
        wendout = float(wendout)

        thrin = input('THR TIMEIN ')
        thurin = float(thurin)
        throut = input('THR TIMEOUT ')
        throut =float(throut)

        friin = input('FRI TIMEIN ')
        friin = float(friin)

        break
    
    except:
       print('INCORRECT CODE!')
       continue
    
