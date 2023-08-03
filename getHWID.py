import subprocess

def get_mac_hardware_uuid():
    cmd = "/usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep 'IOPlatformUUID' | awk '{print $NF}'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
    hardware_uuid = result.stdout.decode().strip()
    return hardware_uuid

mac_hardware_uuid = get_mac_hardware_uuid()
print(f"macOS Hardware UUID: {mac_hardware_uuid}")
