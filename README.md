# Black-Scholes Calculator

## Black-Scholes Model

The Black-Scholes Model is a mathematical equation that estimates the theoretical value of derivatives based on other
investment instruments, accounting for the impact of time and other risk factors. The model is usually accurate,
however, due to assumptions that are made in the model the predicted prices can deviate from the real-world. This model
is exclusively used to price European options, due to the fact that it does not account for the ability to exercise US
options before the expiration date.

## Model in Mathematical Notation

<img src="https://latex.codecogs.com/svg.image?\bg{black}C&space;=&space;SN&space;(d_{1})&space;-&space;Ke^{-rt}N(d_{2})>

```


C = call option price

S = current stock (or other underlying) price

K = strike price

r = risk-free interest rate

t = time to maturity

N = A normal distribution

```