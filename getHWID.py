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
    
def get_linux_hardware_uuid():
    try:
        output = subprocess.check_output(["dmidecode", "-s", "system-uuid"], text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return None    

if osName=='Darwin':
    mac_hardware_uuid = get_mac_hardware_uuid()
    print(f"macOS Hardware UUID: {mac_hardware_uuid}")
elif osName == 'Linux':
    linux_hardware_uuid = get_linux_hardware_uuid()
    print(f"Linux Hardware UUID: {linux_hardware_uuid}")