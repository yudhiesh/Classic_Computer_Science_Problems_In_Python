from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)  # generate random length bytes
    return int.from_bytes(
        bytes=tb, byteorder="big"
    )  # convert those bytes into a bit string and return it


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(bytes=original_bytes, byteorder="big")
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    # add 7 to the length of the decrypted data before using integer division by
    # 8 to ensure that we round up and thus avoiding an off-by one error
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1=key1, key2=key2)
    assert result == "One Time Pad!"
