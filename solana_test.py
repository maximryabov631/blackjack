from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

client = Client("https://api.mainnet-beta.solana.com")

sender = Keypair.from_private_key("4FRc9wBYz39NjQk9iJC4KuiGVXF298VL9yGCNndbKkKMYQiE9AkBf49aEkQnJtgegyjVVncVpeepfcmohZAG97Qg")
receiver = PublicKey("5QxoTWaHKqrh2bA3wKa9jM2HdFiQ3gVahzyW4kaLwCbR")

how_much_solana_to_transfer = float(input("enter amount to send: "))

amount = int(1000000000 * how_much_solana_to_transfer)

instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver, 
        lamports=amount
    )

transaction = Transaction(instructions=[instruction], signers=[sender])

result = client.send_transaction(transaction)
print("Transaction response: ", result)