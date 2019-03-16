from kafka import KafkaConsumer
from kafka import KafkaProducer

consumer = KafkaConsumer('python_test',
                         group_id='python',
                         bootstrap_servers=['127.0.0.1:9092'],
                         value_deserializer=lambda m: m.decode('utf-8'))
for msg in consumer:
    print(msg.value)
