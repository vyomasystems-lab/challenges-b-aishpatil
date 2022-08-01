# See LICENSE.vyoma for details
# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path
import automatic_washing_machine_python as tst

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_washing_machine_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut.door_close.value = 0
    dut.start.value = 0
    dut.filled.value = 0
    dut.detergent_added.value = 0
    dut.cycle_timeout.value = 0
    dut.drained.value = 0
    dut.spin_timeout.value = 0
    await FallingEdge(dut.clk)

    print("next_state \t: "+str(dut.next_state.value))
    print("motor_on \t: "+str(dut.motor_on.value))
    print("fill_value_on \t: "+str(dut.fill_value_on.value))
    print("drain_value_on \t: "+str(dut.drain_value_on.value))
    print("door_lock \t: "+str(dut.door_lock.value))
    print("soap_wash \t: "+str(dut.soap_wash.value))
    print("water_wash \t: "+str(dut.water_wash.value))
    print("done \t\t: "+str(dut.done.value))
    
    assert dut.next_state.value == 000, "When Door is not closed machine must wait for it to close"

