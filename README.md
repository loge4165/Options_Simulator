# Options_Simulator


Simulation techniques are a powerful and flexible way of pricing complex derivatives.
Under the risk neutral valuation method the option price is calculated in the following way:
  1) Simulate prices to the relevant horizon
  2) Calculate the payoff at maturity
  3) Repeat steps 1) and 2) many times
  4) Calculate the current value of the option by averaging the present value of the payoffs at maturity (discount rate is the risk free rate).
