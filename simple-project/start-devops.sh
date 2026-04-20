#!/bin/bash
echo "🚀 Starting DevOps Day 3 Environment..."

# Start Redis
sudo systemctl start redis-server
echo "✅ Redis started"

# Start Simple Project
cd simple-project
source venv/bin/activate
python app.py &
echo "✅ Simple Project running on http://localhost:5000"

echo ""
echo "Press Ctrl+C to stop everything"
wait
