import hashlib
import json 
from time import time

class Blockchain(object):
	def_init_(self):
		self.chain=[]
		self.current_transactions = []
		#create the initial block no prev or next- genesis block 
		self.new_block(previous_hash=1, proof=100)
	def new_block(self, proof, previous_hash=None):
		#create a new block to add ot the chain 
		block = {
			'index': len(self.chain)+1
			'timestamp': time()
			'transaction': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1])
		}
		pass
	def new_transaction(self, sender, recipent, amount):
		#adds new transaction to the list of transactions
		self.current_transactions.append({
			'sender': sender,
			'recipent': recipent,
			'amount': amount,
		})
		return self.last_block['index'] + 1
		pass
		
		#POW- proof of work
	def proof_of_work(self, last_proof):
		proof = 0 
		while self.valid_proof(last_proof, proof) is False:
			proof += 1
		return proof
		
	@staticmethod
	def valid_proof(last_proof, proof):
		#f' ' f-string f'{two} when two =2' which is 2 when two =2
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"
	@staticmethod
	def hash(block):
		#hashes a block
		#create a SHA-256 hash of a block
		
		#we must make sure that the Dictionary is Ordered, or there will be inconstitency
		block_string = json.dumps(block, sort_keys= True).encode()
		return hashlib.sha256(block_string).hexdigest()
		
		pass
		
	@property	
	def last_block(self):
		#Returns the last block in the chain
		return self.chain[-1]
		pass
		
		
	