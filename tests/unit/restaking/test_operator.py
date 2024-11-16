from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.operator import Operator

def test_deserialize_operator():
    operator_bytes = bytes([3, 0, 0, 0, 0, 0, 0, 0, 54, 253, 44, 101, 48, 0, 179, 248, 116, 22, 183, 71, 55, 241, 211, 131, 98, 156, 7, 171, 72, 149, 215, 54, 228, 67, 122, 139, 222, 145, 27, 181, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 230, 125, 202, 153, 218, 143, 93, 72, 155, 193, 199, 243, 99, 227, 145, 168, 130, 69, 76, 49, 156, 6, 103, 171, 118, 72, 8, 143, 200, 107, 182, 206, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    operator = Operator.deserialize(operator_bytes)

    assert operator.base == Pubkey.from_string("4hevZmdEmEpUp5tawzB5ZtkEcrFrEiSd3VbsvVQPk8fe")
    assert operator.admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert operator.ncn_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert operator.vault_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert operator.delegate_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert operator.metadata_admin == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert operator.voter == Pubkey.from_string("GWk2DoJez1mwMWStprqusThgbzW8RmvgznnnXXqWHJoo")
    assert operator.index == 0

    assert operator.ncn_count == 1
    assert operator.vault_count == 1
    assert operator.operator_fee_bps == 0

    assert operator.bump == 254

