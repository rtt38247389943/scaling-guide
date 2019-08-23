import itertools
import string
import hashlib
import string
import random

dict = {}

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

for ii in xrange(500000):
	dict[ii] = randomString(1000)

hashes = ['9d52e5647865b61ccee618e1375b3a54']
hashesToDo = len(hashes)
hashesDone = []

def doHash( password):
	m = hashlib.md5()
	m.update(password)
	
	return m.digest().encode('hex')

# https://stackoverflow.com/questions/40269605/how-to-create-a-bruteforce-password-cracker-for-alphabetical-and-alphanumerical
def guess_password():
	hashesToDo = len(hashes)
	#chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	print len(chars)
	#chars = string.ascii_lowercase
	attempts = 0
	for password_length in range(1, 9):
		print password_length
		for guess in itertools.product(chars, repeat=password_length):
			guess = ''.join(guess)
			if hashesToDo == 0:
				return
			for hash in hashes:
				calcHash = doHash( guess)
				if calcHash == hash:
					hashesToDo -= 1
					hashesDone.append( hash[0])
					print "%s %s" % (hash[0], guess)

guess_password()