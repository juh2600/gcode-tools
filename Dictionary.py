#!/usr/bin/env python

from concurrent import futures

import grpc
from gcode_pb2_grpc import GcodeDictionaryServicer as IGcodeDictionary, add_GcodeDictionaryServicer_to_server as addGcodeDictionaryService

from entries import entries

print(entries)