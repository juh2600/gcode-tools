# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gcode.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'gcode.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgcode.proto\x12\tqsp.gcode\x1a\x1bgoogle/protobuf/empty.proto\"\x88\x01\n\x0eSingleArgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.qsp.gcode.ArgType\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\x12\"\n\x07\x66lavors\x18\x05 \x03(\x0e\x32\x11.qsp.gcode.Vendor\";\n\rMutexArgument\x12*\n\x07\x63hoices\x18\x01 \x03(\x0b\x32\x19.qsp.gcode.SingleArgument\"\x7f\n\x08\x41rgument\x12\x11\n\tmandatory\x18\x01 \x01(\x08\x12)\n\x04solo\x18\x02 \x01(\x0b\x32\x19.qsp.gcode.SingleArgumentH\x00\x12)\n\x05mutex\x18\x03 \x01(\x0b\x32\x18.qsp.gcode.MutexArgumentH\x00\x42\n\n\x08\x61rgument\"\xa5\x01\n\x07\x43ommand\x12!\n\x06letter\x18\x01 \x01(\x0e\x32\x11.qsp.gcode.Letter\x12\x0e\n\x06number\x18\x02 \x01(\t\x12!\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x13.qsp.gcode.Argument\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\"\n\x07\x66lavors\x18\x06 \x03(\x0e\x32\x11.qsp.gcode.Vendor\"\x1a\n\x07\x43omment\x12\x0f\n\x07\x63omment\x18\x01 \x01(\t\"\x13\n\x04Line\x12\x0b\n\x03raw\x18\x01 \x01(\t\"v\n\x05\x42lock\x12\x1e\n\x03raw\x18\x01 \x01(\x0b\x32\x0f.qsp.gcode.LineH\x00\x12!\n\x03\x63md\x18\x02 \x01(\x0b\x32\x12.qsp.gcode.CommandH\x00\x12!\n\x03\x63mt\x18\x03 \x01(\x0b\x32\x12.qsp.gcode.CommentH\x00\x42\x07\n\x05\x62lock\"+\n\x07Program\x12 \n\x06\x62locks\x18\x01 \x03(\x0b\x32\x10.qsp.gcode.Block*5\n\x06Letter\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x05\n\x01G\x10\x01\x12\x05\n\x01M\x10\x02\x12\x05\n\x01T\x10\x03\x12\x05\n\x01\x44\x10\x04*[\n\x07\x41rgType\x12\x07\n\x03\x41NY\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\t\n\x05\x46LOAT\x10\x04\x12\r\n\tFILE_PATH\x10\x05\x12\x08\n\x04\x46LAG\x10\x06*?\n\x06Vendor\x12\n\n\x06\x43OMMON\x10\x00\x12\x08\n\x04GRBL\x10\x01\x12\t\n\x05\x46\x41NUC\x10\x02\x12\x08\n\x04HAAS\x10\x03\x12\n\n\x06MARLIN\x10\x04\x32l\n\x0bGcodeParser\x12/\n\x08toString\x12\x10.qsp.gcode.Block\x1a\x0f.qsp.gcode.Line\"\x00\x12,\n\x05parse\x12\x0f.qsp.gcode.Line\x1a\x10.qsp.gcode.Block\"\x00\x32\xb5\x01\n\nCNCMachine\x12\x33\n\x03run\x12\x10.qsp.gcode.Block\x1a\x16.google.protobuf.Empty\"\x00(\x01\x12\x35\n\x07run_one\x12\x10.qsp.gcode.Block\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x0brun_program\x12\x12.qsp.gcode.Program\x1a\x16.google.protobuf.Empty\"\x00\x32\x82\x01\n\x0fGcodeDictionary\x12;\n\tenumerate\x12\x16.google.protobuf.Empty\x1a\x12.qsp.gcode.Command\"\x00\x30\x01\x12\x32\n\x08\x64\x65scribe\x12\x10.qsp.gcode.Block\x1a\x12.qsp.gcode.Command\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcode_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LETTER']._serialized_start=766
  _globals['_LETTER']._serialized_end=819
  _globals['_ARGTYPE']._serialized_start=821
  _globals['_ARGTYPE']._serialized_end=912
  _globals['_VENDOR']._serialized_start=914
  _globals['_VENDOR']._serialized_end=977
  _globals['_SINGLEARGUMENT']._serialized_start=56
  _globals['_SINGLEARGUMENT']._serialized_end=192
  _globals['_MUTEXARGUMENT']._serialized_start=194
  _globals['_MUTEXARGUMENT']._serialized_end=253
  _globals['_ARGUMENT']._serialized_start=255
  _globals['_ARGUMENT']._serialized_end=382
  _globals['_COMMAND']._serialized_start=385
  _globals['_COMMAND']._serialized_end=550
  _globals['_COMMENT']._serialized_start=552
  _globals['_COMMENT']._serialized_end=578
  _globals['_LINE']._serialized_start=580
  _globals['_LINE']._serialized_end=599
  _globals['_BLOCK']._serialized_start=601
  _globals['_BLOCK']._serialized_end=719
  _globals['_PROGRAM']._serialized_start=721
  _globals['_PROGRAM']._serialized_end=764
  _globals['_GCODEPARSER']._serialized_start=979
  _globals['_GCODEPARSER']._serialized_end=1087
  _globals['_CNCMACHINE']._serialized_start=1090
  _globals['_CNCMACHINE']._serialized_end=1271
  _globals['_GCODEDICTIONARY']._serialized_start=1274
  _globals['_GCODEDICTIONARY']._serialized_end=1404
# @@protoc_insertion_point(module_scope)
