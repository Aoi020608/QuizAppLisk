from solders.pubkey import Pubkey

from restakingpy.accounts.vault.vault_staker_withdrawal_ticket import VaultStakerWithdrawalTicket

def test_pubkey_vault_staker_withdrawal_ticket():
    expected_pubkey = Pubkey.from_string("HMCARix5NHnWJpygRBx3azSgVbRsEn3CQgdpwejxtvFJ")

    program_id = Pubkey.from_string("Vau1t6sLNxnzB7ZDsef8TLbPLfyZMYXH8WTNqUdm9g8")
    vault = Pubkey.from_string("CSLdXAxizcHzEGDTfGWrfYoUQ8wpr4uN4nCLX1qjiNr5")
    base = Pubkey.from_string("H1UM7A52ymwraMmSdvMZtWnbEFsP3GWFsAWVuMRYhHRB")

    pubkey, _, _ = VaultStakerWithdrawalTicket.find_program_address(program_id, vault, base)

    assert pubkey == expected_pubkey

def test_deserialize_vault_staker_withdrawal_ticket():
    vault_staker_withdrawal_ticket_bytes = bytes( [7, 0, 0, 0, 0, 0, 0, 0, 169, 238, 69, 144, 235, 162, 130, 1, 47, 59, 64, 140, 200, 89, 148, 197, 111, 200, 27, 101, 27, 95, 2, 84, 26, 124, 239, 194, 4, 203, 42, 26, 123, 102, 10, 252, 117, 3, 156, 172, 207, 0, 128, 86, 108, 216, 143, 66, 211, 33, 58, 61, 247, 80, 200, 236, 37, 34, 138, 197, 74, 179, 108, 83, 237, 217, 233, 106, 207, 56, 130, 247, 6, 136, 93, 187, 255, 71, 166, 131, 136, 114, 115, 82, 218, 85, 62, 47, 254, 216, 208, 243, 158, 88, 74, 234, 128, 150, 152, 0, 0, 0, 0, 0, 100, 196, 11, 20, 0, 0, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    vault_staker_withdrawal_ticket = VaultStakerWithdrawalTicket.deserialize(vault_staker_withdrawal_ticket_bytes)
    
    assert vault_staker_withdrawal_ticket.vault == Pubkey.from_string("CSLdXAxizcHzEGDTfGWrfYoUQ8wpr4uN4nCLX1qjiNr5")
    assert vault_staker_withdrawal_ticket.staker == Pubkey.from_string("9JhPrjoBFuciG1AEG4kPAsLMntEtXKaqYwTZj29VQ3o8")
    assert vault_staker_withdrawal_ticket.base == Pubkey.from_string("H1UM7A52ymwraMmSdvMZtWnbEFsP3GWFsAWVuMRYhHRB")

    assert vault_staker_withdrawal_ticket.vrt_amount == 10000000
    assert vault_staker_withdrawal_ticket.slot_unstaked == 336315492
    assert vault_staker_withdrawal_ticket.bump == 254
