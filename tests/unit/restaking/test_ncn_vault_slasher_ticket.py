from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.ncn_vault_slasher_ticket import NcnVaultSlasherTicket

def test_pubkey_ncn_vault_slasher_ticket():
    expected_pubkey = Pubkey.from_string("73e6g31sbGvJLKz9WAkBiM6yhCmKuuJYjMLV2Gk6GBUq")

    program_id = Pubkey.from_string("RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q")
    ncn = Pubkey.from_string("6D4e44djPyHih4ne361s91it6vWq5sxVyxURkzpB72c9")
    vault = Pubkey.from_string("7CrmCmuf2GQzkuhUvCAuAanJBaZ5HpVCw1VkqTCo4AG7")
    slasher = Pubkey.from_string("7CrmCmuf2GQzkuhUvCAuAanJBaZ5HpVCw1VkqTCo4AG7")

    pubkey, _, _ = NcnVaultSlasherTicket.find_program_address(program_id, ncn, vault, slasher)

    assert pubkey == expected_pubkey

def test_deserialize_ncn_vault_slasher_ticket():
    ncn_vault_slasher_ticket_bytes = bytes( [7, 0, 0, 0, 0, 0, 0, 0, 77, 97, 132, 207, 138, 59, 216, 13, 87, 217, 29, 47, 150, 163, 180, 158, 12, 152, 42, 3, 49, 2, 182, 103, 231, 60, 40, 112, 73, 203, 70, 202, 92, 47, 198, 211, 170, 161, 242, 117, 52, 212, 125, 135, 128, 255, 104, 183, 63, 78, 187, 183, 180, 56, 167, 36, 252, 229, 68, 37, 30, 53, 108, 104, 92, 47, 198, 211, 170, 161, 242, 117, 52, 212, 125, 135, 128, 255, 104, 183, 63, 78, 187, 183, 180, 56, 167, 36, 252, 229, 68, 37, 30, 53, 108, 104, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 116, 249, 79, 20, 0, 0, 0, 0, 116, 249, 79, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    assert ncn_vault_slasher_ticket_bytes[0] == NcnVaultSlasherTicket.discriminator

    ncn_vault_slasher_ticket = NcnVaultSlasherTicket.deserialize(ncn_vault_slasher_ticket_bytes)

    assert ncn_vault_slasher_ticket.ncn == Pubkey.from_string("6D4e44djPyHih4ne361s91it6vWq5sxVyxURkzpB72c9")
    assert ncn_vault_slasher_ticket.vault == Pubkey.from_string("7CrmCmuf2GQzkuhUvCAuAanJBaZ5HpVCw1VkqTCo4AG7")
    assert ncn_vault_slasher_ticket.slasher == Pubkey.from_string("7CrmCmuf2GQzkuhUvCAuAanJBaZ5HpVCw1VkqTCo4AG7")

    assert ncn_vault_slasher_ticket.max_slashable_per_epoch == 100
    assert ncn_vault_slasher_ticket.index == 0

    assert ncn_vault_slasher_ticket.state.slot_added == 340785524
    assert ncn_vault_slasher_ticket.state.slot_removed == 340785524

    assert ncn_vault_slasher_ticket.bump == 252

