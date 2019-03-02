def calculate_difficulty(block_chain):
    # @TODO: Redo this later!
    return (len(block_chain.block_chain) // 2000) + 1
