#!/bin/bash

# Deployment script for AV Navigation IP Protection Website
# Usage: ./deploy.sh [staging|production]

set -e

TARGET=${1:-staging}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="$SCRIPT_DIR/build"

echo "🚀 Starting deployment process for $TARGET environment..."

# Check if build directory exists
if [ ! -d "$BUILD_DIR" ]; then
    echo "❌ Build directory not found. Running site generation first..."
    python "$SCRIPT_DIR/generate_site.py"
fi

# Validate build directory contents
REQUIRED_FILES=("index.html" "patent-details.html" "licensing.html" "contact.html" "sitemap.xml" "robots.txt")
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$BUILD_DIR/$file" ]; then
        echo "❌ Required file missing: $file"
        echo "🔧 Regenerating site..."
        python "$SCRIPT_DIR/generate_site.py"
        break
    fi
done

# TODO: Configure these variables for your hosting setup
if [ "$TARGET" = "staging" ]; then
    REMOTE_HOST="staging.av-navigation-ip.com"
    REMOTE_PATH="/var/www/staging/"
    REMOTE_USER="deploy"
elif [ "$TARGET" = "production" ]; then
    REMOTE_HOST="av-navigation-ip.com"
    REMOTE_PATH="/var/www/html/"
    REMOTE_USER="deploy"
else
    echo "❌ Invalid target environment. Use 'staging' or 'production'"
    exit 1
fi

echo "📋 Deployment Configuration:"
echo "  Target: $TARGET"
echo "  Host: $REMOTE_HOST"
echo "  Path: $REMOTE_PATH"
echo "  User: $REMOTE_USER"
echo "  Build Dir: $BUILD_DIR"

# Uncomment and configure when ready for actual deployment
echo ""
echo "🔧 To enable deployment, configure the following:"
echo "1. Set up SSH key authentication for $REMOTE_USER@$REMOTE_HOST"
echo "2. Ensure $REMOTE_PATH exists and is writable"
echo "3. Uncomment the rsync command below"
echo ""

# rsync -avz --delete "$BUILD_DIR/" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"

echo "📝 Manual deployment command:"
echo "rsync -avz --delete $BUILD_DIR/ $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"

echo ""
echo "✅ Deployment script ready. Configure hosting details and uncomment rsync command to enable."
echo "📄 Site ready for deployment from: $BUILD_DIR"