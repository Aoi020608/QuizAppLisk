import typing
from solders.pubkey import Pubkey

class SlotToggle:

    slot_added: int
    slot_removed: int

    # Initialize a SlotToggle instance with required attributes
    def __init__(self, slot_added: int, slot_removed: int):
        self.slot_added = slot_added
        self.slot_removed = slot_removed

    # Display SlotToggle
    def __str__(self):
        return (
            f"SlotToggle(\n"
            f"  slot_added={self.slot_added},\n"
            f"  slot_removed={self.slot_removed},\n"
            f")"
        )

    @staticmethod
    def deserialize(data: bytes) -> "SlotToggle":
        """Deserializes bytes into a SlotToggle instance."""
        
        # Define offsets for each field
        offset = 0
        # offset += 8

        # Slot added
        slot_added = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8
        
        # Slot removed
        slot_removed = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Return a new SlotToggle instance with the deserialized data
        return SlotToggle(
            slot_added,
            slot_removed
        )
