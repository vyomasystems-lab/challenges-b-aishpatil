# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from random import randrange

#  Base Test case
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    for i in range(31):
        exec("dut.inp%d.value = randrange(4)"% i)
    await Timer(1,"ns")
    select = 11
    dut.sel.value = select
    await Timer(1,"ns")
    assert dut.out.value == dut.inp11.value, "Bug is present"
    cocotb.log.info('##### CTB:Base Test Case Completed ########')


#  Main Test case
@cocotb.test()
async def test_mux1(dut):
    inp = {}   
    for i in range(31):
        inp[i] = "dut.inp"+ str(i) + ".value"
    for i in range(31):
        exec("dut.inp%d.value = randrange(4)"% i)

    for select in range(31):
        dut.sel.value = select
        await Timer(1,"ns")
        if dut.out.value != eval(inp[select]):
            print('\nBug Found:\nThe bug is present at input line '+ str(select) + "\n" + inp[select] + "\n")   # duct.dut.inp11.value.value
            raise TestFailure("Failure!")