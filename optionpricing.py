import numpy as np
from numpy.lib.function_base import average
import pandas as pd

########## Notes on Numpy ############
    # Generates random seed, insert a seed num for testing
np.random.seed()
    # normal distribution of mu = 0, sd = 1
np.random.normal(0,1)
    # generates array of 10 rows, 5 col of normal dist values
x = np.random.normal(0, 1, size=(10, 5))

#
class OptionSim():

    def __init__(self, SIMULATION, TYPE, OPTION, PRICE, STRIKE, RISKFREE, DAYS_EXPIRY, HISTORICAL_VOL, DIVIDEND, PRICE_STEPS, NUM_SIMS):
        self.S = [PRICE]
        self.K = STRIKE
        self.t = DAYS_EXPIRY                            # Time until option expiry (days)
        self.T = self.t/252                             # % of trading days each year
        self.r = RISKFREE
        self.v = HISTORICAL_VOL
        self.d = DIVIDEND
        self.num_steps = PRICE_STEPS
        self.dt = (self.T/self.num_steps)               # the proportion of trading dats in the year, i.e. 21/252, then change being 

        # FORMULATED DATA
        self.price_array = []                           # contains underlying 'final price' array
        self.payoff_array = []

        if SIMULATION == 'MonteCarlo':
            self.montecarlo()
            self.payoff()
            self.calculate_statistics()

        elif SIMULATION == 'Bootstrap':
            pass
        elif SIMULATION == 'AltMC':
            pass


    # Monte Carlo Simulation
    def montecarlo(self):
        # for i in range(0, self.num_steps - 1):
        #     self.S.append( self.S[i] * np.exp( (self.r - self.d - 0.5*(self.v**2)) * self.dt + (np.random.normal(0,1) * self.v * np.sqrt(self.dt)) ) )

        for i in range(0, NUM_SIMS):
            for i in range(0, self.num_steps):
                self.S.append( self.S[i] * np.exp( (self.r - self.d - 0.5*(self.v**2)) * self.dt + (np.random.normal(0,1) * self.v * np.sqrt(self.dt)) ) )
            self.price_array.append(self.S[self.num_steps - 1])
            self.S.clear()
            self.S.append(PRICE)
        
        # PRINTING
        # for i in range(0, self.num_steps):
        #     print(self.S[i])

        # for i in range(0, NUM_SIMS):
        #      print(self.price_array[i])

    def payoff(self):
        if TYPE == "European" and OPTION == 'Call':
            for i in range(0, len(self.price_array)):
                self.payoff_array.append(max(0, self.price_array[i] - self.K))
                # print(self.payoff_array[i])

        elif TYPE == "European" and OPTION == 'Put':
            for i in range(0, len(self.price_array)):
                self.payoff_array.append(max(0, self.K - self.price_array[i]))
            
                # print(self.payoff_array[i])
    
    def calculate_statistics(self):
        # CALCULATES SUMMARY STATISTICS OF THE OPTION,
        # e.i; average payoff/price, sample variance, sd, CI.
        print()
        print('_____________________________________________')
        print('               SUMMARY STATSTICS             ')
        print('_____________________________________________')
        print('OPTION:    ',OPTION)
        print('TYPE:      ',TYPE)
        print('PRICE:     ',average(self.payoff_array))
        print('_____________________________________________')
        print()
       





if __name__ == "__main__":
    # OPTIONS VARS
    # ________________________
    # Simulation Type       ~
    # Option Type           ~
    # Option Side           ~
    # Number of Trials      ~

    # Price                 S
    # Strike                K
    # risk free rate        r
    # dividend yield        q
    # days until exp        t
    # historical vol        v

    # change in time        dt
    # random innovation     z
    # ________________________

    SIMULATION = 'MonteCarlo'
    TYPE = 'European'
    OPTION = 'Put'
    PRICE_STEPS = 100
    NUM_SIMS = 1000

    PRICE = 84.620
    STRIKE  = 84
    RISKFREE = 0.00879
    DIVIDEND = 0
    DAYS_EXPIRY = 7
    HISTORICAL_VOL = 0.19      
    
    

    Sim = OptionSim(SIMULATION, TYPE, OPTION, PRICE, STRIKE, RISKFREE, DAYS_EXPIRY, HISTORICAL_VOL, DIVIDEND, PRICE_STEPS, NUM_SIMS)