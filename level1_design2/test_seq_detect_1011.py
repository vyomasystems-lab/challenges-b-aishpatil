# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.result import TestFailure
from cocotb.triggers import RisingEdge, FallingEdge


def sequence_detection(inp_bit, current):
    if(current == 0):
        if(inp_bit == '0'):
            return 0
        else:
            return 1
    elif(current == 1):
        if(inp_bit == '0'):
            return 2
        else:
            return 1
    elif(current == 2):
        if(inp_bit == '0'):
            return 0
        else:
            return 3
    elif(current == 3):
        if(inp_bit == '0'):
            return 2
        else:
            return 4
    elif(current == 4):
        if(inp_bit == '0'):
            return 2
        else:
            return 1



@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """


    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    print()  

    # sequence = "1011011" # Test 1
    sequence = "101011"
    # sequence = "1011101101011101101110111011"
    print("Printing Sequence Passing bit, Correct Sequence detection and output from Verilog code")
    for element in range(0, len(sequence)):
        print( sequence[element] , end = ' ')
    print()  

    current = 0
    for element in range(0, len(sequence)):
        current = sequence_detection(sequence[element],current)
        print( "1" if current == 4 else "0" , end = ' ')    
    print()  

    for element in range(0, len(sequence)):
        if(sequence[element] == '1'):
            dut.inp_bit.value = 1
        else:
            dut.inp_bit.value = 0
        await FallingEdge(dut.clk)
        from_verilog = dut.seq_seen.value
        print(str(from_verilog), end = ' ')
    print()  
    
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0

    for element in range(0, len(sequence)):
        current = sequence_detection(sequence[element],current)

        if(sequence[element] == '1'):
            dut.inp_bit.value = 1
        else:
            dut.inp_bit.value = 0
        await FallingEdge(dut.clk)
        from_verilog = dut.seq_seen.value
        print(str(from_verilog), end = ' ')
        check = '1' if current == 4 else '0'
        assert (str(from_verilog) == check) , '\nBug Detected:\nThe bug is present On input '+ sequence[element] + "\nInput Number \t: " + str(element+1) + "\nOut from Verilog is : " + str(from_verilog) + "\nCurrent State is  \t: "+ str(current) + "\nOut must be  \t: " + "1" if current == 4 else "0" 
    print()  
