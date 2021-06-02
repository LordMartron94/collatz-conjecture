from datetime import date


class UserFlagData:
    def __init__(self, userId: int, isKicked: bool, kick_date: [date, None], remove_kick_date: [date, None],
                 kick_reason: str, isBanned: bool, ban_date: [date, None], ban_reason: str):
        self.userId = userId,
        self.isKicked = isKicked,
        self.kick_date = kick_date,
        self.remove_kick_date = remove_kick_date,
        self.kick_reason = kick_reason,
        self.isBanned = isBanned,
        self.ban_date = ban_date,
        self.ban_reason = ban_reason
