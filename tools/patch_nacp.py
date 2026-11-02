#!/usr/bin/env python3
"""
Patch Nintendo Switch control.nacp for Official Account Save Data (Option A):
- StartupUserAccount (0x3025, u8) = 1 (Required: HOS prompts user selector on launch)
- SaveDataOwnerId (0x3078, u64) = 0x0100A1B2C3D40000
- UserAccountSaveDataSize (0x3080, u64) = 16 MiB (0x01000000)
- UserAccountSaveDataJournalSize (0x3088, u64) = 16 MiB (0x01000000)
- UserAccountSaveDataSizeMax (0x3148, u64) = 32 MiB (0x02000000)
- UserAccountSaveDataJournalSizeMax (0x3150, u64) = 32 MiB (0x02000000)
"""

import struct
import sys

TITLE_ID = 0x0100A1B2C3D40000
SAVE_SIZE = 16 * 1024 * 1024      # 16 MiB
JOURNAL_SIZE = 16 * 1024 * 1024   # 16 MiB
SAVE_MAX = 32 * 1024 * 1024       # 32 MiB
JOURNAL_MAX = 32 * 1024 * 1024    # 32 MiB


def patch_nacp(path: str) -> None:
    with open(path, "rb") as f:
        data = bytearray(f.read())

    if len(data) != 0x4000:
        raise ValueError(f"Unexpected control.nacp size: {len(data)} (expected 0x4000)")

    # StartupUserAccount: 1 = Required (prompts HOS user selector at launch)
    data[0x3025] = 1

    # SaveDataOwnerId
    struct.pack_into("<Q", data, 0x3078, TITLE_ID)

    # UserAccountSaveDataSize & UserAccountSaveDataJournalSize
    struct.pack_into("<Q", data, 0x3080, SAVE_SIZE)
    struct.pack_into("<Q", data, 0x3088, JOURNAL_SIZE)

    # UserAccountSaveDataSizeMax & UserAccountSaveDataJournalSizeMax
    struct.pack_into("<Q", data, 0x3148, SAVE_MAX)
    struct.pack_into("<Q", data, 0x3150, JOURNAL_MAX)

    with open(path, "wb") as f:
        f.write(data)

    print(f"Patched {path}:")
    print(f"  StartupUserAccount (0x3025)            = {data[0x3025]}")
    print(f"  SaveDataOwnerId (0x3078)               = 0x{struct.unpack_from('<Q', data, 0x3078)[0]:016X}")
    print(f"  UserAccountSaveDataSize (0x3080)       = 0x{struct.unpack_from('<Q', data, 0x3080)[0]:08X} ({SAVE_SIZE // (1024 * 1024)} MiB)")
    print(f"  UserAccountSaveDataJournalSize (0x3088)= 0x{struct.unpack_from('<Q', data, 0x3088)[0]:08X} ({JOURNAL_SIZE // (1024 * 1024)} MiB)")
    print(f"  UserAccountSaveDataSizeMax (0x3148)    = 0x{struct.unpack_from('<Q', data, 0x3148)[0]:08X} ({SAVE_MAX // (1024 * 1024)} MiB)")
    print(f"  UserAccountSaveDataJournalMax (0x3150) = 0x{struct.unpack_from('<Q', data, 0x3150)[0]:08X} ({JOURNAL_MAX // (1024 * 1024)} MiB)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/control.nacp>", file=sys.stderr)
        sys.exit(1)
    patch_nacp(sys.argv[1])
