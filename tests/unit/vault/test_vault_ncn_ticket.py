from solders.pubkey import Pubkey

from restakingpy.accounts.vault.vault_ncn_ticket import VaultNcnTicket

def test_deserialize_vault_ncn_ticket():
    vault_ncn_ticket_bytes = bytes([3, 0, 0, 0, 0, 0, 0, 0, 227, 127, 125, 244, 135, 159, 207, 145, 143, 39, 163, 192, 165, 202, 47, 107, 191, 2, 189, 185, 94, 150, 204, 49, 255, 215, 224, 187, 96, 51, 16, 58, 39, 214, 168, 149, 199, 240, 9, 111, 210, 6, 111, 131, 207, 176, 242, 181, 115, 171, 29, 152, 114, 192, 171, 154, 47, 104, 26, 221, 190, 170, 137, 91, 0, 0, 0, 0, 0, 0, 0, 0, 113, 136, 42, 20, 0, 0, 0, 0, 113, 136, 42, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    assert vault_ncn_ticket_bytes[0] == VaultNcnTicket.discriminator

    vault_ncn_ticket = VaultNcnTicket.deserialize(vault_ncn_ticket_bytes)
    
    assert vault_ncn_ticket.vault == Pubkey.from_string("GK4JWqjwLY25pF2s2pgQG9kwnd486qRaEmZUz9ofqtuf")
    assert vault_ncn_ticket.ncn == Pubkey.from_string("3gWkEDrg3DP5pYGfB53ic5HWL8yMWpJJ5Y4WoLuTX4dx")

    assert vault_ncn_ticket.index == 0

    assert vault_ncn_ticket.state.slot_added == 338331761
    assert vault_ncn_ticket.state.slot_removed == 338331761

    assert vault_ncn_ticket.bump == 255

