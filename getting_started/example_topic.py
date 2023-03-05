from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({
    "bootstrap.servers": "broker:29092"
})

topic_name = "example_topic"
example_topic = NewTopic(topic_name, 1, 1)
admin_client.create_topics([example_topic])

print(admin_client.list_topics().topics)