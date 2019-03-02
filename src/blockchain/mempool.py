#T his file contains a class that simply holds an unordered set of uncommited transactions


class MemPool:
    def __init__(self):
        self.mempool = {}

    def add(self, transaction):
        if transaction.__hash__() in self.mempool:
            print("Make me an error later, but there was a hash collision in the mempool")
        else:
            self.mempool[transaction.__hash__()] = transaction

    def get_and_remove(self, transaction):
        ret = self.mempool[transaction.__hash__()]
        self.mempool.__delitem__(transaction.__hash__())
        return ret

    def get(self, transaction):
        return self.mempool[transaction.__hash__()]
