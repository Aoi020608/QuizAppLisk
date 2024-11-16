import typing

from solders.pubkey import Pubkey

class VaultNcnSlasherOperatorTicket:

    discriminator: typing.ClassVar = 1
    vault: Pubkey
    ncn: Pubkey
    slasher: Pubkey
    operator: Pubkey
    epoch: int
    slashed: int
    bump: int

    # Initialize a Config instance with required attributes
    def __init__(self, vault: Pubkey, ncn: Pubkey, slasher: Pubkey, operator: Pubkey, epoch: int, slashed: int, bump: int):
        self.vault = vault
        self.ncn = ncn
        self.slasher = slasher
        self.operator = operator
        self.epoch = epoch
        self.slashed = slashed
        self.bump = bump

    # Display Config
    def __str__(self):
        return (
            f"VaultNcnSlasherOperatorTicket(\n"
            f"  vault={self.vault},\n"
            f"  ncn={self.ncn},\n"
            f"  slasher={self.slasher},\n"
            f"  operator={self.operator},\n"
            f"  epoch={self.epoch},\n"
            f"  slashed={self.slashed},\n"
            f"  bump={self.bump},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "VaultNcnSlasherOperatorTicket":
        """Deserializes bytes into a Config instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        ncn = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        slasher = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        operator = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        epoch = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        slashed = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return VaultNcnSlasherOperatorTicket(
            vault,
            ncn,
            slasher,
            operator,
            epoch,
            slashed,
            bump,
        )

    @staticmethod
    def seeds(vault: Pubkey, ncn: Pubkey, slasher: Pubkey, operator: Pubkey, epoch: int) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"vault_ncn_slasher_operator", bytes(vault), bytes(ncn), bytes(slasher), bytes(operator), bytes(epoch)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, vault: Pubkey, ncn: Pubkey, slasher: Pubkey, operator: Pubkey, epoch: int) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = VaultNcnSlasherOperatorTicket.seeds(vault, ncn, slasher, operator, epoch)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds
