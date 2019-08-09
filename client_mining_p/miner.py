import hashlib
import requests
import json
from blockchain import Blockchain

import sys


# TODO: Implement functionality to search for a proof


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # TODO: switch this for something better
    # TODO: look up multi threading
    # Run forever until interrupted

    while True:
        # TODO: Get the last proof from the server and look for a new one
        proof_req = requests.get(f'{node}/lastblock')
        req_data = proof_req.json()
        block = json.dumps(req_data['block'], sort_keys=True).encode()

        # TODO: When found, POST it to the server {"proof": new_proof}
        proof = 0
        while not Blockchain.valid_proof(block, proof):
            proof += 1

        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        mine_req = requests.get(f'{node}/mine?proof={proof}')

        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        req_data = mine_req.json()
        if req_data['message'][:3] == "New":
            coins_mined += 1

        print(f"total coins mined: {coins_mined}")
