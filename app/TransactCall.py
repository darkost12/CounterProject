#!/usr/bin/env python
from web3 import Web3
import json
import sys
import os


class Counter:
    def __init__(self):
        self.getContract()

    # Using ganache-cli RPC-Provider
    def connect():
        web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
        web3.eth.defaultAccount = web3.eth.accounts[0]
        if web3.isConnected():
            print("Connected to the network!")
            Counter.web3 = web3
        else:
            sys.exit("Oops! Something went wrong. Check client's settings.")

    # Address in local blockchain of Ganache-cli
    def getContract(self):
        address = os.getenv("CONT_ADDR")
        if address == None:
            sys.exit("Address not found. Check env variable \'CONT_ADDR\'")
        with open("abi.json") as file:
            abi = json.load(file)
        self.contract = Counter.web3.eth.contract(
            address=Counter.web3.toChecksumAddress(address), abi=abi
        )

    def getCount(self):
        current = self.contract.functions.getCount().call()
        print("The current value of counter is ", current)
        return current

    def setCount(self, value):
        if int(value) < 0:
            print("Unable to set negative counter")
            return False
        tx_hash = self.contract.functions.setCount(int(value)).transact()
        tx_receipt = Counter.web3.eth.waitForTransactionReceipt(tx_hash)
        self.getCount()

    def increment(self):
        tx_hash = self.contract.functions.increment().transact()
        tx_receipt = Counter.web3.eth.waitForTransactionReceipt(tx_hash)
        self.getCount()

    def decrement(self):
        if int(self.contract.functions.getCount().call()) == 0:
            print("Unable to decrement a zero")
            return False
        tx_hash = self.contract.functions.decrement().transact()
        tx_receipt = Counter.web3.eth.waitForTransactionReceipt(tx_hash)
        self.getCount()


if __name__ == "__main__":
    Counter.connect()
    instance = Counter()

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
