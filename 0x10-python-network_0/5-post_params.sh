#!/bin/bash
# A variable email and A variable subject must be sent
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
