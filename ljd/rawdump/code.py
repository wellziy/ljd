#
# Copyright (C) 2013 Andrian Nord. See Copyright Notice in main.py
#

from ljd.util.log import errprint

import ljd.bytecode.instructions as instructions
import gconfig

def getIDFunc(beginNum):
	data = {}
	data["num"] = beginNum or 0
	def func():
		ret = data["num"]
		data["num"] = data["num"] + 1
		return ret
	return func

if gconfig.gBCVersion == 1:
	func = getIDFunc(0)
	_OPCODES = (
		# Comparison ops

		(func(), 	instructions.ISLT),  # @UndefinedVariable
		(func(), 	instructions.ISGE),  # @UndefinedVariable
		(func(), 	instructions.ISLE),  # @UndefinedVariable
		(func(), 	instructions.ISGT),  # @UndefinedVariable

		(func(), 	instructions.ISEQV),  # @UndefinedVariable
		(func(), 	instructions.ISNEV),  # @UndefinedVariable

		(func(), 	instructions.ISEQS),  # @UndefinedVariable
		(func(), 	instructions.ISNES),  # @UndefinedVariable

		(func(), 	instructions.ISEQN),  # @UndefinedVariable
		(func(), 	instructions.ISNEN),  # @UndefinedVariable

		(func(), 	instructions.ISEQP),  # @UndefinedVariable
		(func(), 	instructions.ISNEP),  # @UndefinedVariable

		# Unary test and copy ops

		(func(), 	instructions.ISTC),  # @UndefinedVariable
		(func(), 	instructions.ISFC),  # @UndefinedVariable

		(func(), 	instructions.IST),  # @UndefinedVariable
		(func(), 	instructions.ISF),  # @UndefinedVariable

		#(func(), 	instructions.ISTYPE),  # @UndefinedVariable
		#(func(), 	instructions.ISNUM),  # @UndefinedVariable

		# Unary ops

		(func(), 	instructions.MOV),  # @UndefinedVariable
		(func(), 	instructions.NOT),  # @UndefinedVariable
		(func(), 	instructions.UNM),  # @UndefinedVariable
		(func(), 	instructions.LEN),  # @UndefinedVariable

		# Binary ops

		(func(), 	instructions.ADDVN),  # @UndefinedVariable
		(func(), 	instructions.SUBVN),  # @UndefinedVariable
		(func(), 	instructions.MULVN),  # @UndefinedVariable
		(func(), 	instructions.DIVVN),  # @UndefinedVariable
		(func(), 	instructions.MODVN),  # @UndefinedVariable

		(func(), 	instructions.ADDNV),  # @UndefinedVariable
		(func(), 	instructions.SUBNV),  # @UndefinedVariable
		(func(), 	instructions.MULNV),  # @UndefinedVariable
		(func(), 	instructions.DIVNV),  # @UndefinedVariable
		(func(), 	instructions.MODNV),  # @UndefinedVariable

		(func(), 	instructions.ADDVV),  # @UndefinedVariable
		(func(), 	instructions.SUBVV),  # @UndefinedVariable
		(func(), 	instructions.MULVV),  # @UndefinedVariable
		(func(), 	instructions.DIVVV),  # @UndefinedVariable
		(func(), 	instructions.MODVV),  # @UndefinedVariable

		(func(), 	instructions.POW),  # @UndefinedVariable
		(func(), 	instructions.CAT),  # @UndefinedVariable

		# Constant ops

		(func(), 	instructions.KSTR),  # @UndefinedVariable
		(func(), 	instructions.KCDATA),  # @UndefinedVariable
		(func(), 	instructions.KSHORT),  # @UndefinedVariable
		(func(), 	instructions.KNUM),  # @UndefinedVariable
		(func(), 	instructions.KPRI),  # @UndefinedVariable

		(func(), 	instructions.KNIL),  # @UndefinedVariable

		# Upvalue and function ops

		(func(), 	instructions.UGET),  # @UndefinedVariable

		(func(), 	instructions.USETV),  # @UndefinedVariable
		(func(), 	instructions.USETS),  # @UndefinedVariable
		(func(), 	instructions.USETN),  # @UndefinedVariable
		(func(), 	instructions.USETP),  # @UndefinedVariable

		(func(), 	instructions.UCLO),  # @UndefinedVariable

		(func(), 	instructions.FNEW),  # @UndefinedVariable

		# Table ops

		(func(), 	instructions.TNEW),  # @UndefinedVariable

		(func(), 	instructions.TDUP),  # @UndefinedVariable

		(func(), 	instructions.GGET),  # @UndefinedVariable
		(func(), 	instructions.GSET),  # @UndefinedVariable

		(func(), 	instructions.TGETV),  # @UndefinedVariable
		(func(), 	instructions.TGETS),  # @UndefinedVariable
		(func(), 	instructions.TGETB),  # @UndefinedVariable
		#(func(), 	instructions.TGETR),  # @UndefinedVariable

		(func(), 	instructions.TSETV),  # @UndefinedVariable
		(func(), 	instructions.TSETS),  # @UndefinedVariable
		(func(), 	instructions.TSETB),  # @UndefinedVariable

		(func(), 	instructions.TSETM),  # @UndefinedVariable
		#(func(), 	instructions.TSETR),  # @UndefinedVariable

		# Calls and vararg handling

		(func(), 	instructions.CALLM),  # @UndefinedVariable
		(func(), 	instructions.CALL),  # @UndefinedVariable
		(func(), 	instructions.CALLMT),  # @UndefinedVariable
		(func(), 	instructions.CALLT),  # @UndefinedVariable

		(func(), 	instructions.ITERC),  # @UndefinedVariable
		(func(), 	instructions.ITERN),  # @UndefinedVariable

		(func(), 	instructions.VARG),  # @UndefinedVariable

		(func(), 	instructions.ISNEXT),  # @UndefinedVariable

		# Returns

		(func(), 	instructions.RETM),  # @UndefinedVariable
		(func(), 	instructions.RET),  # @UndefinedVariable
		(func(), 	instructions.RET0),  # @UndefinedVariable
		(func(), 	instructions.RET1),  # @UndefinedVariable

		# Loops and branches

		(func(), 	instructions.FORI),  # @UndefinedVariable
		(func(), 	instructions.JFORI),  # @UndefinedVariable

		(func(), 	instructions.FORL),  # @UndefinedVariable
		(func(), 	instructions.IFORL),  # @UndefinedVariable
		(func(), 	instructions.JFORL),  # @UndefinedVariable

		(func(), 	instructions.ITERL),  # @UndefinedVariable
		(func(), 	instructions.IITERL),  # @UndefinedVariable
		(func(), 	instructions.JITERL),  # @UndefinedVariable

		(func(), 	instructions.LOOP),  # @UndefinedVariable
		(func(), 	instructions.ILOOP),  # @UndefinedVariable
		(func(), 	instructions.JLOOP),  # @UndefinedVariable

		(func(), 	instructions.JMP),  # @UndefinedVariable

		# Function headers

		(func(), 	instructions.FUNCF),  # @UndefinedVariable
		(func(), 	instructions.IFUNCF),  # @UndefinedVariable
		(func(), 	instructions.JFUNCF),  # @UndefinedVariable

		(func(), 	instructions.FUNCV),  # @UndefinedVariable
		(func(), 	instructions.IFUNCV),  # @UndefinedVariable
		(func(), 	instructions.JFUNCV),  # @UndefinedVariable

		(func(), 	instructions.FUNCC),  # @UndefinedVariable
		(func(), 	instructions.FUNCCW)  # @UndefinedVariable
	)
