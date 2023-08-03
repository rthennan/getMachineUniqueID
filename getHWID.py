import subprocess
import platform

osName = platform.system()

print('OS Name',osName)

def get_mac_hardware_uuid():
    cmd = "/usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep 'IOPlatformUUID' | awk '{print $NF}'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
    hardware_uuid = result.stdout.decode().strip()
    return hardware_uuid

def get_disk_serial_number():
    with open('/proc/self/mounts', 'r') as f:
        root_device = next(line.split()[0] for line in f if line.startswith('/dev/'))
    with open('/sys/block/{}/serial'.format(root_device.split('/')[-1]), 'r') as f:
        return f.read().strip()

if osName=='Darwin':
    mac_hardware_uuid = get_mac_hardware_uuid()
    print(f"macOS Hardware UUID: {mac_hardware_uuid}")
elif osName == 'Linux':
    disk_serial_number = get_disk_serial_number()
    print(f"Disk Serial Number: {disk_serial_number}")