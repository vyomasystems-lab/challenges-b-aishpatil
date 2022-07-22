# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)  # reference model

VERILOG_SOURCES = $(PWD)/mkbitmanip.v

TOPLEVEL := mkbitmanip        # design
MODULE   := test_mkbitmanip   # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
