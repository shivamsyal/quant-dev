import numpy as np
import matplotlib.pyplot as plt
import seaborn
import random

spot = float(input("Enter a spot price: "))
long_put = round(random.uniform(spot-10, spot), 2)
long_call = round(random.uniform(spot-10, spot), 2)
put_prem = round(random.uniform(0.0, 10.0), 2)
call_prem = round(random.uniform(0.0, 10.0), 2)
sRange = np.arange(0.7*spot, spot*1.3, 1)

def calls(sR, price, prem):
    return np.where(sR > price, sR - price, 0) - prem
def puts(sR, price, prem):
    return np.where(sR < price, price - sR, 0) - prem
payoff_call = calls(sRange, long_call, call_prem)
payoff_put = puts(sRange, long_put, put_prem)
payoff_strang = payoff_call + payoff_put
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible('zero')
ax.plot(sRange, payoff_call, '--', label='Long Call', color='r')
ax.plot(sRange, payoff_put, '--', label='Long Call', color='g')
ax.plot(sRange, payoff_strang, label='Strangle', color='b')
plt.xlabel('Price', ha = 'left')
plt.ylabel('Profit/Loss')
plt.legend()
plt.show()