else:
	_OPCODES = (
		# Comparison ops

		(0x00, 	instructions.ISLT),  # @UndefinedVariable
		(0x01, 	instructions.ISGE),  # @UndefinedVariable
		(0x02, 	instructions.ISLE),  # @UndefinedVariable
		(0x03, 	instructions.ISGT),  # @UndefinedVariable

		(0x04, 	instructions.ISEQV),  # @UndefinedVariable
		(0x05, 	instructions.ISNEV),  # @UndefinedVariable

		(0x06, 	instructions.ISEQS),  # @UndefinedVariable
		(0x07, 	instructions.ISNES),  # @UndefinedVariable

		(0x08, 	instructions.ISEQN),  # @UndefinedVariable
		(0x09, 	instructions.ISNEN),  # @UndefinedVariable

		(0x0A, 	instructions.ISEQP),  # @UndefinedVariable
		(0x0B, 	instructions.ISNEP),  # @UndefinedVariable

		# Unary test and copy ops

		(0x0C, 	instructions.ISTC),  # @UndefinedVariable
		(0x0D, 	instructions.ISFC),  # @UndefinedVariable

		(0x0E, 	instructions.IST),  # @UndefinedVariable
		(0x0F, 	instructions.ISF),  # @UndefinedVariable

		(0x0E, 	instructions.ISTYPE),  # @UndefinedVariable
		(0x0F, 	instructions.ISNUM),  # @UndefinedVariable

		# Unary ops

		(0x10, 	instructions.MOV),  # @UndefinedVariable
		(0x11, 	instructions.NOT),  # @UndefinedVariable
		(0x12, 	instructions.UNM),  # @UndefinedVariable
		(0x13, 	instructions.LEN),  # @UndefinedVariable

		# Binary ops

		(0x14, 	instructions.ADDVN),  # @UndefinedVariable
		(0x15, 	instructions.SUBVN),  # @UndefinedVariable
		(0x16, 	instructions.MULVN),  # @UndefinedVariable
		(0x17, 	instructions.DIVVN),  # @UndefinedVariable
		(0x18, 	instructions.MODVN),  # @UndefinedVariable

		(0x19, 	instructions.ADDNV),  # @UndefinedVariable
		(0x1A, 	instructions.SUBNV),  # @UndefinedVariable
		(0x1B, 	instructions.MULNV),  # @UndefinedVariable
		(0x1C, 	instructions.DIVNV),  # @UndefinedVariable
		(0x1D, 	instructions.MODNV),  # @UndefinedVariable

		(0x1E, 	instructions.ADDVV),  # @UndefinedVariable
		(0x1F, 	instructions.SUBVV),  # @UndefinedVariable
		(0x20, 	instructions.MULVV),  # @UndefinedVariable
		(0x21, 	instructions.DIVVV),  # @UndefinedVariable
		(0x22, 	instructions.MODVV),  # @UndefinedVariable

		(0x23, 	instructions.POW),  # @UndefinedVariable
		(0x24, 	instructions.CAT),  # @UndefinedVariable

		# Constant ops

		(0x25, 	instructions.KSTR),  # @UndefinedVariable
		(0x26, 	instructions.KCDATA),  # @UndefinedVariable
		(0x27, 	instructions.KSHORT),  # @UndefinedVariable
		(0x28, 	instructions.KNUM),  # @UndefinedVariable
		(0x29, 	instructions.KPRI),  # @UndefinedVariable

		(0x2A, 	instructions.KNIL),  # @UndefinedVariable

		# Upvalue and function ops

		(0x2B, 	instructions.UGET),  # @UndefinedVariable

		(0x2C, 	instructions.USETV),  # @UndefinedVariable
		(0x2D, 	instructions.USETS),  # @UndefinedVariable
		(0x2E, 	instructions.USETN),  # @UndefinedVariable
		(0x2F, 	instructions.USETP),  # @UndefinedVariable

		(0x30, 	instructions.UCLO),  # @UndefinedVariable

		(0x31, 	instructions.FNEW),  # @UndefinedVariable

		# Table ops

		(0x32, 	instructions.TNEW),  # @UndefinedVariable

		(0x33, 	instructions.TDUP),  # @UndefinedVariable

		(0x34, 	instructions.GGET),  # @UndefinedVariable
		(0x35, 	instructions.GSET),  # @UndefinedVariable

		(0x36, 	instructions.TGETV),  # @UndefinedVariable
		(0x37, 	instructions.TGETS),  # @UndefinedVariable
		(0x38, 	instructions.TGETB),  # @UndefinedVariable
		(0x38, 	instructions.TGETR),  # @UndefinedVariable

		(0x39, 	instructions.TSETV),  # @UndefinedVariable
		(0x3A, 	instructions.TSETS),  # @UndefinedVariable
		(0x3B, 	instructions.TSETB),  # @UndefinedVariable

		(0x3C, 	instructions.TSETM),  # @UndefinedVariable
		(0x3B, 	instructions.TSETR),  # @UndefinedVariable

		# Calls and vararg handling

		(0x3D, 	instructions.CALLM),  # @UndefinedVariable
		(0x3E, 	instructions.CALL),  # @UndefinedVariable
		(0x3F, 	instructions.CALLMT),  # @UndefinedVariable
		(0x40, 	instructions.CALLT),  # @UndefinedVariable

		(0x41, 	instructions.ITERC),  # @UndefinedVariable
		(0x42, 	instructions.ITERN),  # @UndefinedVariable

		(0x43, 	instructions.VARG),  # @UndefinedVariable

		(0x44, 	instructions.ISNEXT),  # @UndefinedVariable

		# Returns

		(0x45, 	instructions.RETM),  # @UndefinedVariable
		(0x46, 	instructions.RET),  # @UndefinedVariable
		(0x47, 	instructions.RET0),  # @UndefinedVariable
		(0x48, 	instructions.RET1),  # @UndefinedVariable

		# Loops and branches

		(0x49, 	instructions.FORI),  # @UndefinedVariable
		(0x4A, 	instructions.JFORI),  # @UndefinedVariable

		(0x4B, 	instructions.FORL),  # @UndefinedVariable
		(0x4C, 	instructions.IFORL),  # @UndefinedVariable
		(0x4D, 	instructions.JFORL),  # @UndefinedVariable

		(0x4E, 	instructions.ITERL),  # @UndefinedVariable
		(0x4F, 	instructions.IITERL),  # @UndefinedVariable
		(0x50, 	instructions.JITERL),  # @UndefinedVariable

		(0x51, 	instructions.LOOP),  # @UndefinedVariable
		(0x52, 	instructions.ILOOP),  # @UndefinedVariable
		(0x53, 	instructions.JLOOP),  # @UndefinedVariable

		(0x54, 	instructions.JMP),  # @UndefinedVariable

		# Function headers

		(0x55, 	instructions.FUNCF),  # @UndefinedVariable
		(0x56, 	instructions.IFUNCF),  # @UndefinedVariable
		(0x57, 	instructions.JFUNCF),  # @UndefinedVariable

		(0x58, 	instructions.FUNCV),  # @UndefinedVariable
		(0x59, 	instructions.IFUNCV),  # @UndefinedVariable
		(0x5A, 	instructions.JFUNCV),  # @UndefinedVariable

		(0x5B, 	instructions.FUNCC),  # @UndefinedVariable
		(0x5C, 	instructions.FUNCCW)  # @UndefinedVariable
	)


