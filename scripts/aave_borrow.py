from brownie import config, network
from web3 import Web3

from scripts.helper_scripts import (
    get_account,
    get_lending_pool,
    approve_erc20,
    get_borrowable_data,
    LOCAL_BLOCKCHAIN_FORKS,
)
from scripts.get_weth import get_weth

APPROVE_AMOUNT = Web3.toWei(0.1, "ether")


def main() -> None:
    account = get_account()
    # Get WETH
    weth_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in LOCAL_BLOCKCHAIN_FORKS:
        get_weth()
    # Deposit WETH into lending pool
    lending_pool = get_lending_pool()
    approve_erc20(lending_pool.address, APPROVE_AMOUNT, weth_address, account)
    print(f"Depositing {APPROVE_AMOUNT} WETH.")
    tx = lending_pool.deposit(
        weth_address, APPROVE_AMOUNT, account.address, 0, {"from": account}
    )
    tx.wait(1)
    print("Deposited.")


# if __name__ == "__main__":
#     main()
