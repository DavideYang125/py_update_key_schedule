docker build -t recode:v1.0 .

docker run -d -p 6066:80 recode:v1.0