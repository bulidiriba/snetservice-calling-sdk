# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import face_common_pb2 as face__common__pb2


class FaceDetectStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FindFace = channel.unary_unary(
        '/FaceDetect/FindFace',
        request_serializer=face__common__pb2.ImageRGB.SerializeToString,
        response_deserializer=face__common__pb2.FaceDetections.FromString,
        )


class FaceDetectServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FindFace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FaceDetectServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FindFace': grpc.unary_unary_rpc_method_handler(
          servicer.FindFace,
          request_deserializer=face__common__pb2.ImageRGB.FromString,
          response_serializer=face__common__pb2.FaceDetections.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'FaceDetect', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
