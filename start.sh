#!/bin/bash
# Start the BODS Validator application
# Backend on port 8000, Frontend on port 5173

echo "Starting BODS Validator..."

# Start backend
cd "$(dirname "$0")/backend"
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
echo "Backend started (PID $BACKEND_PID) on http://localhost:8000"

# Start frontend
cd "$(dirname "$0")/frontend"
npm run dev &
FRONTEND_PID=$!
echo "Frontend started (PID $FRONTEND_PID) on http://localhost:5173"

echo ""
echo "BODS Validator is running!"
echo "  Open http://localhost:5173 in your browser"
echo "  Press Ctrl+C to stop"

trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null" EXIT
wait
