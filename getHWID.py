# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:31:21 2023

@author: Rajesh
"""

import psutil
import platform 
import subprocess

print(f'OS Platform ==> {platform.system()}')


def get_mac_machine_id():
    # Run system_profiler and capture the output
    output = subprocess.check_output(["system_profiler"])
    
    # Search for the UUID and S/N in the output
    # You can modify the parsing logic based on your macOS version and desired info
    # Here we are searching for "Hardware UUID" and "Serial Number (system)"
    uuid = output.decode().split("Hardware UUID:")[1].splitlines()[0].strip()
    serial_number = output.decode().split("Serial Number (system):")[1].splitlines()[0].strip()
    
    return uuid, serial_number

mac_uuid, mac_serial_number = get_mac_machine_id()
print(f"macOS Hardware UUID: {mac_uuid}")
print(f"macOS Serial Number: {mac_serial_number}")