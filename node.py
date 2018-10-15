from uuid import uuid4

from blockchain import Blockchain
from verification import Verification

class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'JET'
        self.blockchain = Blockchain(self.id)


    def get_transaction_value(self):
        """ Returns the user input (a new transaction amount) as a float. """
        # Get the user input, transform it from a string to a float and store it in user_input
        tx_recipient = input('Enter the recipient for the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        """Prompts the user for its choice and return it."""
        user_input = input('Your choice: ')
        return user_input


    def print_blockchain_elements(self):
        """ Output all blocks of the blockchain. """
        # Output the blockchain list to the console
        for block in self.blockchain.chain:
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)


    def listen_for_input(self):
        waiting_for_input = True
        # A while loop for the user input interface
        # It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                # unpack the tuple
                recipient, amount = tx_data
                # add the transaction to the blockchain
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.open_transactions)
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                # q is "quit," which will exit the loop
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            verifier = Verification()
            if not verifier.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                # Break out of the loop
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
        else:
            print('User left!')


        print('Done!')


node = Node()
node.listen_for_input()
