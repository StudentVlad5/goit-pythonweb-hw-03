docker build -t my-web-app .
MSYS_NO_PATHCONV=1 docker run -p 3000:3000 -v "$(pwd)/storage:/app/storage" my-web-app
