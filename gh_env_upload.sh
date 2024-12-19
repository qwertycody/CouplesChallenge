#!/bin/bash

# Script to upload .pr.env file to GitHub Actions Secrets
# Requires GitHub CLI (gh) to be installed and authenticated.

# GitHub repository details
REPO_OWNER="qwertycody"
REPO_NAME="CouplesChallenge"
SECRET_NAME="ENV_FILE"

# Path to .pr.env file
ENV_FILE_PATH=".pr.env"

# Check if .env file exists
if [[ ! -f "$ENV_FILE_PATH" ]]; then
    echo "Error: .pr.env file not found at $ENV_FILE_PATH"
    exit 1
fi

# Combine .pr.env file contents into a single string
ENV_CONTENTS=$(cat "$ENV_FILE_PATH")

# Upload the .pr.env file content to GitHub Actions Secrets
echo "Uploading .pr.env file to GitHub Secrets..."
gh secret set "$SECRET_NAME" \
    --repo "$REPO_OWNER/$REPO_NAME" \
    --body "$ENV_CONTENTS"

# Confirm success
if [[ $? -eq 0 ]]; then
    echo "✅ Successfully uploaded .pr.env file to GitHub Secrets as $SECRET_NAME"
else
    echo "❌ Failed to upload .pr.env file to GitHub Secrets."
    exit 1
fi
