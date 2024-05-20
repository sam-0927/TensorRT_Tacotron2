# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/collector/metrics/v1/metrics_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.metrics.v1 import metrics_pb2 as opentelemetry_dot_proto_dot_metrics_dot_v1_dot_metrics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>opentelemetry/proto/collector/metrics/v1/metrics_service.proto\x12(opentelemetry.proto.collector.metrics.v1\x1a,opentelemetry/proto/metrics/v1/metrics.proto\"h\n\x1b\x45xportMetricsServiceRequest\x12I\n\x10resource_metrics\x18\x01 \x03(\x0b\x32/.opentelemetry.proto.metrics.v1.ResourceMetrics\"~\n\x1c\x45xportMetricsServiceResponse\x12^\n\x0fpartial_success\x18\x01 \x01(\x0b\x32\x45.opentelemetry.proto.collector.metrics.v1.ExportMetricsPartialSuccess\"R\n\x1b\x45xportMetricsPartialSuccess\x12\x1c\n\x14rejected_data_points\x18\x01 \x01(\x03\x12\x15\n\rerror_message\x18\x02 \x01(\t2\xac\x01\n\x0eMetricsService\x12\x99\x01\n\x06\x45xport\x12\x45.opentelemetry.proto.collector.metrics.v1.ExportMetricsServiceRequest\x1a\x46.opentelemetry.proto.collector.metrics.v1.ExportMetricsServiceResponse\"\x00\x42\xa4\x01\n+io.opentelemetry.proto.collector.metrics.v1B\x13MetricsServiceProtoP\x01Z3go.opentelemetry.io/proto/otlp/collector/metrics/v1\xaa\x02(OpenTelemetry.Proto.Collector.Metrics.V1b\x06proto3')



_EXPORTMETRICSSERVICEREQUEST = DESCRIPTOR.message_types_by_name['ExportMetricsServiceRequest']
_EXPORTMETRICSSERVICERESPONSE = DESCRIPTOR.message_types_by_name['ExportMetricsServiceResponse']
_EXPORTMETRICSPARTIALSUCCESS = DESCRIPTOR.message_types_by_name['ExportMetricsPartialSuccess']
ExportMetricsServiceRequest = _reflection.GeneratedProtocolMessageType('ExportMetricsServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTMETRICSSERVICEREQUEST,
  '__module__' : 'opentelemetry.proto.collector.metrics.v1.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.collector.metrics.v1.ExportMetricsServiceRequest)
  })
_sym_db.RegisterMessage(ExportMetricsServiceRequest)

ExportMetricsServiceResponse = _reflection.GeneratedProtocolMessageType('ExportMetricsServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTMETRICSSERVICERESPONSE,
  '__module__' : 'opentelemetry.proto.collector.metrics.v1.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.collector.metrics.v1.ExportMetricsServiceResponse)
  })
_sym_db.RegisterMessage(ExportMetricsServiceResponse)

ExportMetricsPartialSuccess = _reflection.GeneratedProtocolMessageType('ExportMetricsPartialSuccess', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTMETRICSPARTIALSUCCESS,
  '__module__' : 'opentelemetry.proto.collector.metrics.v1.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.collector.metrics.v1.ExportMetricsPartialSuccess)
  })
_sym_db.RegisterMessage(ExportMetricsPartialSuccess)

_METRICSSERVICE = DESCRIPTOR.services_by_name['MetricsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n+io.opentelemetry.proto.collector.metrics.v1B\023MetricsServiceProtoP\001Z3go.opentelemetry.io/proto/otlp/collector/metrics/v1\252\002(OpenTelemetry.Proto.Collector.Metrics.V1'
  _EXPORTMETRICSSERVICEREQUEST._serialized_start=154
  _EXPORTMETRICSSERVICEREQUEST._serialized_end=258
  _EXPORTMETRICSSERVICERESPONSE._serialized_start=260
  _EXPORTMETRICSSERVICERESPONSE._serialized_end=386
  _EXPORTMETRICSPARTIALSUCCESS._serialized_start=388
  _EXPORTMETRICSPARTIALSUCCESS._serialized_end=470
  _METRICSSERVICE._serialized_start=473
  _METRICSSERVICE._serialized_end=645
# @@protoc_insertion_point(module_scope)
