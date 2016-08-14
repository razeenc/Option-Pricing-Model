# binomial-option-pricing-model

Binomial option pricing model written as part of the Coursera FE & RM course offered by Columbia University.

I wrote the code to use myself for an assignment, hence it is not very user friendly.
Therefore, do the following to manipulate the output:
To change the options from put to call or vice versa look for the part in the code that populates euroV[][] and amV[][]. Change the code such that either the function putPayoff() or callPayoff() is used, as desired. There's one instance in the euroV code (line 68) and two instances in the amV code (lines 83 & 91).
To choose if the option should be calculated on the asset or on the futures contract, again look at the code populating euroV[][] and amV[][] and change the parts mentioning "S", the stock price, to "F", the futures price. There's one instance in the euroV code (line 68) and two instances in the amV code (lines 83 & 91).
Change the parameters like strike, expiry, period at will.
