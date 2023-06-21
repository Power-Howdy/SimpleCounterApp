from brownie import SimpleCounter, accounts
from brownie.network import priority_fee

def main():
    priority_fee('0.1 gwei')
    SimpleCounter.deploy( {"from": accounts[0]})
    print("deployed")