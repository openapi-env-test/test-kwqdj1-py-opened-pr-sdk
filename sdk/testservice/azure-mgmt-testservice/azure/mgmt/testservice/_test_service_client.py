# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import TestServiceClientConfiguration
from .operations import TestOperations
from . import models


class TestServiceClient(SDKClient):
    """Test Service Client for SDK Automation integration test.

    :ivar config: Configuration for client.
    :vartype config: TestServiceClientConfiguration

    :ivar test: Test operations
    :vartype test: azure.mgmt.testservice.operations.TestOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = TestServiceClientConfiguration(base_url)
        super(TestServiceClient, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.test = TestOperations(
            self._client, self.config, self._serialize, self._deserialize)
