from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.ncn_vault_ticket import NcnVaultTicket

def test_deserialize_ncn_vault_ticket():
    ncn_vault_ticket_bytes = bytes([6, 0, 0, 0, 0, 0, 0, 0, 189, 61, 129, 225, 194, 154, 170, 233, 182, 232, 146, 17, 216, 105, 66, 149, 165, 235, 154, 146, 138, 39, 192, 122, 29, 135, 249, 34, 48, 217, 156, 255, 234, 125, 22, 183, 244, 202, 151, 89, 0, 166, 125, 103, 91, 131, 149, 241, 31, 157, 148, 78, 134, 53, 159, 184, 134, 255, 60, 155, 42, 246, 139, 9, 0, 0, 0, 0, 0, 0, 0, 0, 24, 162, 102, 19, 0, 0, 0, 0, 24, 162, 102, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    ncn_vault_ticket = NcnVaultTicket.deserialize(ncn_vault_ticket_bytes)

    assert ncn_vault_ticket.ncn == Pubkey.from_string("DjiTEWCfVTtZuWvRcMtjBec9JFiSCUkNXAKrxzSn4CWz")
    assert ncn_vault_ticket.vault == Pubkey.from_string("GnM2mFbTjtWcCNk4GAggeVqTLD7V5WprnAdzjCxxuyx4")
    assert ncn_vault_ticket.index == 0

    assert ncn_vault_ticket.state.slot_added == 325493272
    assert ncn_vault_ticket.state.slot_removed == 325493272

    assert ncn_vault_ticket.bump == 254

