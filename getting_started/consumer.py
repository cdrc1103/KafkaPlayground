from confluent_kafka import Consumer

conf = {'bootstrap.servers': "broker:29092",
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)
