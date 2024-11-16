from solders.pubkey import Pubkey

from restakingpy.accounts.restaking.ncn_operator_state import NcnOperatorState

def test_deserialize_ncn_operator_state():
    ncn_operator_state_bytes = bytes([4, 0, 0, 0, 0, 0, 0, 0, 189, 61, 129, 225, 194, 154, 170, 233, 182, 232, 146, 17, 216, 105, 66, 149, 165, 235, 154, 146, 138, 39, 192, 122, 29, 135, 249, 34, 48, 217, 156, 255, 49, 135, 48, 9, 181, 128, 72, 188, 40, 173, 110, 49, 70, 28, 111, 1, 199, 141, 109, 236, 240, 229, 9, 92, 102, 138, 189, 180, 143, 196, 109, 250, 0, 0, 0, 0, 0, 0, 0, 0, 29, 162, 102, 19, 0, 0, 0, 0, 29, 162, 102, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 162, 102, 19, 0, 0, 0, 0, 29, 162, 102, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    ncn_operator_state = NcnOperatorState.deserialize(ncn_operator_state_bytes)

    assert ncn_operator_state.ncn == Pubkey.from_string("DjiTEWCfVTtZuWvRcMtjBec9JFiSCUkNXAKrxzSn4CWz")
    assert ncn_operator_state.operator == Pubkey.from_string("4LLYCGQc982RyVeaewMw55PyJzrETzGkLPHBkffUPiBK")
    assert ncn_operator_state.index == 0

    assert ncn_operator_state.ncn_opt_in_state.slot_added == 325493277
    assert ncn_operator_state.ncn_opt_in_state.slot_removed == 325493277

    assert ncn_operator_state.operator_opt_in_state.slot_added == 325493277
    assert ncn_operator_state.operator_opt_in_state.slot_removed == 325493277

    assert ncn_operator_state.bump == 252

