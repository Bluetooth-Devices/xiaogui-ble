"""
Parser for Xiaogui BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/xiaogui.py

MIT License applies.
"""
from __future__ import annotations

import logging
import struct

from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import SensorLibrary

_LOGGER = logging.getLogger(__name__)


def address_to_bytes(address: str) -> bytes:
    """Return the address as bytes."""
    return bytes([int(x, 16) for x in address.split(":")])


UNPACK_DATA = struct.Struct(">BHHHB").unpack

_DEVICE_TYPE_FROM_MODEL = {
    0x20: "TZC4",
    0x21: "TZC4",
    0x24: "QJ-J",
    0x25: "QJ-J",
    0x30: "TZC4",
    0x31: "TZC4",
}


class XiaoguiBluetoothDeviceData(BluetoothData):
    """Data for Xiaogui BLE sensors."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing Xiaogui BLE advertisement data: %s", service_info)
        address = service_info.address
        self.set_device_manufacturer("Xiaogui")

        mfr_list = list(service_info.manufacturer_data)
        if not mfr_list:
            return

        last_id = list(service_info.manufacturer_data)[-1]
        last_data = service_info.manufacturer_data[last_id]
        if len(last_data) != 13:
            return

        mac_trailer = last_data[-6:]
        expected_mac = address_to_bytes(service_info.address)
        if expected_mac != mac_trailer:
            return

        model = last_data[6]
        if device_type := _DEVICE_TYPE_FROM_MODEL.get(model):
            self.set_device_type(device_type)
            name = f"{device_type} {short_address(address)}"
            self.set_title(name)
            self.set_device_name(name)
        else:
            return

        changed_manufacturer_data = self.changed_manufacturer_data(service_info)
        if not changed_manufacturer_data or len(changed_manufacturer_data) > 1:
            # If len(changed_manufacturer_data) > 1 it means we switched
            # ble adapters so we do not know which data is the latest
            # and we need to wait for the next update.
            return

        last_id = list(changed_manufacturer_data)[-1]
        data = (
            int(last_id).to_bytes(2, byteorder="little")
            + changed_manufacturer_data[last_id]
        )
        xvalue = data[1:9]
        (frame_cnt, weight, impedance, control, stabilized_byte) = UNPACK_DATA(xvalue)
        packet_id = frame_cnt << 8 | stabilized_byte
        self.update_predefined_sensor(SensorLibrary.PACKET_ID__NONE, packet_id)
        if stabilized_byte in (0x20,):
            self.update_predefined_sensor(
                SensorLibrary.MASS_NON_STABILIZED__MASS_KILOGRAMS,
                weight / 10,
                "non_stabilized_mass",
            )
        elif stabilized_byte in (0x21,):
            self.update_predefined_sensor(
                SensorLibrary.MASS__MASS_KILOGRAMS, weight / 10
            )
            self.update_predefined_sensor(SensorLibrary.IMPEDANCE__OHM, impedance / 10)
        elif stabilized_byte in (0x24, 0x30):
            self.update_predefined_sensor(
                SensorLibrary.MASS_NON_STABILIZED__MASS_KILOGRAMS,
                weight / 100,
                "non_stabilized_mass",
            )
        elif stabilized_byte in (0x25, 0x31):
            self.update_predefined_sensor(
                SensorLibrary.MASS__MASS_KILOGRAMS, weight / 100
            )
            self.update_predefined_sensor(SensorLibrary.IMPEDANCE__OHM, impedance / 10)