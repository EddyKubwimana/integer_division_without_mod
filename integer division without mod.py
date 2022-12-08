#integer division without a multiplication or division

def integerdiv (dividend, divisor):
    if dividend>=divisor and dividend > 0 and divisor >0:
        comp = divisor
        incr = 0
        while comp<= dividend:
            incr += 1
            comp+= divisor
             
        return incr
    elif dividend <= divisor and dividend >=0:
        return 0
    elif dividend < 0 and divisor<0:
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend>=divisor:
            comp = divisor
            incr = 0
            while comp<= dividend:
              incr += 1
              comp+=divisor
            
            return incr
    else:
        dividend = abs(dividend)
        divisor= abs(divisor)
        comp = divisor
        incr = 0
        while comp<= dividend:
            incr += 1
            comp+= divisor
             
        return -incr

#print(integerdiv(-10,10))


#finding the remainder without using %
def remainder(dividend,divisor):
    if divisor>dividend:
        return dividend
    elif divisor == dividend:
        return 0
    else:
        incr = divisor
        while dividend > incr:
            incr += divisor
            if dividend == incr:
                return 0
        incr -=divisor
        return dividend-incr
print(remainder(135676,1237),135676%1237)
        
    
        
        
                
        
