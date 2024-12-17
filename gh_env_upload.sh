#!/bin/bash

# Script to upload .env file to GitHub Actions Secrets
# Requires GitHub CLI (gh) to be installed and authenticated.

# GitHub repository details
REPO_OWNER="qwertycody"
REPO_NAME="CouplesChallenge"
SECRET_NAME="ENV_FILE"

# Path to .env file
ENV_FILE_PATH=".env"

# Check if .env file exists
if [[ ! -f "$ENV_FILE_PATH" ]]; then
    echo "Error: .env file not found at $ENV_FILE_PATH"
    exit 1
fi

# Combine .env file contents into a single string
ENV_CONTENTS=$(cat "$ENV_FILE_PATH")

# Upload the .env file content to GitHub Actions Secrets
echo "Uploading .env file to GitHub Secrets..."
gh secret set "$SECRET_NAME" \
    --repo "$REPO_OWNER/$REPO_NAME" \
    --body "$ENV_CONTENTS"

# Confirm success
if [[ $? -eq 0 ]]; then
    echo "✅ Successfully uploaded .env file to GitHub Secrets as $SECRET_NAME"
else
    echo "❌ Failed to upload .env file to GitHub Secrets."
    exit 1
fi
