# blockchain-implementation
[![Build Status](https://travis-ci.org/dachrillz/blockchain-implementation.svg?branch=master)](https://travis-ci.org/dachrillz/blockchain-implementation)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/245ba1f76ec7485f98365cfeb79cd25b)](https://www.codacy.com/app/dachrillz/blockchain-implementation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dachrillz/blockchain-implementation&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/dachrillz/blockchain-implementation/branch/master/graph/badge.svg)](https://codecov.io/gh/dachrillz/blockchain-implementation)

# Current goals

I stopped at writing the json interface. Nonces need to be converted
to ints in order to be serializable!
Write tests for the serializer!

1. Write an interface for the block explorer
2. Write a simple wallet
3. Verify that an incoming transaction is correct


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
12. Block explorer functions do a lot of redundant calculations, they need to be optimized later.
