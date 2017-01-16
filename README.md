# binomial-option-pricing-model

I wrote the code for personal use on an assignment, hence it is not really user friendly.
If anyone would still like to use it, do the following to manipulate the output:
To change the options from put to call or vice versa look for the part in the code that populates euroV[][] and amV[][]. Change the code such that either the function putPayoff() or callPayoff() is used, as desired. There's one instance in the euroV code (line 68) and two instances in the amV code (lines 83 & 91).
To choose if the option should be calculated on the asset or on the futures contract, again look at the code populating euroV[][] and amV[][] and change the parts mentioning "S", the stock price, to "F", the futures price. There's one instance in the euroV code (line 68) and two instances in the amV code (lines 83 & 91).
Change the parameters like strike, expiry, period at will.
