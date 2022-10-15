import interface
import mover
import log

result = ''
log_text = 'Начало сеанса'

def Move():
    global result
    global log_text
    while interface.close == 0:
        log.Log(log_text)
        interface.Get_data(result, interface.equation)
        result = mover.Calc(interface.equation)
        result = str(result).replace('[', '').replace(']', '')
        interface.equation = f'{interface.equation}={result}'
        log_text = interface.equation





