# Import the sha256 function
from hashlib import sha256

# Nonce value
MAX_NONCE = 10000


# Function for encoding text to a 64 bit hexadecimal value
def SHA256(text):
    """
    >>> SHA256('Hello')
    185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
    >>> SHA256('Text')
    71988c4d8e0803ba4519f0b2864c1331c14a1890bf8694e251379177bfedb5c3
    """
    return sha256(text.encode("ascii")).hexdigest()


# function for guessing nonce value
def mine(block_number, transactions, previous_hash, prefix_zeros, MAX_NONCE):
    """
    >>> mine(3,'Nap->here','71988c4d8e0803ba4519f0b2864c1331c14a1890bf8694e251379177bfedb5c3',2,100000)
    Successfully mined bitcoins with nonce value:56
    00d1789e063c9562e29f40918208ba908e98bfbbf4012a729b3b14ced5efc54b
    """

    # string with difficulty zeroes
    prefix_str = "0" * prefix_zeros

    # nonce is the value we want
    for nonce in range(MAX_NONCE):

        # concatinating the string and encoding it
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        # if matched the mined successfully
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    # might raise exception due to hardware issues etc
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


# Driver Code
if __name__ == "__main__":

    # Transactions string
    transactions = input("Enter Transactions : ")

    # Number of prefix zeroes
    difficulty = int(input("Enter Difficulty level : "))

    # For knowing time taken for mining
    import time

    start = time.time()
    print("start mining")

    previous_hash = input("Enter Previous has value : ")

    # Calling mine function with all required parameters
    new_hash = mine(5, transactions, previous_hash, difficulty, MAX_NONCE)

    # total time for refrence
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)

# INPUT : Transactions = '''Neeraj->Zara->50,Nandu->Allu->5''' , difficulty=2 ,
#         Previous_hash = a7sdxa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7
# OUTPUT : Successfully mined bitcoins with nonce value:336 end mining. Mining took: 12.207852363586426 seconds
# 006f74cef9d071afa15c58b38198be14f9b4aabb4cd6f7a44afffd9f6968efcd
