from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.ncn_operator_state import NcnOperatorState

def test_pubkey_ncn_operator_state():
    expected_pubkey = Pubkey.from_string("F85CoUrtYpTN7G5Sr6HpsndsQhd2nzEnTyZdLXvjhfmi")

    program_id = Pubkey.from_string("RestkWeAVL8fRGgzhfeoqFhsqKRchg6aa1XrcH96z4Q")
    ncn = Pubkey.from_string("3gWkEDrg3DP5pYGfB53ic5HWL8yMWpJJ5Y4WoLuTX4dx")
    operator = Pubkey.from_string("2Uit7hCcTnMFFDYszysxMMWYuh2s2r6UfQAw8D1T5PNW")

    pubkey, _, _ = NcnOperatorState.find_program_address(program_id, ncn, operator)

    assert pubkey == expected_pubkey


def test_deserialize_ncn_operator_state():
    ncn_operator_state_bytes = bytes( [4, 0, 0, 0, 0, 0, 0, 0, 39, 214, 168, 149, 199, 240, 9, 111, 210, 6, 111, 131, 207, 176, 242, 181, 115, 171, 29, 152, 114, 192, 171, 154, 47, 104, 26, 221, 190, 170, 137, 91, 21, 245, 185, 95, 40, 39, 249, 71, 159, 27, 46, 62, 14, 243, 25, 154, 165, 199, 239, 161, 162, 237, 58, 76, 58, 22, 8, 112, 246, 150, 146, 183, 0, 0, 0, 0, 0, 0, 0, 0, 148, 9, 15, 20, 0, 0, 0, 0, 148, 9, 15, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 148, 9, 15, 20, 0, 0, 0, 0, 148, 9, 15, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) 

    assert ncn_operator_state_bytes[0] == NcnOperatorState.discriminator

    ncn_operator_state = NcnOperatorState.deserialize(ncn_operator_state_bytes)

    assert ncn_operator_state.ncn == Pubkey.from_string("3gWkEDrg3DP5pYGfB53ic5HWL8yMWpJJ5Y4WoLuTX4dx")
    assert ncn_operator_state.operator == Pubkey.from_string("2Uit7hCcTnMFFDYszysxMMWYuh2s2r6UfQAw8D1T5PNW")
    assert ncn_operator_state.index == 0

    assert ncn_operator_state.ncn_opt_in_state.slot_added == 336529812
    assert ncn_operator_state.ncn_opt_in_state.slot_removed == 336529812

    assert ncn_operator_state.operator_opt_in_state.slot_added == 336529812
    assert ncn_operator_state.operator_opt_in_state.slot_removed == 336529812

    assert ncn_operator_state.bump == 254

