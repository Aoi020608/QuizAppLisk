from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.config import Config

def test_pubkey_restaking_config():
    expected_pubkey = Pubkey.from_string("4vvKh3Ws4vGzgXRVdo8SdL4jePXDvCqKVmi21BCBGwvn")

    program_id = Pubkey.from_string("RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q")

    pubkey, _, _ = Config.find_program_address(program_id)

    assert pubkey == expected_pubkey

def test_deserialize_restaking_config():
    config_bytes = bytes([1, 0, 0, 0, 0, 0, 0, 0, 96, 84, 246, 179, 232, 158, 88, 207, 173, 182, 195, 222, 227, 162, 211, 191, 89, 225, 141, 138, 7, 53, 82, 181, 198, 31, 36, 130, 214, 78, 95, 38, 7, 82, 151, 3, 233, 209, 72, 36, 13, 237, 19, 215, 83, 88, 206, 101, 40, 120, 109, 65, 221, 187, 195, 114, 118, 11, 178, 161, 116, 80, 255, 125, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 128, 151, 6, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    assert config_bytes[0] == Config.discriminator

    config = Config.deserialize(config_bytes)
    
    assert config.admin == Pubkey.from_string("7V3HKHNgxwxiMLjcgvwPCBey7yy4WJrHUH4JVFmewu1P")
    assert config.vault_program == Pubkey.from_string("Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8")
    assert config.ncn_count == 3
    assert config.operator_count == 1
    assert config.epoch_length == 432000
    assert config.bump == 255

