# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:31:21 2023

@author: Rajesh
"""

import psutil
import platform 
import subprocess
import plistlib
import json

print(f'OS Platform ==> {platform.system()}')

osName = platform.system()

def get_mac_machine_id():
    # Run system_profiler and capture the output
    output = subprocess.check_output(["system_profiler"])
    print('macOS output', output.decode())
    
    # Search for the UUID and S/N in the output
    # You can modify the parsing logic based on your macOS version and desired info
    # Here we are searching for "Hardware UUID" and "Serial Number (system)"
    uuid = output.decode().split("Hardware UUID:")[1].splitlines()[0].strip()
    serial_number = output.decode().split("Serial Number (system):")[1].splitlines()[0].strip()
    
    #return uuid, serial_number

def get_linux_machine_id():
    # Run dmidecode and capture the output
    output = subprocess.check_output(["dmidecode"])
    # You can modify the parsing logic based on the output format of dmidecode
    # Here we are searching for "UUID":"
    uuid = output.decode().split("UUID:")[1].splitlines()[0].strip()
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
    linux_uuid = get_linux_machine_id()
    print(f"Linux UUID: {linux_uuid}")
else:
    cmd = "system_profiler SPHardwareDataType | awk '/Serial Number/ {print $4}'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
    serial_number = result.stdout.strip()
    print('macOS serial number1',serial_number)
    
    system_profile_data = subprocess.Popen(
    ['system_profiler', '-json', 'SPHardwareDataType'], stdout=subprocess.PIPE)
    data = json.loads(system_profile_data.stdout.read())
    serial = data.get('SPHardwareDataType', {})[0].get('serial_number')
    print('macOS serial number2',serial)