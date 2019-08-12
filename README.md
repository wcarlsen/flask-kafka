# Flask and Kafka consumer background service
A small project to learn about background threads and Kafka.

```bash
# Install
cd server/
pipenv install

# Run
docker-compose up --build
pipenv run flask db upgrade
pipenv run start

# Install Kafka (arch: sudo pacman -S kafka) to produce messages
kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

Unfortunately Flask doesn't support websockets out of the box (maybe flask-sockerio will work), but it could have been fun to show the messages posted in a frontend using websockets to publish events messages from a Kafka topic.