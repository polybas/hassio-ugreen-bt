"""Unittest for device builder."""

import unittest

from custom_components.ugreen_bt.ugreen_bt_lib.utils.device_builder import build_device
from custom_components.ugreen_bt.ugreen_bt_lib.devices.gs600 import GS600



class TestDeviceBuilder(unittest.TestCase):
    def test_build_Unknow(self):
        bt_addr = "aa:bb:cc:dd:ee:ff"
        bt_name = "PBOX56786746478"
        with self.assertRaises(TypeError):
            build_device(bt_addr, bt_name)

    def _test_device_build(self, bt_name, cls):
        bt_addr = "aa:bb:cc:dd:ee:ff"
        built = build_device(bt_addr, bt_name)

        self.assertIsInstance(built, cls)
        self.assertEqual(built.address, bt_addr)

    def test_build_gs600(self):
        self._test_device_build("AC2A56786746478", GS600)


if __name__ == '__main__':
    unittest.main()
