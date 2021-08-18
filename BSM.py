import numpy as np
import pandas as pd

class BSM():
    def __init__(self, TYPE, OPTION, PRICE, STRIKE, RISKFREE, DAYS_EXPIRY, HISTORICAL_VOL):
        self.S = PRICE
        self.K = STRIKE
        self.T = DAYS_EXPIRY                            # Time until option expiry (days)
        self.t = self.T/252                             # % of trading days each year
        self.r = RISKFREE
        self.v = HISTORICAL_VOL
        
        self.type = TYPE
        self.option = OPTION

    # CALL
    def call(self):
        pass

    def put(self):
        pass



if __name__ == "__main__":
    TYPE = 0
    OPTION = 0
    PRICE = 0
    STRIKE = 0 
    RISKFREE = 0
    DAYS_EXPIRY = 0 
    HISTORICAL_VOL = 0

    Bsm = BSM(TYPE, OPTION, PRICE, STRIKE, RISKFREE, DAYS_EXPIRY, HISTORICAL_VOL)