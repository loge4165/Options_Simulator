import numpy as np
import pandas as pd

########## Notes on Numpy ############
    # Generates random seed
np.random.seed(39405)
    # normal distribution of mu = 0, sd = 1
np.random.normal(0,1)
    # generates array of 10 rows, 5 col of normal dist values
x = np.random.normal(0, 1, size=(10, 5))

#
class OptionSim():

    def __init__(self, SIMULATION, TYPE, OPTION, PRICE, STRIKE, RISKFREE, DAYS_EXPIRY, IMPLIED_VOL, DIVIDEND, PRICE_STEPS):
        self.S = [PRICE]
        self.K = STRIKE
        self.T = DAYS_EXPIRY                            # Time until option expiry (days)
        self.t = self.T/252                             # % of trading days each year
        self.r = RISKFREE
        self.v = IMPLIED_VOL
        self.d = DIVIDEND
        self.num_steps = PRICE_STEPS
        self.dt = (self.t/self.num_steps)               # the proportion of trading dats in the year, i.e. 21/252, then change being 

        if SIMULATION == 'MonteCarlo':
            self.montecarlo(TYPE, OPTION)
        elif SIMULATION == 'Bootstrap':
            pass
        elif SIMULATION == 'AltMC':
            pass


    # Monte Carlo Simulation
    def montecarlo(self, TYPE, OPTION):
        if TYPE == "European" and OPTION == 'Call':

            for i in range(0, self.num_steps - 1):
                self.S.append( self.S[i] * np.exp( (self.r - self.d - 0.5*(self.v**2)) * self.dt + (np.random.normal(0,1) * self.v * np.sqrt(self.dt)) ) )
            
            for i in range(0, self.num_steps):
                print(self.S[i])




        elif TYPE == "European" and OPTION == 'Put':
            pass
        elif TYPE == "American" and OPTION == 'Call':
            pass
        elif TYPE == "American" and OPTION == 'Put':
            pass






if __name__ == "__main__":
    # OPTIONS VARS
    # ________________________
    # Simulation Type       ~
    # Price                 S
    # Strike                K
    # risk free rate        r
    # dividend yield        q
    # random innovation     z
    # change in time        dt
    # days until exp        t
    # historical vol        v
    # ________________________

    SIMULATION = 'MonteCarlo'
    TYPE = 'European'
    OPTION = 'Call'
    PRICE_STEPS = 100

    PRICE = 100
    STRIKE  = 100
    RISKFREE = 0.025
    DAYS_EXPIRY = 21
    IMPLIED_VOL = 0.2
    DIVIDEND = 0
    

    Sim = OptionSim(SIMULATION, TYPE, OPTION, PRICE, STRIKE, RISKFREE, DAYS_EXPIRY, IMPLIED_VOL, DIVIDEND, PRICE_STEPS)