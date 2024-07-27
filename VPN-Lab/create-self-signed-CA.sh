#!/bin/bash

# Step 1: Generate a private key for the CA
openssl genpkey -algorithm RSA -out ca-key.pem -aes256 
# Step 2: Create a self-signed root certificate
openssl req -x509 -new -nodes -key ca-key.pem -sha256 -days 3650 -out ca-cert.pem   \
-subj "/C=CN/ST=Beijing/L=Beijing/O=Tsinghua Univeristy/OU=Network Security/CN=CA for VPN"

echo "CA private key and certificate have been created."

