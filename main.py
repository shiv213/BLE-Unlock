from ble_lib import check_for_device
import os
import time

timeout = 2
device_mac_address = "d7:dc:1c:87:57:1f"
unlocked = True
max_attempts = 5
attempts = 0

while True:
    code = check_for_device(device_mac_address, timeout)
    if code == 0:
        print("Found device")
        attempts = 0
        if not unlocked:
            unlocked = True
            print("Unlocking...")
            os.system("loginctl unlock-session")
    elif code == 1:
        print(
            "Failed to find device, locking after %d more fails"
            % (max_attempts - attempts)
        )
        time.sleep(1)
        attempts += 1
        if unlocked and attempts == max_attempts:
            unlocked = False
            print("Locking...")
            os.system("loginctl lock-session")
            attempts = 0

    if unlocked:
        time.sleep(1)
    else:
        time.sleep(5)
