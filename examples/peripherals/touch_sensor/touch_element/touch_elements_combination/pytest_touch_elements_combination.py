# SPDX-FileCopyrightText: 2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Unlicense OR CC0-1.0
import pytest
from pytest_embedded import Dut


@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.generic
def test_touch_elements_combination(dut: Dut) -> None:
    dut.expect_exact('Touch Elements Combination Example: Touch element library installed')
    dut.expect_exact('Touch Elements Combination Example: Touch button installed')
    dut.expect_exact('Touch Elements Combination Example: Touch buttons created')
    dut.expect_exact('Touch Elements Combination Example: Touch slider installed')
    dut.expect_exact('Touch Elements Combination Example: Touch slider created')
    dut.expect_exact('Touch Elements Combination Example: Touch element library start')
