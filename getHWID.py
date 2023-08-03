import subprocess

def get_mac_disk_serial_number():
    cmd = "/usr/sbin/diskutil info / | grep 'Serial Number (system)' | awk '{print $NF}'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
    serial_number = result.stdout.strip()
    return serial_number

mac_disk_serial_number = get_mac_disk_serial_number()
print(f"macOS Disk Serial Number: {mac_disk_serial_number}")
