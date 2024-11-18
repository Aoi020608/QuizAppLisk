from solders.pubkey import Pubkey

from restakingpy.accounts.vault.vault import Vault

def test_pubkey_vault():
    expected_pubkey = Pubkey.from_string("CinzjQ2V8VPKd48f32AeYV9KepFJ4bUxkdv3ErByAaX6")

    program_id = Pubkey.from_string("Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8")
    base = Pubkey.from_string("x5iHY3cEs5U9NUojWiqCJguwTvFV1rMZyRiqHx5pcVN")

    pubkey, _, _ = Vault.find_program_address(program_id, base)

    assert pubkey == expected_pubkey

def test_deserialize_vault():
    vault_bytes = bytes([2, 0, 0, 0, 0, 0, 0, 0, 14, 28, 69, 172, 101, 234, 20, 159, 246, 181, 159, 230, 140, 125, 31, 158, 154, 93, 100, 115, 99, 98, 63, 205, 247, 137, 131, 152, 167, 62, 78, 81, 123, 26, 12, 228, 85, 114, 48, 12, 194, 217, 121, 183, 62, 199, 58, 68, 91, 8, 169, 79, 254, 124, 20, 233, 227, 253, 5, 213, 147, 176, 101, 199, 6, 155, 136, 87, 254, 171, 129, 132, 251, 104, 127, 99, 70, 24, 192, 53, 218, 196, 57, 220, 26, 235, 59, 85, 152, 160, 240, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 202, 154, 59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 155, 12, 45, 170, 52, 62, 182, 1, 156, 174, 157, 178, 79, 135, 163, 157, 2, 137, 78, 179, 137, 20, 97, 38, 217, 64, 243, 54, 41, 111, 231, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 100, 170, 41, 125, 22, 116, 75, 233, 109, 110, 72, 25, 194, 168, 154, 6, 231, 84, 16, 12, 39, 206, 173, 229, 242, 0, 148, 144, 6, 19, 52, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 193, 117, 9, 20, 0, 0, 0, 0, 56, 156, 21, 20, 0, 0, 0, 0, 0, 0, 10, 0, 10, 0, 244, 1, 10, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    assert vault_bytes[0] == Vault.discriminator

    vault = Vault.deserialize(vault_bytes)

    assert vault.base == Pubkey.from_string("x5iHY3cEs5U9NUojWiqCJguwTvFV1rMZyRiqHx5pcVN")
    assert vault.vrt_mint == Pubkey.from_string("9HYBnMCrVLwtTfPi7EFn6F6HwzhV7YEhwn4P4RXSELri")
    assert vault.supported_mint == Pubkey.from_string("So11111111111111111111111111111111111111112")
    assert vault.vrt_supply == 0
    assert vault.tokens_deposited == 0
    assert vault.deposit_capacity == 1000000000

    assert vault.delegation_state.staked_amount == 0
    assert vault.delegation_state.enqueued_for_cooldown_amount == 0
    assert vault.delegation_state.cooling_down_amount == 0

    assert vault.additional_assets_need_unstaking == 0
    assert vault.vrt_enqueued_for_cooldown_amount == 0
    assert vault.vrt_cooling_down_amount == 0
    assert vault.vrt_ready_to_claim_amount == 0

    assert vault.admin == Pubkey.from_string("NtAUW1z9C9D3AedNgyMLhSo5djkq4HVUv6jDWDhRYsx")
    assert vault.delegation_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.operator_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.ncn_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.slasher_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.capacity_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.fee_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.delegate_asset_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.fee_wallet == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.mint_burn_admin == Pubkey.from_string("11111111111111111111111111111111")
    assert vault.metadata_admin == Pubkey.from_string("VrtAtqPCyXGucAbk6oTfmegwEp4z2wbYmnLeuZtpWK5")
    assert vault.vault_index == 2
    assert vault.ncn_count == 0
    assert vault.operator_count == 0
    assert vault.slasher_count == 0
    assert vault.last_fee_change_slot == 336164289
    assert vault.last_full_state_update_slot == 336960568
    assert vault.deposit_fee_bps == 0
    assert vault.withdrawal_fee_bps == 10
    assert vault.next_withdrawal_fee_bps == 10
    assert vault.reward_fee_bps == 500
    assert vault.program_fee_bps == 10
    assert vault.bump == 255

