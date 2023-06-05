#!/usr/bin/env python3

## Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
## SPDX-License-Identifier: MIT-0

from aws_cdk import core
import os

from swarm_cdk.swarm_cdk_deployment import SwarmDeployment
from swarm_cdk.swarm_cdk_infra import SwarmInfra

app = core.App()
infra = SwarmInfra(app, "swarm-infra", env={"region": "ap-northeast-1"})
deployment = SwarmDeployment(
    app,
    "swarm-deployment",
    bucket=infra.bucket,
    vpc=infra.vpc,
    env={"region": "ap-northeast-1"},
)

app.synth()
