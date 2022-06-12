from math import log, sqrt, pi, exp
from scipy.stats import norm

"""
        Price an option using the Black-Scholes model

        C = call option price

        S = current stock price

        K = strike price

        r = risk-free interest rate

        t = time to maturity

        N = a normal distribution
"""

def d1(s, k, t, r, sigma):
    return(log(s/k) + (r + sigma**2/2.) * t) / (sigma * sqrt(t))


def d2(s, k, t, r, sigma):
    return d1(s, k, t, r, sigma) - sigma * sqrt(t)


def black_scholes_call(s, k, t, r, sigma):
    return s * norm.cdf(d1(s, k, t, r, sigma)) - k * exp(-r * t) * norm.cdf(d2(s, k, t, r, sigma))

def black_scholes_put(s, k, t, r, sigma):
    return k * exp(-r * t) - s * black_scholes_call(s, k, t, r, sigma)