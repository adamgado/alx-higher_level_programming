#!/bin/bash
# sends a JSON POST request to a URL
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
