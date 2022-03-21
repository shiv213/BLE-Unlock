import gatt
from gi.repository import GObject


def get_default_adapter():
    """https://stackoverflow.com/a/49017827"""
    import dbus

    bus = dbus.SystemBus()
    try:
        manager = dbus.Interface(
            bus.get_object("org.bluez", "/"), "org.freedesktop.DBus.ObjectManager"
        )
    except dbus.exceptions.DBusException:
        raise BluetoothDisabled

    for path, ifaces in manager.GetManagedObjects().items():
        if ifaces.get("org.bluez.Adapter1") is None:
            continue
        return path.split("/")[-1]
    raise NoAdapterFound


class BLEManager(gatt.DeviceManager):
    def __init__(self, adapter_name):
        self.device_set = set()
        self.aliases = dict()
        super().__init__(adapter_name)

    def get_device_set(self):
        return self.device_set

    def set_timeout(self, timeout):
        GObject.timeout_add(timeout, self.stop)

    def device_discovered(self, device):
        self.aliases[device.mac_address] = device.alias()
        self.device_set.add(device.mac_address)

    def scan(self, timeout):
        self.start_discovery()
        self.set_timeout(timeout * 1000)
        self.run()


def check_for_device(device_mac_address, timeout):
    manager = BLEManager(adapter_name=get_default_adapter())

    if not manager.is_adapter_powered:
        print("Please turn on Bluetooth")
        exit(1)

    manager.scan(timeout)

    if device_mac_address in manager.device_set:
        return 0
    return 1


class BluetoothDisabled(Exception):
    pass


class NoAdapterFound(Exception):
    pass
