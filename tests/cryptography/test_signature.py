from unittest import TestCase

from src.cryptography.signature import verify_signature_from_public_key, create_signature


class TestSignature(TestCase):

    def test_signature_valid(self):
        mes = b'hej'
        key = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
        public = '04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'
        signature = create_signature(key, mes)

        a = verify_signature_from_public_key(signature, public, mes)

        self.assertTrue(a)

    def test_signature_invalid_public_key(self):
        mes = 'hej'
        key = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
        public = '04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'
        signature = create_signature(key, mes)

        public = '04c7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'
        a = verify_signature_from_public_key(signature, public, mes)

        self.assertFalse(a)

    def test_signature_invalid_message(self):
        mes = 'hej'
        key = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
        public = '04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'

        signature = create_signature(key, mes)

        mes = 'hejsansvejsan'

        a = verify_signature_from_public_key(signature, public, mes)

        self.assertFalse(a)
