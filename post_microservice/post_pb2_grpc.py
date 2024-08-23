# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import post_pb2 as post__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in post_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PostServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/PostService/CreatePost',
                request_serializer=post__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=post__pb2.CreatePostResponse.FromString,
                _registered_method=True)
        self.ReadPost = channel.unary_unary(
                '/PostService/ReadPost',
                request_serializer=post__pb2.ReadPostRequest.SerializeToString,
                response_deserializer=post__pb2.ReadPostResponse.FromString,
                _registered_method=True)
        self.GetPosts = channel.unary_unary(
                '/PostService/GetPosts',
                request_serializer=post__pb2.GetPostsRequest.SerializeToString,
                response_deserializer=post__pb2.GetPostsResponse.FromString,
                _registered_method=True)


class PostServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=post__pb2.CreatePostRequest.FromString,
                    response_serializer=post__pb2.CreatePostResponse.SerializeToString,
            ),
            'ReadPost': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadPost,
                    request_deserializer=post__pb2.ReadPostRequest.FromString,
                    response_serializer=post__pb2.ReadPostResponse.SerializeToString,
            ),
            'GetPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPosts,
                    request_deserializer=post__pb2.GetPostsRequest.FromString,
                    response_serializer=post__pb2.GetPostsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('PostService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PostService/CreatePost',
            post__pb2.CreatePostRequest.SerializeToString,
            post__pb2.CreatePostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PostService/ReadPost',
            post__pb2.ReadPostRequest.SerializeToString,
            post__pb2.ReadPostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PostService/GetPosts',
            post__pb2.GetPostsRequest.SerializeToString,
            post__pb2.GetPostsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ProfileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProfile = channel.unary_unary(
                '/ProfileService/GetProfile',
                request_serializer=post__pb2.GetProfileRequest.SerializeToString,
                response_deserializer=post__pb2.GetProfileResponse.FromString,
                _registered_method=True)


class ProfileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProfile,
                    request_deserializer=post__pb2.GetProfileRequest.FromString,
                    response_serializer=post__pb2.GetProfileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ProfileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProfileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProfileService/GetProfile',
            post__pb2.GetProfileRequest.SerializeToString,
            post__pb2.GetProfileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
