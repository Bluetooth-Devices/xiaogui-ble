from bluetooth_sensor_state_data import BluetoothServiceInfo, SensorUpdate
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from xiaogui_ble.parser import XiaoguiBluetoothDeviceData

SCALE_SERVICE_INFO = BluetoothServiceInfo(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={57280: b"\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94"},
    service_uuids=[],
    service_data={},
    source="local",
)
SCALE_SERVICE_INFO_2 = BluetoothServiceInfo(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={
        57280: b"\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94",
        63424: b"\x06\xa4\x13\x80\x00\x021_Z\\R\xd3\x94",
    },
    service_uuids=[],
    service_data={},
    source="local",
)
SCALE_SERVICE_INFO_3 = BluetoothServiceInfo(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={
        57280: b"\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94",
        63424: b"\x06\xa4\x13\x80\x00\x021_Z\\R\xd3\x94",
        6592: b"\x06\x8e\x00\x00\x00\x020_Z\\R\xd3\x94",
    },
    service_uuids=[],
    service_data={},
    source="local",
)


def test_can_create():
    XiaoguiBluetoothDeviceData()


def test_scale():
    parser = XiaoguiBluetoothDeviceData()
    result = parser.update(SCALE_SERVICE_INFO)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Xiaogui",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=17.0,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=57136,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )
    result = parser.update(SCALE_SERVICE_INFO_2)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Xiaogui",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="mass", device_id=None),
                device_class=SensorDeviceClass.MASS,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="impedance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="impedance", device_id=None),
                device_class=SensorDeviceClass.IMPEDANCE,
                native_unit_of_measurement=Units.OHM,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=17.0,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=63281,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
            DeviceKey(key="mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="mass", device_id=None),
                name="Mass",
                native_value=17.0,
            ),
            DeviceKey(key="impedance", device_id=None): SensorValue(
                device_key=DeviceKey(key="impedance", device_id=None),
                name="Impedance",
                native_value=499.2,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )

    service_info = SCALE_SERVICE_INFO_3
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Xiaogui",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="impedance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="impedance", device_id=None),
                device_class=SensorDeviceClass.IMPEDANCE,
                native_unit_of_measurement=Units.OHM,
            ),
            DeviceKey(key="mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="mass", device_id=None),
                device_class=SensorDeviceClass.MASS,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
        },
        entity_values={
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=6448,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=16.78,
            ),
            DeviceKey(key="impedance", device_id=None): SensorValue(
                device_key=DeviceKey(key="impedance", device_id=None),
                name="Impedance",
                native_value=499.2,
            ),
            DeviceKey(key="mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="mass", device_id=None),
                name="Mass",
                native_value=17.0,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )
