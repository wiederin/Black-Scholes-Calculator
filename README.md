# Black-Scholes Calculator

## Calculator




## Black-Scholes Model

The Black-Scholes Model is a mathematical equation that estimates the theoretical value of derivatives based on other
investment instruments, accounting for the impact of time and other risk factors. The model is usually accurate,
however, due to assumptions that are made in the model the predicted prices can deviate from the real-world. This model
is exclusively used to price European options, due to the fact that it does not account for the ability to exercise US
options before the expiration date.

## Model in Mathematical Notation

### Equation:

<img src="https://latex.codecogs.com/svg.image?\color{white}C&space;=&space;SN&space;(d_{1})&space;-&space;Ke^{-rt}N(d_{2})">

where:

<img src="https://latex.codecogs.com/svg.image?\bg{white}d_{1}&space;=&space;\frac{ln_{S}^{K}&space;&plus;&space;(r&space;&plus;&space;\frac{\sigma&space;^{2}}{2}t)}{\sigma&space;_{s}\sqrt{t}}&space;">

<img src="https://latex.codecogs.com/svg.image?\bg{white}d_{2}&space;=&space;d_{1}&space;-&space;\sigma&space;_{s}\sqrt{t}&space;&space;&space;">

C = call option price


S = current stock (or other underlying) price


K = strike price


r = risk-free interest rate


t = time to maturity


N = A normal distribution

sigma = volatility of asset


## How it works

### Assumptions

1. no dividends are paid out during the life of the option

2. markets are random (market movements cannot be predicted)

3. there are no transaction costs in buying the option

4. the risk-free rate and volatility of the underlying asset are known and constant

5. the returns on the underlying asset are log-normally distributed

6. the option is european and can only be exercised at expiration


The original Black-Scholes model does not consider the effects of dividends paid during the life of the option, the
model is often adapted to account for dividends by determining the ex-dividend date value of the underlying stock. The
model is also often adapted by option-selling market makers to account for the effect of options that can be exercised
before expiration. For US-style options binomial, trinomial, or the Bjerksund-Stensland models are used.

### Volatility Skew

The model makes assumption #5 because asset prices cannot be negative. Asset prices tend to have significant right
skewness and some degree of kurtosis (fat tails), meaning that high-risk downward moves happen more often in the market
than a normal distribution predicts. The assumption of lognormal underlying asset prices should show that implied
volatilities are similar for each strike price according to the B-S model. Since the market crash of 1987, implied
volatilities for at-the-money options have been lower than those further out of the money or far in the money. The
reason being that the market is pricing in a greate likelihood of a high volatility move to the downside. This has led
to the presence of the volatility skew. Mapping the implied volatilities for options with the same expiration date on a
graph, the skew shape can be seen. Therefore, the Black-Scholes model is not efficient for calculating implied
volatility.




### Drawbacks & Limitations

* only used for European options

* assumes dividends and risk-free rates are constant, although this may not be the case.

* assumption of constant volatility over the option's life, is not realistic because volatility fluctuates with the
level of supply and demand.

* assumption of no transaction costs or taxes is unrealistic

* assumption that risk-free interest rate is constant is unrealistic

* short selling of securities with use of proceeds is permitted

* there are no risk-less arbitrage opportunities can lead to real world deviations from the model

# Sources

* https://www.investopedia.com/terms/b/blackscholes.asp

