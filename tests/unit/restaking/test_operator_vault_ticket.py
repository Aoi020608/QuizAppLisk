from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.operator_vault_ticket import OperatorVaultTicket

def test_pubkey_operator_vault_ticket():
    expected_pubkey = Pubkey.from_string("GSbTaLjof8cw7XLKBXxz2CkamMrZx1j89yL1hkeL8gCu")

    program_id = Pubkey.from_string("RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q")
    operator = Pubkey.from_string("2Uit7hCcTnMFFDYszysxMMWYuh2s2r6UfQAw8D1T5PNW")
    vault = Pubkey.from_string("GK4JWqjwLY25pF2s2pgQG9kwnd486qRaEmZUz9ofqtuf")

    pubkey, _, _ = OperatorVaultTicket.find_program_address(program_id, operator, vault)

    assert pubkey == expected_pubkey

def test_deserialize_operator_vault_ticket():
    operator_vault_ticket_bytes = bytes([5, 0, 0, 0, 0, 0, 0, 0, 21, 245, 185, 95, 40, 39, 249, 71, 159, 27, 46, 62, 14, 243, 25, 154, 165, 199, 239, 161, 162, 237, 58, 76, 58, 22, 8, 112, 246, 150, 146, 183, 227, 127, 125, 244, 135, 159, 207, 145, 143, 39, 163, 192, 165, 202, 47, 107, 191, 2, 189, 185, 94, 150, 204, 49, 255, 215, 224, 187, 96, 51, 16, 58, 0, 0, 0, 0, 0, 0, 0, 0, 236, 181, 15, 20, 0, 0, 0, 0, 236, 181, 15, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    operator_vault_ticket = OperatorVaultTicket.deserialize(operator_vault_ticket_bytes)

    assert operator_vault_ticket.operator == Pubkey.from_string("2Uit7hCcTnMFFDYszysxMMWYuh2s2r6UfQAw8D1T5PNW")
    assert operator_vault_ticket.vault == Pubkey.from_string("GK4JWqjwLY25pF2s2pgQG9kwnd486qRaEmZUz9ofqtuf")
    assert operator_vault_ticket.index == 0

    assert operator_vault_ticket.state.slot_added == 336573932
    assert operator_vault_ticket.state.slot_removed == 336573932

    assert operator_vault_ticket.bump == 255

