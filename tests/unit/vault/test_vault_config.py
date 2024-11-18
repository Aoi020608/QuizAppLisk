from solders.pubkey import Pubkey

from restakingpy.accounts.vault.config import Config

def test_pubkey_vault_config():
    expected_pubkey = Pubkey.from_string("UwuSgAq4zByffCGCrWH87DsjfsewYjuqHfJEpzw1Jq3")

    program_id = Pubkey.from_string("Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8")

    pubkey, _, _ = Config.find_program_address(program_id)

    assert pubkey == expected_pubkey

def test_deserialize_vault_config():
    config_bytes = bytes( [1, 0, 0, 0, 0, 0, 0, 0, 96, 84, 246, 179, 232, 158, 88, 207, 173, 182, 195, 222, 227, 162, 211, 191, 89, 225, 141, 138, 7, 53, 82, 181, 198, 31, 36, 130, 214, 78, 95, 38, 6, 80, 196, 128, 197, 32, 56, 109, 46, 134, 174, 14, 207, 116, 137, 139, 142, 86, 234, 52, 231, 39, 253, 70, 176, 213, 22, 247, 84, 97, 202, 81, 128, 151, 6, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 208, 7, 196, 9, 10, 0, 10, 0, 128, 124, 215, 54, 120, 226, 92, 12, 200, 40, 242, 113, 118, 118, 100, 152, 169, 125, 113, 210, 157, 163, 151, 131, 46, 10, 225, 3, 74, 237, 146, 105, 96, 84, 246, 179, 232, 158, 88, 207, 173, 182, 195, 222, 227, 162, 211, 191, 89, 225, 141, 138, 7, 53, 82, 181, 198, 31, 36, 130, 214, 78, 95, 38, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    config = Config.deserialize(config_bytes)
    
    assert config.admin == Pubkey.from_string("7V3HKHNgxwxiMLjcgvwPCBey7yy4WJrHUH4JVFmewu1P")
    assert config.restaking_program == Pubkey.from_string("RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q")
    assert config.epoch_length == 432000
    assert config.num_vaults == 9
    assert config.deposit_withdrawal_fee_cap_bps == 2000
    assert config.fee_rate_of_change_bps == 2500
    assert config.fee_bump_bps == 10
    assert config.program_fee_bps == 10
    assert config.program_fee_wallet == Pubkey.from_string("9eZbWiHsPRsxLSiHxzg2pkXsAuQMwAjQrda7C7e21Fw6")
    assert config.fee_admin == Pubkey.from_string("7V3HKHNgxwxiMLjcgvwPCBey7yy4WJrHUH4JVFmewu1P")
    assert config.bump == 255

