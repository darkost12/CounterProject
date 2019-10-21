#!/usr/bin/env python
from web3 import Web3
import json
import sys
import os


# Class which provides Counter type object
class Counter:
    def __init__(self):
        self.getContract()

    # Function that connects to ganache client
    def connect():
        web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
        web3.eth.defaultAccount = web3.eth.accounts[0]
        if web3.isConnected():
            print("Connected to the network!")
            Counter.web3 = web3
        else:
            sys.exit("Error. Check ganache-cli settings.")

    # Function that links application with contract in the network
    def getContract(self):
        address = os.getenv("CONT_ADDR")
        if address == None:
            sys.exit("Set contract address in variable \'CONT_ADDR\' manually")
        with open("abi.json") as file:
            abi = json.load(file)
        self.contract = Counter.web3.eth.contract(
            address=Counter.web3.toChecksumAddress(address), abi=abi
        )

    # Function that gets the value of counter from the state variable
    # return value - the current state of variable in contract
    def getCount(self):
        value = self.contract.functions.getCount().call()
        print("The current value of counter is ", value)
        return value

    # Function that assigns new value to the state variable in contract
    def setCount(self, value):
        if int(value) < 0:
            print("Unable to set negative counter")
            return False
        tx_hash = self.contract.functions.setCount(int(value)).transact()
        tx_receipt = Counter.web3.eth.waitForTransactionReceipt(tx_hash)
        self.getCount()

    # Function that increases the state variable by 1
    def increment(self):
        tx_hash = self.contract.functions.increment().transact()
        tx_receipt = Counter.web3.eth.waitForTransactionReceipt(tx_hash)
        self.getCount()

    # Function that reduces the state variable by 1
    # return False - if 0 was met
    def decrement(self):
        if int(self.contract.functions.getCount().call()) == 0:
            print("Unable to decrement a zero")
            return False
        tx_hash = self.contract.functions.decrement().transact()
        tx_receipt = Counter.web3.eth.waitForTransactionReceipt(tx_hash)
        self.getCount()


if __name__ == "__main__":
    # Initialization of object
    Counter.connect()
    instance = Counter()

    # Console user interface logic
    options = {
        "1": Counter.getCount,
        "3": Counter.increment,
        "4": Counter.decrement,
    }

    while True:
        operation = input(
            "\nChoose the number of operation:\n1 - GetCount\
            \n2 - SetCount\n3 - Increment\n4 - Decrement\n5 - Exit\n"
        )
        if int(operation) == 2:
            while True:
                # Assuming that the counter works with uints
                value = input("Choose non-negative integer value to assign\n")
                if value.isdigit():
                    break
            Counter.setCount(instance, value)
        elif operation in options:
            options[operation](instance)
        elif int(operation) == 5:
            sys.exit()
