# Options_Simulator

A Monte Carlo simulation is a model used to predict the probability of different outcomes when the intervention of random variables is present. This is particularly using when determining 'accurate' option prices, as the assumption that underlying asset price follows a geometric brownian motion allows us to repetitvely simulate price innovations across a given interval (i.e. a month). These simulations, when repeated, can then be used to calculate option maturity prices, and with enough trials, these average payoffs give confidence in the determined option's 'natural' value.


Simulation techniques are a powerful and flexible way of pricing complex derivatives. Under the risk neutral valuation method the option price is calculated in the following way:
  1) Simulate prices to the relevant horizon
  2) Calculate the option payoff at maturity
  3) Repeat steps 1) and 2) many times
  4) Calculate the current value of the option by averaging the present value of the payoffs at maturity (discount rate is the risk free rate).
