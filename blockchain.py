from functools import reduce
import json
import pickle

from hash_util import hash_block
from block import Block
from transaction import Transaction
from verification import Verification

# The reward given to miners for creating a new block
MINING_REWARD = 10

# Initializing our (empty) blockchain list
blockchain = []
# Unhandled transactions
open_transactions = []
# We are the owner of this blockchain node, hence this is our identifier (e.g. for sending coins)
owner = 'Jet'


def load_data():
    """Initialize blockchain + open transactions data from a file."""
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            # We need to convert  the loaded data because Transactions should use OrderedDict
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [Transaction(tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                updated_block = Block(block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1])
            # We need to convert  the loaded data because Transactions should use OrderedDict
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = Transaction(tx['sender'], tx['recipient'], tx['amount'])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
        # USING PICKLE:
        # with open('blockchain.p', mode='rb') as f:
        #     file_content = pickle.loads(f.read())
        #     global blockchain
        #     global open_transactions
        #     blockchain = file_content['chain']
        #     open_transactions = file_content['ot']
    except (IOError, IndexError):
        # Our starting block for the blockchain
        genesis_block = Block('', 0, [], 100, 0)
        # Initializing our (empty) blockchain list
        blockchain = [genesis_block]
        # Unhandled transactions
        open_transactions = []
    finally:
        print('Cleanup!')


load_data()


def save_data():
    """Save blockchain + open transactions snapshot to a file."""
    try:
        with open('blockchain.txt', mode='w') as f:
            saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in blockchain]]
            f.write(json.dumps(saveable_chain))
            f.write('\n')
            saveable_tx = [tx.__dict__ for tx in open_transactions]
            f.write(json.dumps(saveable_tx))
        # USING PICKLE:
        # with open('blockchain.p', mode='wb') as f:
        #     save_data = {
        #         'chain': blockchain,
        #         'ot': open_transactions
        #     }
        #     f.write(pickle.dumps(save_data))
    except IOError:
        print('Saving failed!')


def proof_of_work():
    """Generate a proof of work for the open transactions, the hash of the previous block and a random number (which is guessed until it fits)."""
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    # Try different PoW numbers and return the first valid one
    verifier = Verification()
    while not verifier.valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    """Calculate and return the balance for a participant.

    Arguments:
        :participant: The person for whom to calculate the balance.
    """
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of transactions that were already included in blocks of the blockchain
    tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in blockchain]
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of open transactions (to avoid double spending)
    open_tx_sender = [tx.amount for tx in open_transactions if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    print('tx_sender === ', tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # This fetches received coin amounts of transactions that were already included in blocks of the blockchain
    # We ignore open transactions here because you shouldn't be able to spend coins before the transaction was confirmed + included in a block
    tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    # Return the total balance
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value, to the blockchain.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins with the transaction (default = 1.0)
    """
    transaction = Transaction(sender, recipient, amount)
    verifier = Verification()
    if verifier.verify_transaction(transaction, get_balance):
        open_transactions.append(transaction)
        save_data()
        return True
    return False


def mine_block():
    """Create a new block and add open transactions to it."""
    # Fetch the current last block of the blockchain
    last_block = blockchain[-1]
    # Hash the last block (=> to be able to compare it to the stored hash value)
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # Miners should be rewarded, so create a reward transaction
    reward_transaction = Transaction('MINING', owner, MINING_REWARD)
    # Copy transaction instead of manipulating the original open_transactions list
    # This ensures that if for some reason the mining should fail, we don't have the reward transaction stored in the open transactions
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transactions, proof)
    blockchain.append(block)
    return True
