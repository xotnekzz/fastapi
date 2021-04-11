docker stop fastapi; docker rm fastapi

docker build -t fastapi .

docker run -i -t -d -p 80:80 --name fastapi fastapi