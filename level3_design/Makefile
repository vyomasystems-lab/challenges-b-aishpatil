# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/automatic_washing_machine.v               # provide your design path

TOPLEVEL := automatic_washing_machine          # design file
MODULE   := test_automatic_washing_machine    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
