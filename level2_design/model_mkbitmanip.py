# See LICENSE.iitm for details

from cocotb.binary import BinaryValue
import os
import sys
import operator
from cocotb.result import ReturnValue

def bitmanip(mav_putvalue_instr, mav_putvalue_src1,mav_putvalue_src2, mav_putvalue_src3):
    instr=hex(mav_putvalue_instr)[2:]
    le=int(instr,16) #convert Hex  to int
    le=bin(le)[2:] #convert int to binary
    le=le.zfill(32)
    length=len(le)
    opcode = le[-7::]
    func3 = le[length-15:length-12]
    func7 = le[length-32:length-25]
    func7_imm = le[length-32:length-27]
    func7_2bit = le[length-27:length-25]
    func7_1bit = le[length-28:length-27]
    func7_fsri_1bit = le[length-27:length-26]
    func7_imm_SHFL = le[length-32:length-26]
    imm_value = le[length-25:length-20]
    imm_value_1 = le[length-25:length-20]
    fsr_imm_value = le[length-26:length-20]
    fsr_imm_value=(int(str(fsr_imm_value),2))
    imm_value=(int(str(imm_value),2))
    shamt_imm= imm_value & (31)
    shamt1= mav_putvalue_src2 & (31)
    #print("func7 {0} immvalue1 {1} : func3 {2} opcode {3} ".format(func7,imm_value_1,func3,opcode))
    #print("func7_imm {0} func7_imm_SHFL {1} func7_1bit {2} ".format(func7_imm, func7_imm_SHFL, func7_1bit))
    if((func7 == "0100000") and (func3 == "111") and (opcode == "0110011") ):
        print('--ANDN 1')
        mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2)
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0100000") and (func3 == "110") and (opcode == "0110011")):
        print('--ORN 2')
        mav_putvalue=mav_putvalue_src1 | (~mav_putvalue_src2)
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0100000") and (func3 == "100") and (opcode == "0110011")):
        print('--XNOR 3')
        mav_putvalue=mav_putvalue_src1 ^ (~mav_putvalue_src2)
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010000") and (func3 == "001") and (opcode == "0110011")):
        print('--SLO  4')
        shamt1 =mav_putvalue_src2 & (31)
        out=((mav_putvalue_src1)<< shamt1)
        res=out
        min_i=0
        max_i=shamt1
        if(shamt1==0):
           mav_putvalue = out
        else:
            while (min_i<max_i):
                res=((1 << min_i) | res)
                min_i=min_i+1
                mav_putvalue=res & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010000") and (func3 == "101") and (opcode == "0110011")):
        print('--SRO  5')
        out=((mav_putvalue_src1)>> shamt1)
        res=out
        min_i=32-shamt1
        max_i=32
        while (min_i<max_i):
            res=((1 << min_i) | res)
            min_i=min_i+1
        mav_putvalue=res & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (func3 == "001") and (opcode == "0110011")):
        print('--ROL  6')
        out=(mav_putvalue_src1 << shamt1) | (mav_putvalue_src1 >> ((32-shamt1) & (31)))
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (func3 == "101") and (opcode == "0110011")):
        print('--ROR  7')
        out=(mav_putvalue_src1 >> shamt1) | (mav_putvalue_src1 << ((32-shamt1) & (31)))
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010000") and (func3 == "010") and (opcode == "0110011")):
        print('--SH1ADD  8')
        out=(mav_putvalue_src1  << 1) +mav_putvalue_src2
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010000") and (func3 == "100") and (opcode == "0110011")):
        print('--SH2ADD  9')
        out=(mav_putvalue_src1  << 2) +mav_putvalue_src2
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010000") and (func3 == "110") and (opcode == "0110011")):
        print('--SH3ADD  10')
        out=(mav_putvalue_src1  << 3) +mav_putvalue_src2
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0100100") and (func3 == "001") and (opcode == "0110011")):
        print('--SBCLR   11')
        out= mav_putvalue_src1 & (~(1<<shamt1))
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010100") and (func3 == "001") and (opcode == "0110011")):
        print('--SBSET   12')
        out= mav_putvalue_src1 | (1<<shamt1)
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110100") and (func3 == "001") and (opcode == "0110011")):
        print('--SBINV  13')
        out= mav_putvalue_src1  ^ (1<<shamt1)
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0100100") and (func3 == "101") and (opcode == "0110011")):
        print('--SBEXT  14')
        out= 1 & (mav_putvalue_src1 >> shamt1)
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0010100") and (func3 == "101") and (opcode == "0110011")):
        print('--GORC 15 (check)')
        x=mav_putvalue_src1
        mav_putvalue=mav_putvalue_src1
        if (shamt1 & 1):
            x= x | ((x & 0x55555555)<< 1) | (( x & 0xaaaaaaaa) >>1)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 2):
            x= x | ((x & 0x33333333)<< 2) | ((x & 0xcccccccc) >>2)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 4):
            x= x | ((x & 0x0f0f0f0f)<< 4) | (( x & 0xf0f0f0f0) >>4)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 8):
            x= x | ((x & 0x00ff00ff)<< 8) | ((x & 0xff00ff00) >>8)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 16):
            x= x | ((x & 0x0000ffff)<< 16) | ((x & 0xffff0000) >>16)
            mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110100") and (func3 == "101") and (opcode == "0110011")):
        print('--GREV  16 (should check)')
        x=mav_putvalue_src1
        mav_putvalue=mav_putvalue_src1
        if (shamt1 & 1):
            x= ((x & 0x55555555)<< 1) | (( x & 0xaaaaaaaa) >>1)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 2):
            x= ((x & 0x33333333)<< 2) | (( x & 0xcccccccc) >>2)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 4):
            x= ((x & 0x0f0f0f0f)<< 4) | (( x & 0xf0f0f0f0) >>4)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 8):
            x= ((x & 0x00ff00ff)<< 8) | (( x & 0xff00ff00) >>8)
            mav_putvalue=x & 0xffffffff
        if (shamt1 & 16):
            x= ((x & 0x0000ffff)<< 16) | (( x & 0xffff0000) >>16)
            mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_2bit == "11") and (func3 == "001") and (opcode == "0110011")):
        print('--CMIX  17')
        out= (mav_putvalue_src1 & mav_putvalue_src2) |(mav_putvalue_src3 & (~mav_putvalue_src2))
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_2bit == "11") and (func3 == "101") and (opcode == "0110011")):
        print('--CMOV 18')
        if (mav_putvalue_src2):
            mav_putvalue=mav_putvalue_src1
        else:
            mav_putvalue=mav_putvalue_src3
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_2bit == "10") and (func3 == "001") and (opcode == "0110011")):
        print('--FSL 19')
        shamt12= mav_putvalue_src2 & (63)
        A= mav_putvalue_src1
        B= mav_putvalue_src3
        if(shamt12>=32):
            shamt12=shamt12-32
            A= mav_putvalue_src3
            B= mav_putvalue_src1
        if(shamt12):
            mav_putvalue= (A << shamt12) | (B >> (32-shamt12))
        else:
            mav_putvalue=A
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_2bit == "10") and (func3 == "101") and (opcode == "0110011")):
        print('--FSR  20(check)')
        shamt12= mav_putvalue_src2 & (63)
        A= mav_putvalue_src1
        B= mav_putvalue_src3
        if(shamt12>=32):
            shamt12=shamt12-32
            A= mav_putvalue_src3
            B= mav_putvalue_src1
        if(shamt12):
            mav_putvalue= (A >> shamt12) | (B << (32-shamt12))
        else:
            mav_putvalue=A
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "00000") and (func3 == "001") and (opcode == "0010011")):
        print('--CLZ   21')
        x=bin(mav_putvalue_src1)[2:]
        x=x.zfill(32)
        mav_putvalue = len(x.split('1', 1)[0])
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "00001") and (func3 == "001") and (opcode == "0010011")):
        print('--CTZ    22')
        x=bin(mav_putvalue_src1)[2:]
        x=x.zfill(32)
        m = str(x)
        mav_putvalue = len(m)-len(m.rstrip('0'))
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue
    
    if((func7 == "0110000") and (imm_value_1 == "00010") and (func3 == "001") and (opcode == "0010011")):
        print('--PCNT   23')
        binary = bin(mav_putvalue_src1)
        setBits = [ones for ones in binary[2:] if ones=='1']
        mav_putvalue= len(setBits)
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "00100") and (func3 == "001") and (opcode == "0010011")):
        print('--SEXT.B  24')
        le=mav_putvalue_src1
        lex=bin(le)[2:]
        lex=lex.zfill(32)
        imm_value = lex[24]
        min_i=8
        max_i=32
        while (min_i<max_i):
            if(imm_value=='1'):
                le=((1 << min_i) | le)
                min_i=min_i+1
            else:
                le=((1 << min_i) | le)
                min_i=min_i+1
                le=le & 0x000000ff
        mav_putvalue=le & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "00101") and (func3 == "001") and (opcode == "0010011")):
        print('--SEXT.H  25')
        le=mav_putvalue_src1
        lex=bin(le)[2:]
        lex=lex.zfill(32)
        imm_value = lex[16]
        min_i=16
        max_i=32
        while (min_i<max_i):
            if(imm_value=='1'):
                le=((1 << min_i) | le)
                min_i=min_i+1
            else:
                le=((1 << min_i) | le)
                min_i=min_i+1
                le=le & 0x0000ffff
        mav_putvalue=le & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "10000") and (func3 == "001") and (opcode == "0010011")):
        print('--CRC32.B 26')
        i=0
        x = mav_putvalue_src1
        while i<8:
            x = (x  >> 1) ^ (0xedb88320 & ~((x &1)-1));
            i+=1
        mav_putvalue=x
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "10001") and (func3 == "001") and (opcode == "0010011")):
        print('--CRC32.H  27')
        i=0
        x = mav_putvalue_src1
        while i<16:
            x = (x  >> 1) ^ (0xedb88320 & ~((x &1)-1));
            i+=1
        mav_putvalue=x
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "10010") and (func3 == "001") and (opcode == "0010011")):
        print('--CRC32.W  28')
        i=0
        x = mav_putvalue_src1
        while i<32:
            x = (x  >> 1) ^ (0xedb88320 & ~((x &1)-1));
            i+=1
        mav_putvalue=x
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "11000") and (func3 == "001") and (opcode == "0010011")):
        print('--CRC32C.B 29')
        i=0
        x = mav_putvalue_src1
        while i<8:
            x = (x  >> 1) ^ (0x82F63B78 & ~((x &1)-1));
            i+=1
        mav_putvalue=x
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "11001") and (func3 == "001") and (opcode == "0010011")):
        print('--CRC32C.H  30')
        i=0
        x = mav_putvalue_src1
        while i<16:
            x = (x  >> 1) ^ (0x82F63B78 & ~((x &1)-1));
            i+=1
        mav_putvalue=x
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0110000") and (imm_value_1 == "11010") and (func3 == "001") and (opcode == "0010011")):
        print('--CRC32C.W  31')
        i=0
        x = mav_putvalue_src1
        while i<32:
            x = (x  >> 1) ^ (0x82F63B78 & ~((x &1)-1));
            i+=1
        mav_putvalue=x
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000101")  and (func3 == "001") and (opcode == "0110011")):
        print('--CLMUL  32')
        x=0
        i=0
        while i<32:
            if ((mav_putvalue_src2 >> i) & 1):
                x =x ^ mav_putvalue_src1 << i
            i=i+1
        mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000101")  and (func3 == "011") and (opcode == "0110011")):
        print('--CLMULH  33')
        x=0
        i=1
        while i<32:
            if ((mav_putvalue_src2 >> i) & 1):
                x =x ^ mav_putvalue_src1 >> (32-i)
            i=i+1
        mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000101")  and (func3 == "010") and (opcode == "0110011")):
        print('--CLMULR  34')
        x=0
        i=0
        while i<32:
            if ((mav_putvalue_src2 >> i) & 1):
                x =x ^ mav_putvalue_src1 >> (32-i-1)
            i=i+1
        mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000101")  and (func3 == "100") and (opcode == "0110011")):
        print('--MIN  35')
        le1=mav_putvalue_src1
        lex=bin(le1)[2:]
        lex=lex.zfill(32)
        imm_value1 = lex[0]
        le2=mav_putvalue_src2
        ex=bin(le2)[2:]
        ex=ex.zfill(32)
        imm_value2 = ex[0]
        if(imm_value1=='1') and (imm_value2=='0'):
            mav_putvalue_src1=(mav_putvalue_src1<<1)|1
            return mav_putvalue_src1
        if(imm_value1=='0') and (imm_value2=='1'):
            mav_putvalue_src2=(mav_putvalue_src2<<1)|1
            return mav_putvalue_src2
        if((imm_value1=='0') and (imm_value2=='0')) or ((imm_value1=='1') and (imm_value2=='1')) :
            if (mav_putvalue_src1 < mav_putvalue_src2):
                mav_putvalue_src1=(mav_putvalue_src1<<1)|1
                return mav_putvalue_src1
            else:
                mav_putvalue_src2=(mav_putvalue_src2<<1)|1
                return mav_putvalue_src2

    if((func7 == "0000101")  and (func3 == "101") and (opcode == "0110011")):
        print('--MAX 36')
        le1=mav_putvalue_src1
        lex=bin(le1)[2:]
        lex=lex.zfill(32)
        imm_value1 = lex[0]
        le2=mav_putvalue_src2
        ex=bin(le2)[2:]
        ex=ex.zfill(32)
        imm_value2 = ex[0]
        if(imm_value1=='1') and (imm_value2=='0'):
            mav_putvalue_src2=(mav_putvalue_src2<<1)|1
            return mav_putvalue_src2
        if(imm_value1=='0') and (imm_value2=='1'):
            mav_putvalue_src1=(mav_putvalue_src1<<1)|1
            return mav_putvalue_src1
        if((imm_value1=='0') and (imm_value2=='0')) or ((imm_value1=='1') and (imm_value2=='1'))  :
            if (mav_putvalue_src1 > mav_putvalue_src2):
                mav_putvalue_src1=(mav_putvalue_src1<<1)|1
                return mav_putvalue_src1
            else:
                mav_putvalue_src2=(mav_putvalue_src2<<1)|1
                return mav_putvalue_src2

    if((func7 == "0000101")  and (func3 == "110") and (opcode == "0110011")):
        print('--MINU  37')
        if (mav_putvalue_src1 <  mav_putvalue_src2):
            mav_putvalue=mav_putvalue_src1
        else:
             mav_putvalue=mav_putvalue_src2
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000101")  and (func3 == "111") and (opcode == "0110011")):
        print('--MAXU 38')
        if (mav_putvalue_src1 >  mav_putvalue_src2):
            mav_putvalue=mav_putvalue_src1
        else:
             mav_putvalue=mav_putvalue_src2
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0100100")  and (func3 == "110") and (opcode == "0110011")):
        print('--BDEP 39')
        r=0
        j=0
        for i in range(32):
            if ((mav_putvalue_src2 >> i) & 1):
                if ((mav_putvalue_src1 >> j) & 1):
                    r |= 1 << i
                j=j+1
        mav_putvalue=r
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000100")  and (func3 == "110") and (opcode == "0110011")):
        print('--BEXT 40')
        r=0
        j=0
        for i in range(32):
                if ((mav_putvalue_src2 >> i) & 1):
                    if ((mav_putvalue_src1 >> i) & 1):
                        r |= 1 << j
                    j=j+1
        mav_putvalue=r
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000100")  and (func3 == "100") and (opcode == "0110011")):
        print('--PACK 41')
        lower = (mav_putvalue_src1 << 16) >> 16
        lower=lower & 0x0000ffff
        upper =mav_putvalue_src2 << 16
        mav_putvalue=lower | upper
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0100100")  and (func3 == "100") and (opcode == "0110011")):
        print('--PACKU 42')
        lower = (mav_putvalue_src1 >> 16)
        upper =mav_putvalue_src2 >> 16 << 16
        mav_putvalue=lower | upper
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7 == "0000100")  and (func3 == "111") and (opcode == "0110011")):
        print('--PACKH 45')
        lower = mav_putvalue_src1& 255
        upper = (mav_putvalue_src2 & 255) << 8
        mav_putvalue=lower | upper
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "00100")  and (func3 == "001") and (opcode == "0010011")):
        print('--SLOI  46')
        out=((mav_putvalue_src1)<< shamt_imm)
        res=out
        min_i=0
        max_i=shamt_imm
        while (min_i<max_i):
            res=((1 << min_i) | res)
            min_i=min_i+1
        mav_putvalue=res & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue
