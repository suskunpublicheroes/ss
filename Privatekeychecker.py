from pycoin.key import Key

with open("private_keys.txt", "r") as file:
    private_keys = file.readlines()

for private_key in private_keys:
    try:
        key = Key.from_wif(private_key.strip())
        balance = key.balance()
        address = key.address()
        with open("successful.txt", "a") as success_file:
            success_file.write("Balance for address {} is {} Satoshi\n".format(address, balance))
    except Exception as e:
        pass
