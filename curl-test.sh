#!/bin/bash
# Tests the timeline_post API endpoints.
# Creates a random timeline post, verifies it appears in the GET response,
# then deletes it using the DELETE endpoint.

set -e

BASE_URL="${BASE_URL:-http://localhost:5000}"
ENDPOINT="$BASE_URL/api/timeline_post"

RANDOM_ID=$RANDOM
NAME="TestUser$RANDOM_ID"
EMAIL="testuser$RANDOM_ID@example.com"
CONTENT="This is a random test post $RANDOM_ID"

echo "=> POST $ENDPOINT"
POST_RESPONSE=$(curl -s -X POST "$ENDPOINT" \
  -d "name=$NAME" \
  -d "email=$EMAIL" \
  -d "content=$CONTENT")
echo "$POST_RESPONSE"

POST_ID=$(echo "$POST_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo "Created timeline post with id $POST_ID"

echo
echo "=> GET $ENDPOINT"
GET_RESPONSE=$(curl -s "$ENDPOINT")

if echo "$GET_RESPONSE" | grep -q "$CONTENT"; then
    echo "SUCCESS: found post '$CONTENT' in GET response"
else
    echo "FAILURE: post '$CONTENT' not found in GET response"
    echo "$GET_RESPONSE"
    exit 1
fi

echo
echo "=> DELETE $ENDPOINT/$POST_ID"
curl -s -X DELETE "$ENDPOINT/$POST_ID"
echo

if curl -s "$ENDPOINT" | grep -q "$CONTENT"; then
    echo "FAILURE: post $POST_ID still present after delete"
    exit 1
else
    echo "SUCCESS: post $POST_ID deleted"
fi
