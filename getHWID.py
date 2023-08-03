# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:31:21 2023

@author: Rajesh
"""

import psutil
import platform 
import subprocess

print(f'OS Platform ==> {platform.system()}')

osName = platform.system()

def get_mac_machine_id():
    # Run system_profiler and capture the output
    output = subprocess.check_output(["system_profiler"])
    
    # Search for the UUID and S/N in the output
    # You can modify the parsing logic based on your macOS version and desired info
    # Here we are searching for "Hardware UUID" and "Serial Number (system)"
    uuid = output.decode().split("Hardware UUID:")[1].splitlines()[0].strip()
    serial_number = output.decode().split("Serial Number (system):")[1].splitlines()[0].strip()
    
    return uuid, serial_number

def get_linux_machine_id():
    # Run dmidecode and capture the output
    output = subprocess.check_output(["dmidecode"])
    # You can modify the parsing logic based on the output format of dmidecode
    # Here we are searching for "UUID":"
    uuid = output.decode().split("UUID:")[1].splitlines()[0].strip()
    print('Linux Output',output)
    return uuid

def get_windows_machine_id():
    # Get the BIOS UUID
    bios_uuid = psutil.win_bios_uuid()
    
    # Get the disk serial number of the system drive
    system_drive = psutil.disk_partitions()[0].device
    disk_serial_number = psutil.disk_usage(system_drive).serial_number
    
    return bios_uuid, disk_serial_number

if osName=='Windows':
    bios_uuid, disk_serial_number = get_windows_machine_id()
    print(f"Windows BIOS UUID: {bios_uuid}")
    print(f"Windows System Drive Serial Number: {disk_serial_number}")
elif osName== 'Linux':
    linux_uuid, linux_serial_number = get_linux_machine_id()
    print(f"Linux UUID: {linux_uuid}")
    print(f"Linux Serial Number: {linux_serial_number}")
else:
    mac_uuid, mac_serial_number = get_mac_machine_id()
    print(f"macOS Hardware UUID: {mac_uuid}")
    print(f"macOS Serial Number: {mac_serial_number}")