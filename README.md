# blockchain-implementation
[![Build Status](https://travis-ci.org/dachrillz/blockchain-implementation.svg?branch=master)](https://travis-ci.org/dachrillz/blockchain-implementation)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/245ba1f76ec7485f98365cfeb79cd25b)](https://www.codacy.com/app/dachrillz/blockchain-implementation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dachrillz/blockchain-implementation&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/dachrillz/blockchain-implementation/branch/master/graph/badge.svg)](https://codecov.io/gh/dachrillz/blockchain-implementation)

# Current goals
1. Verify unspent outputs!!!!!!!
2. Next up should be ability to make request transactions to the blockchain. Thas is:
1. write the I/O for the terminal in order to make transactions
2. might require the coinbase to be implemented in the transactions
3. add ability to add transactions to the blocks.
4. don't forget to write tests!


# Later goals
3. Add ability for the client to check integrity of the blockchain
4. Mining! That is make sure that blocks get written at a certain pace.
5. Write tests for the miner
6. Write test to verify PoW
7. What to do with all time stamps?
8. Make sure that transactions are removed from mem pool after they are used!
9. handle when there is transation id collisions.
10. Handle when the script machine crashes
11. Difficulty is spread all over and needs to be figured out
