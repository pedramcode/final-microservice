# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x94\x02\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x02\x12\x12\n\nupdated_at\x18\x04 \x01(\x02\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x11\n\tfirstname\x18\x07 \x01(\t\x12\x10\n\x08lastname\x18\x08 \x01(\t\x12\r\n\x05\x65mail\x18\t \x01(\t\x12\x0e\n\x06mobile\x18\n \x01(\t\x12\x14\n\x0cis_superuser\x18\x0b \x01(\x08\x12\x10\n\x08is_staff\x18\x0c \x01(\x08\x12\x1a\n\x12is_mobile_verified\x18\r \x01(\x08\x12\x19\n\x11is_email_verified\x18\x0e \x01(\x08\"V\n\x11UserCreateRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06mobile\x18\x04 \x01(\t\"6\n\x10UserLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x11UserLogoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"G\n\x11UserUpdateRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x11\n\tfirstname\x18\x02 \x01(\t\x12\x10\n\x08lastname\x18\x03 \x01(\t\".\n\x0fIssueOtpRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\"\x1e\n\rUserMeRequest\x12\r\n\x05token\x18\x01 \x01(\t\"0\n\x12\x45valuateOtpRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0b\n\x03otp\x18\x02 \x01(\t\"\"\n\x11UserLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\"/\n\x0fMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t2\xfe\x02\n\x07UserAPI\x12-\n\x06\x43reate\x12\x17.user.UserCreateRequest\x1a\n.user.User\x12%\n\x02Me\x12\x13.user.UserMeRequest\x1a\n.user.User\x12-\n\x06Update\x12\x17.user.UserUpdateRequest\x1a\n.user.User\x12\x38\n\x05Login\x12\x16.user.UserLoginRequest\x1a\x17.user.UserLoginResponse\x12\x38\n\x06Logout\x12\x17.user.UserLogoutRequest\x1a\x15.user.MessageResponse\x12\x39\n\tIssue_otp\x12\x15.user.IssueOtpRequest\x1a\x15.user.MessageResponse\x12?\n\x0c\x45valuate_otp\x12\x18.user.EvaluateOtpRequest\x1a\x15.user.MessageResponseb\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
_USERCREATEREQUEST = DESCRIPTOR.message_types_by_name['UserCreateRequest']
_USERLOGINREQUEST = DESCRIPTOR.message_types_by_name['UserLoginRequest']
_USERLOGOUTREQUEST = DESCRIPTOR.message_types_by_name['UserLogoutRequest']
_USERUPDATEREQUEST = DESCRIPTOR.message_types_by_name['UserUpdateRequest']
_ISSUEOTPREQUEST = DESCRIPTOR.message_types_by_name['IssueOtpRequest']
_USERMEREQUEST = DESCRIPTOR.message_types_by_name['UserMeRequest']
_EVALUATEOTPREQUEST = DESCRIPTOR.message_types_by_name['EvaluateOtpRequest']
_USERLOGINRESPONSE = DESCRIPTOR.message_types_by_name['UserLoginResponse']
_MESSAGERESPONSE = DESCRIPTOR.message_types_by_name['MessageResponse']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)

UserCreateRequest = _reflection.GeneratedProtocolMessageType('UserCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserCreateRequest)
  })
_sym_db.RegisterMessage(UserCreateRequest)

UserLoginRequest = _reflection.GeneratedProtocolMessageType('UserLoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLOGINREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserLoginRequest)
  })
_sym_db.RegisterMessage(UserLoginRequest)

UserLogoutRequest = _reflection.GeneratedProtocolMessageType('UserLogoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLOGOUTREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserLogoutRequest)
  })
_sym_db.RegisterMessage(UserLogoutRequest)

UserUpdateRequest = _reflection.GeneratedProtocolMessageType('UserUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERUPDATEREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserUpdateRequest)
  })
_sym_db.RegisterMessage(UserUpdateRequest)

IssueOtpRequest = _reflection.GeneratedProtocolMessageType('IssueOtpRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISSUEOTPREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.IssueOtpRequest)
  })
_sym_db.RegisterMessage(IssueOtpRequest)

UserMeRequest = _reflection.GeneratedProtocolMessageType('UserMeRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERMEREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserMeRequest)
  })
_sym_db.RegisterMessage(UserMeRequest)

EvaluateOtpRequest = _reflection.GeneratedProtocolMessageType('EvaluateOtpRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATEOTPREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.EvaluateOtpRequest)
  })
_sym_db.RegisterMessage(EvaluateOtpRequest)

UserLoginResponse = _reflection.GeneratedProtocolMessageType('UserLoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERLOGINRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserLoginResponse)
  })
_sym_db.RegisterMessage(UserLoginResponse)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)

_USERAPI = DESCRIPTOR.services_by_name['UserAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=21
  _USER._serialized_end=297
  _USERCREATEREQUEST._serialized_start=299
  _USERCREATEREQUEST._serialized_end=385
  _USERLOGINREQUEST._serialized_start=387
  _USERLOGINREQUEST._serialized_end=441
  _USERLOGOUTREQUEST._serialized_start=443
  _USERLOGOUTREQUEST._serialized_end=477
  _USERUPDATEREQUEST._serialized_start=479
  _USERUPDATEREQUEST._serialized_end=550
  _ISSUEOTPREQUEST._serialized_start=552
  _ISSUEOTPREQUEST._serialized_end=598
  _USERMEREQUEST._serialized_start=600
  _USERMEREQUEST._serialized_end=630
  _EVALUATEOTPREQUEST._serialized_start=632
  _EVALUATEOTPREQUEST._serialized_end=680
  _USERLOGINRESPONSE._serialized_start=682
  _USERLOGINRESPONSE._serialized_end=716
  _MESSAGERESPONSE._serialized_start=718
  _MESSAGERESPONSE._serialized_end=765
  _USERAPI._serialized_start=768
  _USERAPI._serialized_end=1150
# @@protoc_insertion_point(module_scope)