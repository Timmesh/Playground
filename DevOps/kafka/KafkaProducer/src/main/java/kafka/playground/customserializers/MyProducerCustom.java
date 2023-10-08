package kafka.playground.customserializers;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

import java.util.Properties;

public class MyProducerCustom {

    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, OrderSerializer.class.getName());
        try (KafkaProducer<String, Order> kafkaProducer = new KafkaProducer<>(properties)) {
            Order order = new Order();
            order.setCustomerName("Nak");
            order.setProduct("Mac Book");
            order.setQuantity(5);
            ProducerRecord<String, Order> record = new ProducerRecord<>("my-custom-topic", order.getCustomerName(), order);
            kafkaProducer.send(record);
            System.out.println("Completed");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