#        uint_xlen_t sro(uint_xlen_t rs1, uint_xlen_t rs2)
#        {
#           int shamt = rs2 & (XLEN - 1);
#           return ~(~rs1 >> shamt);
#        }
    if((func7_imm == "00100") and (func7_fsri_1bit != "1") and (func3 == "101") and (opcode == "0010011")):
        print('--SROI 47')
        out=((mav_putvalue_src1)>> shamt_imm)
        res=out
        min_i=32-shamt_imm
        max_i=32
        while (min_i<max_i):
            res=((1 << min_i) | res)
            min_i=min_i+1
        mav_putvalue=res & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "01100") and (func7_fsri_1bit != "1") and (func3 == "101") and (opcode == "0010011")):
        print('--RORI  48')
        imm_value = int(le[length-27:length-20],2)
        shamt_imm = imm_value & (31)
        out=(mav_putvalue_src1 >> shamt_imm) | (mav_putvalue_src1 << ((32-shamt_imm) & (31)))
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1

        return mav_putvalue

    if((func7_imm == "01001")  and (func3 == "001") and (opcode == "0010011")):
        print('--SBCLRI   49')
        out= mav_putvalue_src1 & (~(1<<shamt_imm))
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "00101") and (func3 == "001") and (opcode == "0010011")):
        print('--SBSETI   50')
        out= mav_putvalue_src1 | (1<<shamt_imm)
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "01101")  and (func3 == "001") and (opcode == "0010011")):
        print('--SBINVI  51')
        out= mav_putvalue_src1  ^ (1<<shamt_imm)
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "01001")  and (func3 == "101") and (opcode == "0010011")):
        print('--SBEXTI  52')
        out= 1 & (mav_putvalue_src1 >> shamt_imm)
        mav_putvalue=out & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    def suffle32(mav_putvalue_src1,maskl,maskr,n):
        x = mav_putvalue_src1 & ~(maskl | maskr)
        x =x | ((mav_putvalue_src1 << n) & maskl) | ((mav_putvalue_src1 >> n) & maskr)
        return x

    if((func7 == "0000100")  and (func3 == "001") and (opcode == "0110011")):
        print('--SHFL  53')
        x= mav_putvalue_src1
        shamt= mav_putvalue_src2 & (15)
        if(shamt & 8):
            x=suffle32(x, 0x00ff0000,0x0000ff00,8)
        if(shamt & 4):
            x=suffle32(x, 0x0f000f00,0x00f000f0,4)
        if(shamt & 2):
            x=suffle32(x, 0x30303030,0x0c0c0c0c,2)
        if(shamt & 1):
            x=suffle32(x, 0x44444444,0x22222222,1)
        x=(x<<1)|1
        return x

    if((func7 == "0000100")  and (func3 == "101") and (opcode == "0110011")):
        print('--UNSHFL  54')
        x= mav_putvalue_src1
        shamt= mav_putvalue_src2 & (15)
        mav_putvalue=mav_putvalue_src1
        if(shamt & 1):
            x=suffle32(x, 0x44444444,0x22222222,1)
            mav_putvalue=x & 0xffffffff
        if(shamt & 2):
            x=suffle32(x, 0x30303030,0x0c0c0c0c,2)
            mav_putvalue=x & 0xffffffff
        if(shamt & 4):
            x=suffle32(x, 0x0f000f00,0x00f000f0,4)
            mav_putvalue=x & 0xffffffff
        if(shamt & 8):
            x=suffle32(x, 0x00ff0000,0x0000ff00,8)
            mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm_SHFL == "000010")  and (func3 == "001") and (opcode == "0010011")):
        print('--SHFLI  55 (check)')
        imm_value = le[length-26:length-20]
        imm_value=(int(str(imm_value),2))
        x= mav_putvalue_src1
        shamt= imm_value & (15)
        x=mav_putvalue_src1
        if(shamt & 8):
            x=suffle32(x, 0x00ff0000,0x0000ff00,8)
        if(shamt & 4):
            x=suffle32(x, 0x0f000f00,0x00f000f0,4)
        if(shamt & 2):
            x=suffle32(x, 0x30303030,0x0c0c0c0c,2)
        if(shamt & 1):
            x=suffle32(x, 0x44444444,0x22222222,1)
        x=(x<<1)|1
        return x

    if((func7_imm_SHFL == "000010")  and (func3 == "101") and (opcode == "0010011")):
        print('--UNSHFLI  56  (check)')
        imm_value = le[length-26:length-20]
        imm_value=(int(str(imm_value),2))
        x= mav_putvalue_src1
        shamt= imm_value & (15)
        mav_putvalue=mav_putvalue_src1
        if(shamt & 1):
            x=suffle32(x, 0x44444444,0x22222222,1)
            mav_putvalue=x & 0xffffffff
        if(shamt & 2):
            x=suffle32(x, 0x30303030,0x0c0c0c0c,2)
            mav_putvalue=x & 0xffffffff
        if(shamt & 4):
            x=suffle32(x, 0x0f000f00,0x00f000f0,4)
            mav_putvalue=x & 0xffffffff
        if(shamt & 8):
            x=suffle32(x, 0x00ff0000,0x0000ff00,8)
            mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "00101") and (func7_fsri_1bit != "1") and (func3 == "101") and (opcode == "0010011")):
        print('--GORCI 57')
        x=mav_putvalue_src1
        if (shamt_imm & 1):
            x= x | ((x & 0x55555555)<< 1) | ((x & 0xaaaaaaaa) >>1)
        if (shamt_imm & 2):
            x= x | ((x & 0x33333333)<< 2) | ((x & 0xcccccccc) >>2)
        if (shamt_imm & 4):
            x= x| ((x & 0x0f0f0f0f)<< 4) | ((x & 0xf0f0f0f0) >>4)
        if (shamt_imm & 8):
            x= x | ((x & 0x00ff00ff)<< 8) | ((x & 0xff00ff00) >>8)
        if (shamt_imm & 16):
            x= x| ((x & 0x0000ffff)<< 16) | ((x & 0xffff0000) >>16)
        mav_putvalue=x & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue

    if((func7_imm == "01101")and(func7_fsri_1bit != "1") and (func3 == "101") and (opcode == "0010011")):
        print('--GREVI  58')
        imm_value = le[length-25:length-20]
        imm_value=(int(str(imm_value),2))
        shamt_imm= imm_value & (31)
        x=mav_putvalue_src1
        if (shamt_imm & 1):
            x= ((x & 0x55555555)<< 1) | (( x & 0xaaaaaaaa) >>1)
        if (shamt_imm & 2):
            x= ((x & 0x33333333)<< 2) | (( x & 0xcccccccc) >>2)
        if (shamt_imm & 4):
            x= ((x & 0x0f0f0f0f)<< 4) | (( x & 0xf0f0f0f0) >>4)
        if (shamt_imm & 8):
            x= ((x & 0x00ff00ff)<< 8) | (( x & 0xff00ff00) >>8)
        if (shamt_imm & 16):
            x= ((x & 0x0000ffff)<< 16) | (( x & 0xffff0000) >>16)
        
        mav_putvalue=x & 0xffffffff
        #print("mav_putvalue before adding valid bit",hex(mav_putvalue))
        mav_putvalue=(mav_putvalue<<1)|1
        #print("mav_putvalue after adding valid bit",hex(mav_putvalue))
        return mav_putvalue

    if((func7_fsri_1bit == "1")   and (func3 == "101") and (opcode == "0010011")):
        print('--_FSRI  59')
        fsr_imm_value = le[length-26:length-20]
        fsr_imm_value=(int(str(fsr_imm_value),2))
        shamt1= fsr_imm_value & (63)
        #print(shamt1)
        A= mav_putvalue_src1
        B= mav_putvalue_src3
        if(shamt1>=32):
            shamt1=shamt1-32
            A= mav_putvalue_src3
            B= mav_putvalue_src1
        if(shamt1):
            mav_putvalue= (A >> shamt1) | (B << (32-shamt1))
        else:
            mav_putvalue=A
        mav_putvalue=mav_putvalue & 0xffffffff
        #print("mav_putvalue before adding valid bit",hex(mav_putvalue))
        mav_putvalue=(mav_putvalue<<1)|1
        #print("mav_putvalue after adding valid bit",hex(mav_putvalue))
        return mav_putvalue


    def slo(src1,src2):
        print('--SLO function')
        shamt1= src2 & (31)
        out=((src1)<< shamt1)
        res=out
        min_i=0
        max_i=shamt1
        while (min_i<max_i):
            res=((1 << min_i) | res)
            min_i=min_i+1
        mav_putvalue=res & 0xffffffff
        return mav_putvalue

    if((func7 == "0100100")  and (func3 == "111") and (opcode == "0110011")):
        print('--BFP  60')
        cfg = mav_putvalue_src2 >> (16)
        leng=0
        off=0
        if((cfg>>30)==2):
            cfg = cfg>>16
        leng= (cfg>>8) & 15
        off= cfg & 31
        if leng:
            leng=leng
        else:
            leng=16
        mask = slo(0, leng) << off
        data = mav_putvalue_src2 << off
        mav_putvalue =(data & mask) | (mav_putvalue_src1 & ~mask)
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue



    #print('--INVALID ')
    return 0


