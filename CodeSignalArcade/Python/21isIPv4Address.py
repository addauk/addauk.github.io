def solution(inputString):
    bita = inputString.split(".")
    if len(bita) != 4:
        return False
    for ip in bita:
        if len(ip)>1:
            if ip[0] == '0':
                return False
        try:
            intip = int(ip)
        except (TypeError,ValueError):
            return False          
        if not 0 <= intip <=255:
            return False
            
    return True
            

