import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.vault.delegation_state import DelegationState

class VaultOperatorDelegation:

    discriminator: typing.ClassVar = 4

    vault: Pubkey
    operator: Pubkey

    delegation_state: DelegationState
    last_update_slot: int
    index: int
    bump: int

    # Initialize a VaultOperatorDelegation instance with required attributes
    def __init__(self, vault: Pubkey, operator: Pubkey, delegation_state: DelegationState, last_update_slot: int, index: int,  bump: int):
        self.vault = vault
        self.operator = operator

        self.delegation_state = delegation_state
        self.last_update_slot = last_update_slot
        self.index = index
        self.bump = bump

    @staticmethod
    def deserialize(data: bytes) -> "VaultOperatorDelegation":
        """Deserializes bytes into a VaultOperatorDelegation instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        operator = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        delegation_state = DelegationState.deserialize(data[offset:offset + 8 + 8 + 8])
        offset += 8 + 8 + 8 + 256

        last_update_slot = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new VaultNcnTicket instance with the deserialized data
        return VaultOperatorDelegation(
            vault=vault,
            operator=operator,
            delegation_state=delegation_state,
            last_update_slot=last_update_slot,
            index=index,
            bump=bump,
        )

    @staticmethod
    def seeds(vault: Pubkey, operator: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"vault_operator_delegation", bytes(vault), bytes(operator)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, vault: Pubkey, operator: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = VaultOperatorDelegation.seeds(vault, operator)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds

    # Display VaultOperatorDelegation
    def __str__(self):
        return (
            f"VaultOperatorDelegation(\n"
            f"  vault={self.vault},\n"
            f"  operator={self.operator},\n"
            f"  delegation_state={self.delegation_state},\n"
            f"  last_update_slot={self.last_update_slot},\n"
            f"  index={self.index},\n"
            f"  bump={self.bump},\n"
            f")"
        )
