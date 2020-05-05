from pywallet import wallet

WALLET_PUBKEY = 'xpub6CEtEGBqtxmzhVcgWMcJVrjDkCMrw63CiKs11J6nWjLt9C8jhJuaQGuPSYtPZuModKF9WGEET8JLqvqScTERVzZTCWBHw3Goy2Zj9X8j4o6'

# generate address for specific user (id = 10)
user_addr = wallet.create_address(network="ETH", xpub=WALLET_PUBKEY, child=10)

# or generate a random address, based on timestamp
rand_addr = wallet.create_address(network="ETH", xpub=WALLET_PUBKEY)

print("User Address\n", user_addr)
print("Random Address\n", rand_addr)