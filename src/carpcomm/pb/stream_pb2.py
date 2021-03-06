# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import carpcomm.pb.telemetry_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='carpcomm/pb/stream.proto',
  package='pb',
  serialized_pb='\n\x18\x63\x61rpcomm/pb/stream.proto\x12\x02pb\x1a\x1b\x63\x61rpcomm/pb/telemetry.proto\"l\n\x08IQParams\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x05\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.pb.IQParams.Type\"*\n\x04Type\x12\t\n\x05UINT8\x10\x01\x12\n\n\x06SINT16\x10\x02\x12\x0b\n\x07\x46LOAT32\x10\x03\"\xa7\x03\n\x07\x43ontact\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0csatellite_id\x18\t \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x06 \x01(\x03\x12\x15\n\rend_timestamp\x18\x08 \x01(\x03\x12\x1e\n\x04\x62lob\x18\n \x03(\x0b\x32\x10.pb.Contact.Blob\x12\x12\n\nstation_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x07 \x01(\t\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x0b\n\x03lng\x18\x04 \x01(\x01\x12\x11\n\televation\x18\x05 \x01(\x01\x1a\xd7\x01\n\x04\x42lob\x12\'\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x17.pb.Contact.Blob.Format\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x13\n\x0binline_data\x18\x03 \x01(\x0c\x12!\n\x05\x64\x61tum\x18\x04 \x01(\x0b\x32\x12.pb.TelemetryDatum\x12\x1f\n\tiq_params\x18\x05 \x01(\x0b\x32\x0c.pb.IQParams\"?\n\x06\x46ormat\x12\x06\n\x02IQ\x10\x01\x12\t\n\x05MORSE\x10\x02\x12\t\n\x05\x46RAME\x10\x03\x12\t\n\x05\x44\x41TUM\x10\x04\x12\x0c\n\x08\x46REEFORM\x10\x05')



_IQPARAMS_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='pb.IQParams.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='UINT8', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SINT16', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FLOAT32', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=127,
  serialized_end=169,
)

_CONTACT_BLOB_FORMAT = descriptor.EnumDescriptor(
  name='Format',
  full_name='pb.Contact.Blob.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='IQ', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MORSE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FRAME', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DATUM', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FREEFORM', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=532,
  serialized_end=595,
)


_IQPARAMS = descriptor.Descriptor(
  name='IQParams',
  full_name='pb.IQParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sample_rate', full_name='pb.IQParams.sample_rate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='pb.IQParams.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IQPARAMS_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=61,
  serialized_end=169,
)


_CONTACT_BLOB = descriptor.Descriptor(
  name='Blob',
  full_name='pb.Contact.Blob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='format', full_name='pb.Contact.Blob.format', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='path', full_name='pb.Contact.Blob.path', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inline_data', full_name='pb.Contact.Blob.inline_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='datum', full_name='pb.Contact.Blob.datum', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='iq_params', full_name='pb.Contact.Blob.iq_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTACT_BLOB_FORMAT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=380,
  serialized_end=595,
)

_CONTACT = descriptor.Descriptor(
  name='Contact',
  full_name='pb.Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='pb.Contact.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='satellite_id', full_name='pb.Contact.satellite_id', index=1,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_timestamp', full_name='pb.Contact.start_timestamp', index=2,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_timestamp', full_name='pb.Contact.end_timestamp', index=3,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='blob', full_name='pb.Contact.blob', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='station_id', full_name='pb.Contact.station_id', index=5,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_id', full_name='pb.Contact.user_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lat', full_name='pb.Contact.lat', index=7,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lng', full_name='pb.Contact.lng', index=8,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='elevation', full_name='pb.Contact.elevation', index=9,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTACT_BLOB, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=172,
  serialized_end=595,
)

_IQPARAMS.fields_by_name['type'].enum_type = _IQPARAMS_TYPE
_IQPARAMS_TYPE.containing_type = _IQPARAMS;
_CONTACT_BLOB.fields_by_name['format'].enum_type = _CONTACT_BLOB_FORMAT
_CONTACT_BLOB.fields_by_name['datum'].message_type = carpcomm.pb.telemetry_pb2._TELEMETRYDATUM
_CONTACT_BLOB.fields_by_name['iq_params'].message_type = _IQPARAMS
_CONTACT_BLOB.containing_type = _CONTACT;
_CONTACT_BLOB_FORMAT.containing_type = _CONTACT_BLOB;
_CONTACT.fields_by_name['blob'].message_type = _CONTACT_BLOB
DESCRIPTOR.message_types_by_name['IQParams'] = _IQPARAMS
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT

class IQParams(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IQPARAMS
  
  # @@protoc_insertion_point(class_scope:pb.IQParams)

class Contact(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Blob(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTACT_BLOB
    
    # @@protoc_insertion_point(class_scope:pb.Contact.Blob)
  DESCRIPTOR = _CONTACT
  
  # @@protoc_insertion_point(class_scope:pb.Contact)

# @@protoc_insertion_point(module_scope)
