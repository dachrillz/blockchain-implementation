import os
import sqlite3

from src.blockchain.block import Block
from src.blockchain.transaction import Transaction
from src.interface.json_wrapper import serialize_block_to_json, convert_json_to_python

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path = dir_path + '/testdatabase/blocks.db'


class TestDataBase:
    def __init__(self, block_chain):
        self.open_connection()
        self.wipe_data()
        k = 0
        for block in block_chain.block_chain:
                v = serialize_block_to_json(block)
                self.commit_query("INSERT INTO blocks(k, v) VALUES(:k, :v)", (k,v))
                k += 1

        self.close_connection()

    def wipe_data(self):
                self.commit_query("DROP TABLE IF EXISTS blocks")
                self.commit_query("CREATE TABLE blocks(k INTEGER PRIMARY KEY, v BLOB)")

    def open_connection(self):
        self.connection = sqlite3.connect(dir_path)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def commit_query(self, query_string, args=None):
        if args is not None:
            self.cursor.execute(query_string, args)
        else:
            self.cursor.execute(query_string)
        self.connection.commit()


    def get_block(self, index):
        #ser = test_db.get(b'index')

        _dict = convert_json_to_python(ser)

        block = Block(
            _dict['block_header']['version'],
            _dict['block_header']['prev_hash'],
            _dict['block_header']['merkle_root'],
            _dict['block_header']['timestamp'],
            _dict['block_header']['difficulty_target'],
            _dict['block_header']['nonce'])

        for _trans in _dict['transactions']:
            print("")
            raise NotImplementedError()
