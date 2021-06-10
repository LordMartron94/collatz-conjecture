from datetime import date
from dataclasses import dataclass


@dataclass
class UserFlagData:
    """Class for storing user flag data in an object."""

    userId: int
    isKicked: bool
    kick_date: date
    remove_kick_date: date
    kick_reason: str
    isBanned: bool
    ban_date: date
    ban_reason: str

    def __repr__(self):
        return (
            f"userId: {self.userId}, isKicked: {self.isKicked}, kick_date: {self.kick_date}, "
            f"remove_kick_date: {self.remove_kick_date}, kick_reason: {self.kick_reason}, isBanned: {self.isBanned},"
            f" ban_date: {self.ban_date}, ban_reason: {self.ban_reason}"
        )
