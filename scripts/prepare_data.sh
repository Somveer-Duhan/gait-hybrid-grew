#!/usr/bin/env bash
set -e

ZIP_FILE=""

if [ -z "" ]; then
  echo "Usage: ./prepare_data.sh <path_to_train.zip>"
  exit 1
fi

echo "Unzipping GREW dataset..."
unzip -P 8ahK3gHi07Dg ""

echo "Extracting train.tgz..."
tar -xzvf train.tgz

cd train

echo "Extracting all .tgz segments..."
ls *.tgz | xargs -n1 tar xzvf

echo "GREW extraction complete."
