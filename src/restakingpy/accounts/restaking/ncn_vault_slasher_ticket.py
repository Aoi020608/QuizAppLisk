import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.core.slot_toggle import SlotToggle

class NcnVaultSlasherTicket:
    """
    The NcnVaultSlasherTicket is created by the NCN and it tracks the state of a node consensus network opting-in to a vault slasher.
    The NcnVaultSlasherTicket can be activated and deactivated over time.
    The NcnVaultSlasherTicket can slash a specific operator that's receiving delegation from a vault for a maximum amount per epoch.

    ...

    Attributes
    ----------
    ncn : Pubkey
        The NCN account
    
    vault : Pubkey
        The vault account this slasher can slash

    slasher : Pubkey
        The slasher signer

    max_slashable_per_epoch : int
        The max slashable funds per epoch per operator

    index : int
        The index

    state : SlotToggle
        State of the NCN slasher

    bump : int
        The bump seed for the PDA


    Methods
    -------
    deserialize(data: bytes)
        Deserialize the account data to NcnVaultSlasherTicket struct

    seeds(ncn: Pubkey, vault: Pubkey, slasher: Pubkey):
        Returns the seeds for the PDA

    find_program_address(program_id: Pubkey, ncn: Pubkey, vault: Pubkey, slasher: Pubkey):
        Find the program address for the NcnVaultSlasherTicket account
    """

    discriminator: typing.ClassVar = 7

    ncn: Pubkey
    vault:Pubkey
    slasher:Pubkey

    max_slashable_per_epoch: int
    index: int
    state: SlotToggle
    bump: int

    # Initialize a NcnVaultSlasherTicket instance with required attributes
    def __init__(self, ncn: Pubkey, vault: Pubkey, slasher: Pubkey, max_slashable_per_epoch: int, index: int, state: SlotToggle, bump: int):
        self.ncn = ncn
        self.vault = vault
        self.slasher = slasher
        self.max_slashable_per_epoch = max_slashable_per_epoch
        self.index = index
        self.state = state
        self.bump = bump

    @staticmethod
    def deserialize(data: bytes) -> "NcnVaultSlasherTicket":
        """Deserializes bytes into a NcnVaultSlasherTicket instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        # NCN
        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Vault
        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Slasher
        slasher = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Max Slashable Per Epoch
        max_slashable_per_epoch = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Index
        index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        # State
        state = SlotToggle.deserialize(data[offset:offset + 8 + 8 + 32])
        offset += 8 + 8 + 32

        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new NcnVaultSlasherTicket instance with the deserialized data
        return NcnVaultSlasherTicket(
            ncn=ncn,
            vault=vault,
            slasher=slasher,
            max_slashable_per_epoch=max_slashable_per_epoch,
            index=index,
            state=state,
            bump=bump
        )

    @staticmethod
    def seeds(ncn: Pubkey, vault: Pubkey, slasher: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"ncn_slasher_ticket", bytes(ncn), bytes(vault), bytes(slasher)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, ncn: Pubkey, vault: Pubkey, slasher: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = NcnVaultSlasherTicket.seeds(ncn, vault, slasher)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds

    # Display NcnVaultSlasherTicket
    def __str__(self):
        return (
            f"NcnVaultSlasherTicket(\n"
            f"  ncn={self.ncn},\n"
            f"  vault={self.vault},\n"
            f"  slasher={self.slasher},\n"
            f"  max_slashable_per_epoch={self.max_slashable_per_epoch},\n"
            f"  index={self.index},\n"
            f"  state={self.state},\n"
            f"  bump={self.bump},\n"
            f")"
        )

