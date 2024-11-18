import typing

from solders.pubkey import Pubkey

from restakingpy.accounts.vault.delegation_state import DelegationState

class Vault:
    """
    The vault configuration account for the vault program.
    Manages program-wide settings and state.

    ...

    Attributes
    ----------
    base: Pubkey
        The base account of the VRT

    vrt_mint : Pubkey
        Mint of the VRT token

    supported_mint : Pubkey
        Mint of the token that is supported by the VRT
    
    vrt_supply : int
        The total number of VRT in circulation

    tokens_deposited: int
        The total number of tokens deposited

    deposit_capacity : int
        The maximum deposit capacity allowed in the mint_to instruction.
        The deposited assets in the vault may exceed the deposit_capacity during other operations, such as vault balance updates.

    delegation_state: DelegationState
        Rolled-up stake state for all operators in the set

    additional_assets_need_unstaking : int
        The amount of additional assets that need unstaking to fulfill VRT withdrawals

    vrt_enqueued_for_cooldown_amount : int
        The amount of VRT tokens in VaultStakerWithdrawalTickets enqueued for cooldown

    vrt_cooling_down_amount : int
        The amount of VRT tokens cooling down

    vrt_ready_to_claim_amount : int
        The amount of VRT tokens ready to claim

    admin : Pubkey
        Vault admin

    delegation_admin : Pubkey
        The delegation admin responsible for adding and removing delegations from operators.

    operator_admin : Pubkey
        The operator admin responsible for adding and removing operators.

    ncn_admin : Pubkey
        The node consensus network admin responsible for adding and removing support for NCNs.

    slasher_admin : Pubkey
        The admin responsible for adding and removing slashers.

    capacity_admin : Pubkey
        The admin responsible for setting the capacity

    fee_admin : Pubkey
        The admin responsible for setting the fees

    delegate_asset_admin : Pubkey
        The delegate_admin responsible for delegating assets

    fee_wallet : Pubkey
        Fee wallet account

    mint_burn_admin : Pubkey
        Optional mint signer

    metadata_admin : Pubkey
        ( For future use ) Authority to update the vault's metadata

    vault_index : int
        The index of the vault in the vault list

    ncn_count : int
        Number of VaultNcnTicket accounts tracked by this vault

    operator_count : int
        Number of VaultOperatorDelegation accounts tracked by this vault

    slasher_count : int
        Number of VaultNcnSlasherTicket accounts tracked by this vault

    last_fee_change_slot : int
        The slot of the last fee change

    last_full_state_update_slot : int
        The slot of the last time the delegations were updated

    deposit_fee_bps : int
        The deposit fee in basis points

    withdrawal_fee_bps : int
        The withdrawal fee in basis points

    next_withdrawal_fee_bps : int
        The next epoch's withdrawal fee in basis points

    reward_fee_bps : int
        Fee for each epoch

    program_fee_bps : int
        (Copied from Config) The program fee in basis points

    bump : int
        The bump seed for the PDA

    bump : int
        The bump seed for the PDA

    is_paused : bool


    Methods
    -------
    deserialize(data: bytes)
        Deserialize the account data to Config struct

    seeds(base: Pubkey):
        Returns the seeds for the PDA

    find_program_address(program_id: Pubkey, base: Pubkey):
        Find the program address for the Config account
    """

    discriminator: typing.ClassVar = 2

    # Token information and accounting
    base: Pubkey
    vrt_mint: Pubkey
    supported_mint: Pubkey
    vrt_supply: int
    tokens_deposited: int
    deposit_capacity: int
    delegationtn_state: DelegationState
    additional_assets_need_unstaking: int
    vrt_enqueued_for_cooldown_amount: int
    vrt_cooling_down_amount: int
    vrt_ready_to_claim_amount: int

    # Admins
    admin: Pubkey
    delegation_admin: Pubkey
    operator_admin: Pubkey
    ncn_admin: Pubkey
    slasher_admin: Pubkey
    capacity_admin: Pubkey
    fee_admin: Pubkey
    delegate_asset_admin: Pubkey
    fee_wallet: Pubkey
    mint_burn_admin: Pubkey
    metadata_admin: Pubkey

    # Indexing and counters
    vault_index: int
    ncn_count: int
    operator_count: int
    slasher_count: int
    last_fee_change_slot: int
    last_full_state_update_slot: int
    deposit_fee_bps: int
    withdrawal_fee_bps: int
    next_withdrawal_fee_bps: int
    reward_fee_bps: int
    program_fee_bps: int
    bump: int
    is_paused: bool

    # Initialize a Vault instance with required attributes
    def __init__(self, base: Pubkey, vrt_mint: Pubkey, supported_mint: Pubkey, vrt_supply: int, tokens_deposited: int, deposit_capacity: int, delegation_state: DelegationState, additional_assets_need_unstaking: int, vrt_enqueued_for_cooldown_amount: int, vrt_cooling_down_amount: int, vrt_ready_to_claim_amount: int, admin: Pubkey, delegation_admin: Pubkey, operator_admin: Pubkey, ncn_admin: Pubkey, slasher_admin: Pubkey, capacity_admin: Pubkey, fee_admin: Pubkey, delegate_asset_admin: Pubkey, fee_wallet: Pubkey, mint_burn_admin: Pubkey, metadata_admin: Pubkey, vault_index: int, ncn_count: int, operator_count: int, slasher_count: int, last_fee_change_slot: int, last_full_state_update_slot: int, deposit_fee_bps: int, withdrawal_fee_bps: int, next_withdrawal_fee_bps: int, reward_fee_bps: int, program_fee_bps: int, bump: int, is_paused: bool):
        self.base = base
        self.vrt_mint = vrt_mint
        self.supported_mint = supported_mint
        self.vrt_supply = vrt_supply
        self.tokens_deposited = tokens_deposited
        self.deposit_capacity = deposit_capacity
        self.delegation_state = delegation_state
        self.additional_assets_need_unstaking = additional_assets_need_unstaking
        self.vrt_enqueued_for_cooldown_amount = vrt_enqueued_for_cooldown_amount
        self.vrt_cooling_down_amount = vrt_cooling_down_amount
        self.vrt_ready_to_claim_amount = vrt_ready_to_claim_amount

        self.admin = admin
        self.delegation_admin = delegation_admin
        self.operator_admin = operator_admin
        self.ncn_admin = ncn_admin
        self.slasher_admin = slasher_admin
        self.capacity_admin = capacity_admin
        self.fee_admin = fee_admin
        self.delegate_asset_admin = delegate_asset_admin
        self.fee_wallet = fee_wallet
        self.mint_burn_admin = mint_burn_admin
        self.metadata_admin = metadata_admin

        self.vault_index = vault_index
        self.ncn_count = ncn_count
        self.operator_count = operator_count
        self.slasher_count = slasher_count
        self.last_fee_change_slot = last_fee_change_slot
        self.last_full_state_update_slot = last_full_state_update_slot
        self.deposit_fee_bps = deposit_fee_bps
        self.withdrawal_fee_bps = withdrawal_fee_bps
        self.next_withdrawal_fee_bps = next_withdrawal_fee_bps
        self.reward_fee_bps = reward_fee_bps
        self.program_fee_bps = program_fee_bps
        self.bump = bump
        self.is_paused = is_paused

    @staticmethod
    def deserialize(data: bytes) -> "Vault":
        """Deserializes bytes into a Vault instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        # Token information and accounting
        base = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        vrt_mint = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        supported_mint = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        vrt_supply = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        tokens_deposited = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        deposit_capacity = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        delegation_state = DelegationState.deserialize(data[offset:offset + 8 + 8 + 8])
        offset += 8 + 8 + 8 + 256

        additional_assets_need_unstaking = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        vrt_enqueued_for_cooldown_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        vrt_cooling_down_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        vrt_ready_to_claim_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        delegation_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        operator_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        ncn_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        slasher_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        capacity_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        fee_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        delegate_asset_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        fee_wallet = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        mint_burn_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        metadata_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        vault_index = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        ncn_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        operator_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        slasher_count = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        last_fee_change_slot = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        last_full_state_update_slot = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        deposit_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        withdrawal_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        next_withdrawal_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        reward_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        program_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        bump = int.from_bytes(data[offset:offset + 1])

        is_paused = bool.from_bytes(data[offset:offset + 1])

        # Return a new Vault instance with the deserialized data
        return Vault(
            base=base,
            vrt_mint=vrt_mint,
            supported_mint=supported_mint,
            vrt_supply=vrt_supply,
            tokens_deposited=tokens_deposited,
            deposit_capacity=deposit_capacity,
            delegation_state=delegation_state,
            additional_assets_need_unstaking=additional_assets_need_unstaking,
            vrt_enqueued_for_cooldown_amount=vrt_enqueued_for_cooldown_amount,
            vrt_cooling_down_amount=vrt_cooling_down_amount,
            vrt_ready_to_claim_amount=vrt_ready_to_claim_amount,
            admin=admin,
            delegation_admin=delegation_admin,
            operator_admin=operator_admin,
            ncn_admin=ncn_admin,
            slasher_admin=slasher_admin,
            capacity_admin=capacity_admin,
            fee_admin=fee_admin,
            delegate_asset_admin=delegate_asset_admin,
            fee_wallet=fee_wallet,
            mint_burn_admin=mint_burn_admin,
            metadata_admin=metadata_admin,
            vault_index=vault_index,
            ncn_count=ncn_count,
            operator_count=operator_count,
            slasher_count=slasher_count,
            last_fee_change_slot=last_fee_change_slot,
            last_full_state_update_slot=last_full_state_update_slot,
            deposit_fee_bps=deposit_fee_bps,
            withdrawal_fee_bps=withdrawal_fee_bps,
            next_withdrawal_fee_bps=next_withdrawal_fee_bps,
            reward_fee_bps=reward_fee_bps,
            program_fee_bps=program_fee_bps,
            bump=bump,
            is_paused=is_paused,
        )

    @staticmethod
    def seeds(base: Pubkey) -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"vault", bytes(base)]
    
    @staticmethod
    def find_program_address(program_id: Pubkey, base: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = Vault.seeds(base)
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds

    # Display Vault
    def __str__(self):
        return (
            f"Vault(\n"
            f"  vrt_mint={self.vrt_mint},\n"
            f"  supported_mint={self.supported_mint},\n"
            f"  vrt_supply={self.vrt_supply},\n"
            f"  tokens_deposited={self.tokens_deposited},\n"
            f"  deposit_capacity={self.deposit_capacity},\n"
            f"  delegation_state={self.delegation_state},\n"
            f"  additional_assets_need_unstaking={self.additional_assets_need_unstaking},\n"
            f"  vrt_enqueued_for_cooldown_amount={self.vrt_enqueued_for_cooldown_amount},\n"
            f"  vrt_cooling_down_amount={self.vrt_cooling_down_amount},\n"
            f"  vrt_ready_to_claim_amount={self.vrt_ready_to_claim_amount},\n"
            f"  admin={self.admin},\n"
            f"  delegation_admin={self.delegation_admin},\n"
            f"  operator_admin={self.operator_admin},\n"
            f"  ncn_admin={self.ncn_admin},\n"
            f"  slasher_admin={self.slasher_admin},\n"
            f"  capacity_admin={self.capacity_admin},\n"
            f"  fee_admin={self.fee_admin},\n"
            f"  delegate_asset_admin={self.delegate_asset_admin},\n"
            f"  fee_wallet={self.fee_wallet},\n"
            f"  mint_burn_admin={self.mint_burn_admin},\n"
            f"  metadata_admin={self.metadata_admin},\n"
            f"  vault_index={self.vault_index},\n"
            f"  ncn_count={self.ncn_count},\n"
            f"  operator_count={self.operator_count},\n"
            f"  slasher_count={self.slasher_count},\n"
            f"  last_fee_change_slot={self.last_fee_change_slot},\n"
            f"  last_full_state_update_slot={self.last_full_state_update_slot},\n"
            f"  deposit_fee_bps={self.deposit_fee_bps},\n"
            f"  withdrawal_fee_bps={self.withdrawal_fee_bps},\n"
            f"  next_withdrawal_fee_bps={self.next_withdrawal_fee_bps},\n"
            f"  reward_fee_bps={self.reward_fee_bps},\n"
            f"  bump={self.bump},\n"
            f"  is_paused={self.is_paused},\n"
            f")"
        )
