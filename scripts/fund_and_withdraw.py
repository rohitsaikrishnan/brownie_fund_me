from brownie import FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account
def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"the current entrance fee is {entrance_fee}")
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    print(fund_me.addressToAmountFunded(account.address))

def withdraw():
    fund_me = FundMe[-1]
    account  = get_account()
    fund_me.withdraw({"from":account})


def main():
    fund()
    withdraw()