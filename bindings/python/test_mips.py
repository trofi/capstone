#!/usr/bin/env python

# Capstone Python bindings, by Nguyen Anh Quynnh <aquynh@gmail.com>

from capstone import *
from capstone.mips import *

MIPS_CODE  = "\x0C\x10\x00\x97\x00\x00\x00\x00\x24\x02\x00\x0c\x8f\xa2\x00\x00\x34\x21\x34\x56"
MIPS_CODE2 = "\x56\x34\x21\x34\xc2\x17\x01\x00"

all_tests = (
        (CS_ARCH_MIPS, CS_MODE_32 + CS_MODE_BIG_ENDIAN, MIPS_CODE, "MIPS-32 (Big-endian)"),
        (CS_ARCH_MIPS, CS_MODE_64 + CS_MODE_LITTLE_ENDIAN, MIPS_CODE2, "MIPS-64-EL (Little-endian)"),
)


### Test class cs
def test_class():
    def print_insn_detail(insn):
        # print address, mnemonic and operands
        print("0x%x:\t%s\t%s" %(insn.address, insn.mnemonic, insn.op_str))

        if len(insn.operands) > 0:
            print("\top_count: %u" %len(insn.operands))
            c = 0
            for i in insn.operands:
                c += 1
                if i.type == MIPS_OP_REG:
			        print("\t\toperands[%u].type: REG = %s" %(c, insn.reg_name(i.value.reg)))
                if i.type == MIPS_OP_IMM:
			        print("\t\toperands[%u].type: IMM = %x" %(c, i.value.imm))
                if i.type == MIPS_OP_MEM:
                    print("\t\toperands[%u].type: MEM" %c)
                    if i.value.mem.base != 0:
                        print("\t\t\toperands[%u].mem.base: REG = %s" \
                            %(c, insn.reg_name(i.value.mem.base)))
                    if i.value.mem.disp != 0:
                        print("\t\t\toperands[%u].mem.disp: %x" \
                            %(c, i.value.mem.disp))


    for (arch, mode, code, comment) in all_tests:
        print("*" * 30)
        print("Platform: %s" %comment)
        print("Disasm:")
    
        try:
            md = cs(arch, mode)
            for insn in md.disasm(code, 0x1000):
                print_insn_detail(insn)
                print
        except:
            print("ERROR: Arch or mode unsupported!")


test_class()
