import typing

from solders.pubkey import Pubkey

class VaultStakerWithdrawalTicket:

    discriminator: typing.ClassVar = 7

    vault: Pubkey
    staker: Pubkey
    base: Pubkey

    vrt_amount: int
    slot_unstaked: int
    bump: int

    # Initialize a VaultStakerWithdrawalTicket instance with required attributes
    def __init__(self, vault: Pubkey, staker: Pubkey, base: Pubkey, vrt_amount: int, slot_unstaked: int, bump: int):
        self.vault = vault
        self.staker = staker
        self.base = base

        self.vrt_amount = vrt_amount
        self.slot_unstaked = slot_unstaked
        self.bump = bump

    @staticmethod
    def deserialize(data: bytes) -> "VaultStakerWithdrawalTicket":
        """Deserializes bytes into a VaultStakerWithdrawalTicket instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        vault = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        staker = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        base = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        vrt_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        slot_unstaked = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new VaultNcnTicket instance with the deserialized data
        return VaultStakerWithdrawalTicket(
            vault=vault,
            staker=staker,
            base=base,
            vrt_amount=vrt_amount,
            slot_unstaked=slot_unstaked,
            bump=bump,
        )

    @staticmethod
    def seeds(vault: Pubkey, base: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"vault_staker_withdrawal_ticket", bytes(vault), bytes(base)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, vault: Pubkey, base: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = VaultStakerWithdrawalTicket.seeds(vault, base)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds

    # Display VaultStakerWithdrawalTicket
    def __str__(self):
        return (
            f"VaultStakerWithdrawalTicket(\n"
            f"  vault={self.vault},\n"
            f"  staker={self.staker},\n"
            f"  base={self.base},\n"
            f"  vrt_amount={self.vrt_amount},\n"
            f"  slot_unstaked={self.slot_unstaked},\n"
            f"  bump={self.bump},\n"
            f")"
        )
