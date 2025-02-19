import unittest.mock

import pytest
from vision.common.blockchains.enums import Blockchain

from vision.validatornode.blockchains.celo import CeloClient
from vision.validatornode.blockchains.celo import CeloClientError


@pytest.fixture(scope='module')
@unittest.mock.patch.object(CeloClient, '__init__', lambda self: None)
def celo_client():
    return CeloClient()


def test_get_blockchain_correct(celo_client):
    assert celo_client.get_blockchain() is Blockchain.CELO
    assert CeloClient.get_blockchain() is Blockchain.CELO


def test_get_error_class_correct(celo_client):
    assert celo_client.get_error_class() is CeloClientError
    assert CeloClient.get_error_class() is CeloClientError
