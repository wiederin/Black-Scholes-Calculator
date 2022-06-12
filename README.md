# Black-Scholes Calculator

## Black-Scholes Model

The Black-Scholes Model is a mathematical equation that estimates the theoretical value of derivatives based on other
investment instruments, accounting for the impact of time and other risk factors. The model is usually accurate,
however, due to assumptions that are made in the model the predicted prices can deviate from the real-world. This model
is exclusively used to price European options, due to the fact that it does not account for the ability to exercise US
options before the expiration date.

## Model in Mathematical Notation

### Equation:

<img src="https://latex.codecogs.com/svg.image?\bg{white}C&space;=&space;SN&space;(d_{1})&space;-&space;Ke^{-rt}N(d_{2})">

where:

<img src="https://latex.codecogs.com/svg.image?\bg{white}d_{1}&space;=&space;\frac{ln_{S}^{K}&space;&plus;&space;(r&space;&plus;&space;\frac{\sigma&space;^{2}}{2}t)}{\sigma&space;_{s}\sqrt{t}}&space;">

<img src="https://latex.codecogs.com/svg.image?\bg{white}d_{2}&space;=&space;d_{1}&space;-&space;\sigma&space;_{s}\sqrt{t}&space;&space;&space;">

C = call option price


S = current stock (or other underlying) price


K = strike price


r = risk-free interest rate


t = time to maturity


N = A normal distribution


## How it works

### Assumptions

* no dividends are paid out during the life of the option

* markets are random (market movements cannot be predicted)

* there are no transaction costs in buying the option

* the risk-free rate and volatility of the underlying asset are known and constant

* the returns on the underlying asset are log-normally distributed

* the option is european and can only be exercised at expiration


The original Black-Scholes model does not consider the effects of dividends paid during the life of the option, the
model is often adapted to account for dividends by determining the ex-dividend date value of the underlying stock. The
model is also often adapted by option-selling market makers to account for the effect of options that can be exercised
before expiration. For US-style options binomial, trinomial, or the Bjerksund-Stensland models are used.

### Volatility Skew

### Drawbacks & Limitations

# Sources

* https://www.investopedia.com/terms/b/blackscholes.asp

