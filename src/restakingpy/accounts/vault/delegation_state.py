class DelegationState:
    """
    Keeps track of three key amounts:

    ...

    Attributes
    ----------
    staked_amount : int
        The amount of stake that is currently active on the operator

    enqueued_for_cooldown_amount : Pubkey
        Any stake that was deactivated in the current epoch
    
    cooling_down_amount : int
        Any stake that was deactivated in the previous epoch,
        to be available for re-delegation in the current epoch + 1

    Methods
    -------
    deserialize(data: bytes)
        Deserialize the account data to DelegationState struct
    """

    staked_amount: int
    enqueued_for_cooldown_amount: int
    cooling_down_amount: int

    def __init__(self, staked_amount: int, enqueued_for_cooldown_amount: int, cooling_down_amount: int):
        self.staked_amount = staked_amount
        self.enqueued_for_cooldown_amount = enqueued_for_cooldown_amount
        self.cooling_down_amount = cooling_down_amount

    @staticmethod
    def deserialize(data: bytes) -> "DelegationState":
        """Deserializes bytes into a DelegationState instance."""
        
        # Define offsets for each field
        offset = 0

        staked_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        enqueued_for_cooldown_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        cooling_down_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Return a new DelegationState instance with the deserialized data
        return DelegationState(
            staked_amount,
            enqueued_for_cooldown_amount,
            cooling_down_amount
        )

    # Display DelegationState
    def __str__(self):
        return (
            f"DelegationState(\n"
            f"  staked_amount={self.staked_amount},\n"
            f"  enqueued_for_cooldown_amount={self.enqueued_for_cooldown_amount},\n"
            f"  cooling_down_amount={self.cooling_down_amount},\n"
            f")"
        )