_MAP = [None] * 256


def read(parser):
	global _MAP

	codeword = parser.stream.read_uint(4)

	opcode = codeword & 0xFF

	instruction_class = _MAP[opcode]

	if instruction_class is None:
		errprint("Warning: unknown opcode {0:08x}", opcode)
		instruction_class = instructions.UNKNW  # @UndefinedVariable #zzw.20180714

	instruction = instruction_class()

	if instruction_class.opcode != opcode:
		instruction.opcode = opcode

	_set_instruction_operands(parser, codeword, instruction)

	return instruction


def _set_instruction_operands(parser, codeword, instruction):
	if instruction.args_count == 3:
		A = (codeword >> 8) & 0xFF
		CD = (codeword >> 16) & 0xFF
		B = (codeword >> 24) & 0xFF
	else:
		A = (codeword >> 8) & 0xFF
		CD = (codeword >> 16) & 0xFFFF

	if instruction.A_type is not None:
		instruction.A = _process_operand(parser, instruction.A_type, A)

	if instruction.B_type is not None:
		instruction.B = _process_operand(parser, instruction.B_type, B)

	if instruction.CD_type is not None:
		instruction.CD = _process_operand(parser, instruction.CD_type, CD)


def _process_operand(parser, operand_type, operand):
	if operand_type == instructions.T_STR			\
			or operand_type == instructions.T_TAB	\
			or operand_type == instructions.T_FUN	\
			or operand_type == instructions.T_CDT:
		return parser.complex_constants_count - operand - 1
	elif operand_type == instructions.T_JMP:
		return operand - 0x8000
	else:
		return operand


def _init():
	global _OPCODES, _MAP
	opcode = 0
	for instruction in _OPCODES:
		_MAP[opcode] = instruction[1]
		opcode = opcode + 1

	del globals()["_init"]
	del globals()["_OPCODES"]

_init()
