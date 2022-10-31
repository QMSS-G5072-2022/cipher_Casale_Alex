from cipher_agc2162.cipher_agc2162 import cipher

import pytest

def test_single_word():
    assert cipher("apple",1) == "bqqmf"
