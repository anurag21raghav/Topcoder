#Language : Python 2.7


#Required value "t" should be such that teacher have to attend class for the minimum time.
#Hence, the total time acquired in coming to the class and the remaining time after the teacher leave the class can maximum be "d".

#So, t**2 + t <= d.

#As in programming, direct formula can sometimes lead to precision errors, we will check the neighbouring values too to satisfy the equation.


import math
class QuadraticLaw:
    def getTime(self, d):
        temp = int(math.floor(((float(float(math.sqrt(1+(4*d)))) - 1))/2))
        if (temp+(temp*temp))>d:
            return temp-1
        if ((temp+1) + (temp+1)*(temp+1))>d:
            return temp
        if ((temp+2) + (temp+2)*(temp+2))>d:
            return temp+1
