import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class NcnOperatorState:
    """
    This state represents the mutual opt-in relationship between an NCN and an Operator.
    The NCN initializes this state. Once created, the NCN and operator can both warm-up and cooldown the state to show support for each other.

    ...

    Attributes
    ----------
    ncn : Pubkey
        The NCN account
    
    operator : Pubkey
        The operator account

    index : int
        Index

    ncn_opt_in_state : int
        State of the ncn opt-ing in to the operator

    operator_opt_in_state : int
        State of the operator opt-ing in to the ncn

    slasher_count : int
        Number of slasher accounts associated with the NCN

    bump : int
        The bump seed for the PDA


    Methods
    -------
    deserialize(data: bytes)
        Deserialize the account data to NcnOperatorState struct

    seeds(ncn: Pubkey, operator: Pubkey):
        Returns the seeds for the PDA

    find_program_address(program_id: Pubkey, ncn: Pubkey, operator: Pubkey):
        Find the program address for the NcnOperatorState account
    """

    discriminator: typing.ClassVar = 4

    ncn: Pubkey
    operator:Pubkey

    index: int
    ncn_opt_in_state: SlotToggle
    operator_opt_in_state: SlotToggle
    bump: int

    # Initialize a NcnOperatorState instance with required attributes
    def __init__(self, ncn: Pubkey, operator: Pubkey, index: int, ncn_opt_in_state: SlotToggle, operator_opt_in_state: SlotToggle, bump: int):
        self.ncn = ncn
        self.operator = operator
        self.index = index
        self.ncn_opt_in_state = ncn_opt_in_state
        self.operator_opt_in_state = operator_opt_in_state
        self.bump = bump

    @staticmethod
    def deserialize(data: bytes) -> "NcnOperatorState":
        """Deserializes bytes into a NcnOperatorState instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        # ncn
        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # operator
        operator = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # index
        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        # ncn_opt_in_state
        ncn_opt_in_state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        # operator_opt_in_state
        operator_opt_in_state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        # bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new NcnOperatorState instance with the deserialized data
        return NcnOperatorState(
            ncn=ncn,
            operator=operator,
            index=index,
            ncn_opt_in_state=ncn_opt_in_state,
            operator_opt_in_state=operator_opt_in_state,
            bump=bump
        )

    @staticmethod
    def seeds(ncn: Pubkey, operator: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"ncn_operator_state", bytes(ncn), bytes(operator)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, ncn: Pubkey, operator: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = NcnOperatorState.seeds(ncn, operator)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds

    # Display NcnOperatorState
    def __str__(self):
        return (
            f"NcnOperatorState(\n"
            f"  ncn={self.ncn},\n"
            f"  operator={self.operator},\n"
            f"  index={self.index},\n"
            f"  ncn_opt_in_state={self.ncn_opt_in_state},\n"
            f"  operator_opt_in_state={self.operator_opt_in_state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

