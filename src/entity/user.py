from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    username: str
    password: str
    role: str

    def __repr__(self):
        return f"user_id: {self.user_id}, username: {self.username}, password: {self.password}, role: {self.role}"
