from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.operator_vault_ticket import OperatorVaultTicket

def test_deserialize_operator_vault_ticket():
    operator_vault_ticket_bytes = bytes([5, 0, 0, 0, 0, 0, 0, 0, 191, 148, 154, 6, 161, 122, 188, 244, 50, 106, 52, 223, 23, 56, 170, 217, 204, 12, 71, 226, 144, 229, 29, 161, 104, 120, 136, 104, 201, 171, 36, 124, 153, 220, 50, 191, 209, 117, 83, 207, 175, 107, 214, 213, 106, 228, 90, 210, 176, 106, 28, 117, 117, 84, 45, 1, 225, 34, 138, 21, 17, 219, 40, 30, 0, 0, 0, 0, 0, 0, 0, 0, 244, 9, 104, 19, 0, 0, 0, 0, 244, 9, 104, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    operator_vault_ticket = OperatorVaultTicket.deserialize(operator_vault_ticket_bytes)

    assert operator_vault_ticket.operator == Pubkey.from_string("DtrJ59hK5dogf4aPsPGAH8wzBc2tQiEHCViU9rVNqVm5")
    assert operator_vault_ticket.vault == Pubkey.from_string("BMc8653Cnht8juzcdr9rEhskFe9ZBw6yihsaLbkQhMHX")
    assert operator_vault_ticket.index == 0

    assert operator_vault_ticket.state.slot_added == 325585396
    assert operator_vault_ticket.state.slot_removed == 325585396

    assert operator_vault_ticket.bump == 255

