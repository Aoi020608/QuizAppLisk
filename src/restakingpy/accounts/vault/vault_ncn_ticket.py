import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class VaultNcnTicket:

    discriminator: typing.ClassVar = 3

    vault: Pubkey
    ncn: Pubkey

    index: int
    state: SlotToggle
    bump: int

    # Initialize a VaultNcnTicket instance with required attributes
    def __init__(self, vault: Pubkey, ncn: Pubkey, index: int, state: SlotToggle, bump: int):
        self.vault = vault
        self.ncn = ncn

        self.index = index
        self.state = state
        self.bump = bump

    # Display VaultNcnTicket
    def __str__(self):
        return (
            f"VaultNcnTicket(\n"
            f"  vault={self.vault},\n"
            f"  ncn={self.ncn},\n"
            f"  index={self.index},\n"
            f"  state={self.state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "VaultNcnTicket":
        """Deserializes bytes into a VaultNcnTicket instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new VaultNcnTicket instance with the deserialized data
        return VaultNcnTicket(
            vault,
            ncn,
            index,
            state,
            bump,
        )

    @staticmethod
    def seeds(vault: Pubkey, ncn: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"vault_ncn_ticket", bytes(vault), bytes(ncn)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, vault: Pubkey, ncn: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = VaultNcnTicket.seeds(vault, ncn)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
