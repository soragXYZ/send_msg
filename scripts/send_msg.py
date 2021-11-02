from brownie import config, accounts

def main():
    account_sender = accounts.add(config["wallets"]["from_key"]) # -> private key of sender to set in .env
    account_receiver = config["recipient"]["from_key"]  # -> public key of receiver to set in .env

    msg = "Well hello there".encode('utf-8')
    msg = msg.hex()

    tx = account_sender.transfer(account_receiver, data=msg)
    tx.wait(1)

    print("Message delivered")