import numpy as np
import matplotlib.pyplot as plt
import seaborn
import random

spot = 255.60 #dummy price
long_put = 200 #dummy price
short_put = 230 #dummy price
long_call = 300 #dummy price
short_call = 270 #dummy price
long_put_prem = round(random.uniform(0.0, 5.0), 2)
short_put_prem = round(random.uniform(5.0, 10.0), 2)
long_call_prem = round(random.uniform(0.0, 5.0), 2)
short_call_prem = round(random.uniform(5.0, 10.0), 2)
sRange = np.arange(spot*0.5, spot*2, 1)

def calls(sR, price, prem):
    return np.where(sR > price, sR - price, 0) - prem
def puts(sR, price, prem):
    return np.where(sR < price, price - sR, 0) - prem
payoff_long_call = calls(sRange, long_call, long_call_prem)
payoff_short_call = calls(sRange, short_call, short_call_prem) * -1.0
payoff_long_put = puts(sRange, long_put, long_put_prem)
payoff_short_put = puts(sRange, short_put, short_put_prem) * -1.0
payoff_ic = payoff_long_call + payoff_short_call + payoff_long_put + payoff_short_put
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible('zero')
ax.plot(sRange, payoff_long_call, '--', label='Long Call', color='r')
ax.plot(sRange, payoff_short_call, '--', label='Short Call', color='y')
ax.plot(sRange, payoff_long_put, '--', label='Long Put', color='g')
ax.plot(sRange, payoff_short_put, '--', label='Short Put', color='m')
ax.plot(sRange, payoff_ic, label='Iron Condor', color='b')
plt.xlabel('Price', ha = 'left')
plt.ylabel('Profit/Loss')
plt.legend()
plt.show()
