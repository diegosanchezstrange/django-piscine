#!/bin/bash

curl -sI bit.ly/1O72s3U | grep 'Location' | cut -d ' ' -f2
