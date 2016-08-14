#note to users: I wrote the code to use myself for an assignment, hence it is not very user friendly.
#therefore, do the following to manipulate the output:
#to change the options from put to call or vice versa look for the part in the code that populates euroV[][] and amV[][]. Change the code such that either the function putPayoff() or callPayoff() is used, as desired. Theres one instance in the euroV code (line 68) and two instances in the amV code (lines 83 & 91).
#to choose if the option should be calculated on the asset or on the futures contract, again look at the code populating euroV[][] and amV[][] and change the parts mentioning "S", the stock price, to "F", the futures price. Theres one instance in the euroV code (line 68) and two instances in the amV code (lines 83 & 91).
#change the parameters like strike, expiry, period at will.

import math
import copy

#market and option parameters:
So = 100 #current stock value
r = 0.02 #risk-free interest rate
voli = 0.30 #volatility
c = 0.01 #dividend rate
T = 0.25 #expiry in years
K = 110 #strike price

#binomial model parameters:
n = 5 #number of periods
dt = T/n #size of single time step
R = math.exp(r*dt)
u = math.exp(voli*math.sqrt(dt))
d = 1/u
q = (math.exp((r-c)*dt) - d)/(u - d)


#the payoff function for a call with strike E on asset with price S
def callPayoff(S,K):
    if (S - K) > 0:
        return (S - K)
    else:
        return 0

#the payoff function for a put with strike E on asset with price S
def putPayoff(S,K):
    if (K - S) > 0:
        return (K - S)
    else:
        return 0

#populating S, the array with the stock value at each node
S = [[0 for x in range(n+1)] for y in range(n+1)]
S[0][0] = So
i = 1
while i <= n:
	j = 0
	while j < i:
		S[i][j] = u*S[i-1][j]
		j = j + 1
	S[i][j] = d*S[i-1][j-1]
	i = i + 1

 
#populating F, the array with the futures value on S at each node
F = copy.deepcopy(S)
i = n
while i > 0:
	j = 0
	while j < i:
		F[i-1][j] = q*F[i][j] + (1-q)*F[i][j+1]
		j = j + 1
	i = i - 1
 
#populating euroV, the value array for a european option
euroV = [[0 for x in range(n+1)] for y in range(n+1)]
j = 0
while j <= n:
	euroV[n][j] = callPayoff(S[n][j],K)
	j = j + 1

i = n - 1
while i >= 0:
	j = 0
	while j <= i:
		euroV[i][j] = (q*euroV[i+1][j] + (1-q)*euroV[i+1][j+1])/R
		j = j + 1
	i = i - 1

#populating amV, the value array for an american option
amV = [[0 for x in range(n+1)] for y in range(n+1)]
j = 0
while j <= n:
	amV[n][j] = callPayoff(S[n][j],K)
	j = j + 1

i = n - 1
while i >= 0:
    j = 0
    while j <= i:
        optionValue = (q*amV[i+1][j] + (1-q)*amV[i+1][j+1])/R
        exerciseValue = callPayoff(S[i][j],K)
        if optionValue > exerciseValue:
            amV[i][j] = optionValue
        elif optionValue == exerciseValue:
            amV[i][j] = exerciseValue
        else:
            amV[i][j] = exerciseValue
        j = j + 1
    i = i - 1

"""
#chooser problem:

#call matrix:
#filling cCallV, call array for chooser problem
cCallV = [[0 for x in range(n+1)] for y in range(n+1)]
j = 0
while j <= n:
	cCallV[n][j] = callPayoff(S[n][j],K)
	j = j + 1

i = n - 1
while i >= 0:
	j = 0
	while j <= i:
		cCallV[i][j] = (q*cCallV[i+1][j] + (1-q)*cCallV[i+1][j+1])/R
		j = j + 1
	i = i - 1

#filling cPutV, the put array for the chooser problem
cPutV = [[0 for x in range(n+1)] for y in range(n+1)]
j = 0
while j <= n:
	cPutV[n][j] = putPayoff(F[n][j],K)
	j = j + 1

i = n - 1
while i >= 0:
	j = 0
	while j <= i:
		cPutV[i][j] = (q*cPutV[i+1][j] + (1-q)*cPutV[i+1][j+1])/R
		j = j + 1
	i = i - 1

#choosing the best values:
chooserV = [[0 for x in range(11)] for y in range(11)]
i = 10
j = 0
while j <= i:
    if cCallV[i][j] > cPutV[i][j]:
        chooserV[i][j] = cCallV[i][j]
    else:
        chooserV[i][j] = cPutV[i][j]
    j = j + 1

print chooserV
#finding the fair chooser value:
i = 9
while i >= 0:
	j = 0
	while j <= i:
		chooserV[i][j] = (q*chooserV[i+1][j] + (1-q)*chooserV[i+1][j+1])/R
		j = j + 1
	i = i - 1

print chooserV
"""

#printing the binomial trees to the user:
print 62*"-"
print "B I N O M I A L  O P T I O N   V A L U E  C A L C U L A T O R"
print 62*"-" + "\n"
print "current market data:\nasset value = $%.2f\nvolatility = %.2f\nrisk-free interest = %.2f\n" %(So,voli,r)
print "Projection of the asset value:"
print "\n"
for i in range(n+1):
	string = "%.2f" %S[i][0]
	j = 1
	while j <= i:
		string = string + "  " + "%.2f" %S[i][j] 
		j = j + 1
	print (40-3*i)*" " + "%s" %string
	print "\n"
 
print "Projection of the futures value on the asset S:"
print "\n"
for i in range(n+1):
	string = "%.2f" %F[i][0]
	j = 1
	while j <= i:
		string = string + "  " + "%.2f" %F[i][j] 
		j = j + 1
	print (40-3*i)*" " + "%s" %string
	print "\n"


print "The value of an american option:"
print "\n"
for i in range(n+1):
	string = "%.2f" %amV[i][0]
	j = 1
	while j <= i:
		string = string + "  " + "%.2f" %amV[i][j] 
		j = j + 1
	print (40-3*i)*" " + "%s" %string
	print "\n"


print "The value of a european option:"
print "\n"
for i in range(n+1):
	string = "%.2f" %euroV[i][0]
	j = 1
	while j <= i:
		string = string + "  " + "%.2f" %euroV[i][j] 
		j = j + 1
	print (40-3*i)*" " + "%s" %string
	print "\n"