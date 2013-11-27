/* Capstone Disassembler Engine */
/* By Nguyen Anh Quynh <aquynh@gmail.com>, 2013> */

#ifndef CS_ARM64_MAP_H
#define CS_ARM64_MAP_H

#include "../../include/capstone.h"
#include "../../include/arm64.h"

// return name of regiser in friendly string
char *AArch64_reg_name(unsigned int reg);

// given internal insn id, return public instruction info
void AArch64_get_insn_id(cs_insn *insn, unsigned int id);

// given public insn id, return internal instruction ID
unsigned int AArch64_get_insn_id2(unsigned int id);

char *AArch64_insn_name(unsigned int id);

// map instruction name to instruction ID
arm64_reg AArch64_map_insn(char *name);

#endif
