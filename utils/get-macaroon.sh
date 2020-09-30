#!/bin/bash

curl -X POST -H 'Content-type: application/x-www-form-urlencoded' \
  --cacert ~/.globus/usercert.pem \
  --capath /etc/grid-security/certificates/ \
  --cert /tmp/x509up_u501 \
  --key /tmp/x509up_u501 https://storm.example:8443/oauth/token \
  -d grant_type=client_credentials | jq -r .access_token
