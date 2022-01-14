from brownie import network, accounts,config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENV = ["ganache-local", "development"]
FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-dev"]
DECIMAL = 8
STARTING_PRICE = 200000000000
STARTING_PRICE_toWei = 2000
def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENV) or (network.show_active() in FORKED_LOCAL_ENV):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("Deploying Mocks....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMAL, STARTING_PRICE, {"from": accounts[0]})
    print("mock deployed")

