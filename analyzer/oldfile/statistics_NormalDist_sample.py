from statistics import NormalDist

sum_val = 14
real_data = 9

data_calculation = float(real_data/sum_val)

print(data_calculation)

#NormalDist(mu=10, sigma=2).inv_cdf(0.95)
# パラメータ指定がないと、標準正規分布(mu = 0およびsigma = 1)に自動補完される。
print(NormalDist().cdf(0.655))


