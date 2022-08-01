# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *


# AND - 7033 -00000000000000000111000000110011
# OR  - 6033  - 00000000000000000110000000110011

instruction = {}

instruction[0] = 0x40006033
instruction[1] = 0x40006033
instruction[2] = 0x40004033
instruction[3] = 0x20001033
instruction[4] = 0x20005033
instruction[5] = 0x60001033
instruction[6] = 0x60005033
instruction[7] = 0x20002033
instruction[8] = 0x20004033
instruction[9] = 0x20006033
instruction[10] = 0x48001033
instruction[11] = 0x28001033
instruction[12] = 0x68001033
instruction[13] = 0x48005033
instruction[14] = 0x28005033
instruction[15] = 0x68005033
instruction[16] = 0x48007033
instruction[17] = 0xA001033
instruction[18] = 0xA003033
instruction[19] = 0xA002033
instruction[20] = 0xA004033
instruction[21] = 0xA005033
instruction[22] = 0xA006033
instruction[23] = 0xA007033
instruction[24] = 0x48006033
instruction[25] = 0x8006033
instruction[26] = 0x8004033
instruction[27] = 0x48004033
instruction[28] = 0x8007033
instruction[29] = 0x60001013
instruction[30] = 0x60101013
instruction[31] = 0b01100000001000000001000000010011
instruction[32] = 0b01100000010000000001000000010011
instruction[33] = 0b01100000010111111001111110010011
instruction[34] = 0b01100001000000000001000000010011
instruction[35] = 0b01100001000100000001000000010011
instruction[36] = 0b01100001001000000001000000010011
instruction[37] = 0b01100001100000000001000000010011
instruction[38] = 0b01100001100100000001000000010011
instruction[39] = 0b01100001101000000001000000010011
instruction[40] = 0b00100000000000000001000000010011
instruction[41] = 0b01001000000000000001000000010011
instruction[42] = 0b00101000000000000001000000010011
instruction[43] = 0b01101000000000000001000000010011
instruction[44] = 0b01001000000000000101000000010011
instruction[45] = 0b00001000000000000001000000010011
instruction[46] = 0b00001000000000000101000000010011
instruction[47] = 0b00000110000000000001000000110011
instruction[48] = 0b00000110000000000101000000110011
instruction[49] = 0b00000100000000000001000000110011
instruction[50] = 0b00000100000000000101000000110011
instruction[51] = 0b00000100000000000101000000010011
instruction[52] = 0b00100000000100000101000000010011
instruction[53] = 0b01100000000100000101000000010011
instruction[54] = 0b00001000000000000001000000110011
instruction[55] = 0b00001000000000000101000000110011
instruction[56] = 0b00101000000100000101000000010011
instruction[57] = 0b01101000000100000101000000010011
instruction[58] = 0b00000000000000000110000000110011
instruction[59] = 0b00000000000000000111000000110011



# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    for i in range(len(instruction)):
        # clock
        cocotb.fork(clock_gen(dut.CLK))

        # reset
        dut.RST_N.value <= 0
        yield Timer(10) 
        dut.RST_N.value <= 1

        ######### CTB : Modify the test to expose the bug #############
        # input transaction
        mav_putvalue_src1 = 0x00001001
        mav_putvalue_src2 = 0x00011101
        mav_putvalue_src3 = 0x00000010
        mav_putvalue_instr = instruction[i]

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr

        yield Timer(1) 
        print("src 1 - "+str(dut.mav_putvalue_src1.value))
        print("src 2 - "+str(dut.mav_putvalue_src2.value))
        print("src 3 - "+str(dut.mav_putvalue_src3.value))
        print("Instruction opcode - "+str(dut.mav_putvalue_instr.value)+ " at instruction "+str(i))
    

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        
        # comparison
        print(dut.mav_putvalue.value)
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        print("Instrction " + str(i) + " Success\n-------------------------")
