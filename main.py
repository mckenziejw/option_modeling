####### Option strategy simulator #############
#
# This project aims to evaluate the 10-15 year viability of various options selling strategies by 
# Employing historical volatility and options pricing data with montecarlo simulations.
#
####### What we need ##################
# 1. A source of historic pricing data for the underlying equities
# 2. Historic IV data for the underlying equities
# 3. Use historic IV data to set the stochasticity parameters for MC simulation
# 4. An option pricing model:
#   a. Historic option pricing data (unlikely to find this)
#   b. Calculate option pricing using a formula
#       i. Estimate current IV given recent price trends within the modeled data
#       ii. Apply the Black-Scholes algorithm to estimate actual option premiums given calculated IV
###########################################

####### Implementation ################

# 1. Extract historic pricing data for the underlying equity
# TradingView API?
# Yahoo Finance API?
# Daily/Weekly/Monthly data?

# 2. Define options premium strategy
# Buy + Write covered calls
# Put ratio backspreads

# 3. Use historic IV data to set the stochasticity for MC simulation
# Simple Standard Deviation?
# Moving average for standard deviation? 

# 4. Apply the option pricing model to each price trend in the simulation
# Weekly/Monthly/60 day options
# Adjust for hold-to-expiry vs sell at threshold (50% profit for example)