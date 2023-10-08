package kafka.playground;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

import java.util.Properties;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class MyProducer {

    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.IntegerSerializer");
        try (KafkaProducer<String, Integer> kafkaProducer = new KafkaProducer<>(properties)) {
            ProducerRecord<String, Integer> record = new ProducerRecord<>("my-topic", "New Key", 300);
            RecordMetadata recordMetadata = kafkaProducer.send(record).get();
            System.out.println(recordMetadata.offset());
            System.out.println(recordMetadata.partition());
            System.out.println("Completed");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
