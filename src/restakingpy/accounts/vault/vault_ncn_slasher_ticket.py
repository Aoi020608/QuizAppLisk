import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class VaultNcnSlasherTicket:

    discriminator: typing.ClassVar = 5

    vault: Pubkey
    ncn: Pubkey
    slasher: Pubkey

    max_slashable_per_epoch: int
    index: int
    state: SlotToggle
    bump: int

    # Initialize a VaultNcnSlasherTicket instance with required attributes
    def __init__(self, vault: Pubkey, ncn: Pubkey, slasher: Pubkey, max_slashable_per_epoch: int, index: int, state: SlotToggle, bump: int):
        self.vault = vault
        self.ncn = ncn
        self.slasher = slasher

        self.max_slashable_per_epoch = max_slashable_per_epoch
        self.state = state
        self.index = index
        self.bump = bump

    # Display VaultNcnSlasherTicket
    def __str__(self):
        return (
            f"VaultNcnSlasherTicket(\n"
            f"  vault={self.vault},\n"
            f"  ncn={self.ncn},\n"
            f"  slasher={self.slasher},\n"
            f"  max_slashable_per_epoch={self.max_slashable_per_epoch},\n"
            f"  state={self.state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "VaultNcnSlasherTicket":
        """Deserializes bytes into a VaultNcnSlasherTicket instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        slasher = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        max_slashable_per_epoch = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new VaultNcnSlasherTicket instance with the deserialized data
        return VaultNcnSlasherTicket(
            vault,
            ncn,
            slasher,
            max_slashable_per_epoch,
            index,
            state,
            bump,
        )

    @staticmethod
    def seeds(vault: Pubkey, ncn: Pubkey, slasher: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"vault_slasher_ticket", bytes(vault), bytes(ncn), bytes(slasher)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, vault: Pubkey, ncn: Pubkey, slasher: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = VaultNcnSlasherTicket.seeds(vault, ncn, slasher)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
