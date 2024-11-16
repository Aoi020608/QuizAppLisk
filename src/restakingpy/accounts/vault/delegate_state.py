class DelegationState:

    staked_amount: int
    enqueued_for_cooldown_amount: int
    cooling_down_amount: int

    def __init__(self, staked_amount: int, enqueued_for_cooldown_amount: int, cooling_down_amount: int):
        self.staked_amount = staked_amount
        self.enqueued_for_cooldown_amount = enqueued_for_cooldown_amount
        self.cooling_down_amount = cooling_down_amount

    # Display SlotToggle
    def __str__(self):
        return (
            f"DelegationState(\n"
            f"  staked_amount={self.staked_amount},\n"
            f"  enqueued_for_cooldown_amount={self.enqueued_for_cooldown_amount},\n"
            f"  cooling_down_amount={self.cooling_down_amount},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "DelegationState":
        """Deserializes bytes into a SlotToggle instance."""
        
        # Define offsets for each field
        offset = 0

        staked_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        enqueued_for_cooldown_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        cooling_down_amount = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Return a new SlotToggle instance with the deserialized data
        return DelegationState(
            staked_amount,
            enqueued_for_cooldown_amount,
            cooling_down_amount
        )
