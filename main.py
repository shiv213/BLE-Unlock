#!/usr/bin/python3

from ble_lib import check_for_device
import os
import time

device_mac_address = "d7:dc:1c:87:57:1f"
max_attempts = 7
timeout = 3

unlocked = True
attempts = 0

while True:
    if os.system("loginctl show-session -p LidClosed | grep -q 'no'") == 0:
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
