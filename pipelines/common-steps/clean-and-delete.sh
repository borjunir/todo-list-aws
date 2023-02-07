#!/bin/bash

set -x

aws cloudformation delete-stack --stack-name todo-list-aws-${ENVIRONMENT} --region us-east-1
