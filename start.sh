#!/bin/bash

echo "Starting Flask Multi-Page Application..."
echo "========================================"

# Start ngrok in the background
echo "Starting ngrok on port 5000..."
pyngrok http 5000 > /dev/null 2>&1 &
NGROK_PID=$!

# Wait for ngrok to initialize
sleep 2

# Get the ngrok public URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o '"public_url":"https://[^"]*' | head -1 | cut -d'"' -f4)

if [ -z "$NGROK_URL" ]; then
    echo "Warning: Could not retrieve ngrok URL"
    echo "You can check manually at: http://localhost:4040"
else
    echo ""
    echo "╔════════════════════════════════════════════════════════╗"
    echo "║  🌐 ngrok Public URL:                                 ║"
    echo "║  $NGROK_URL"
    echo "╚════════════════════════════════════════════════════════╝"
    echo ""
fi

echo "Local URL: http://localhost:5000"
echo "ngrok Inspector: http://localhost:4040"
echo "========================================"
echo ""

# Start Flask app
python app.py

# Cleanup ngrok on exit
kill $NGROK_PID 2>/dev/null