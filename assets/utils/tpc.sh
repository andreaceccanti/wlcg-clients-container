#!/bin/bash
set -e

src=$1
dst=$2

echo "TPC pull: ${src} -> ${dst}"

curl -X COPY --capath /etc/grid-security/certificates/ -H "Authorization: Bearer ${BEARER_TOKEN}" \
  -H "TransferHeaderAuthorization: Bearer ${BEARER_TOKEN}" \
  -H "Overwrite: T" \
  -H "Source: ${src}" \
  ${dst}
