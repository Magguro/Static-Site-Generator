echo "Starting Static Site Generator..."
echo $(python3 --version)
python3 src/main.py
cd docs && python3 -m http.server 8888
