from brownie import FundMe,network,config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks,LOCAL_BLOCKCHAIN_ENV



def deploy_FundMe():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()]["price_feed_address"]

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print('address:', price_feed_address)


    fundme = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"contract deployed to {fundme.address}")
    return fundme
def main():
    print ("deploy function")
    deploy_FundMe()
