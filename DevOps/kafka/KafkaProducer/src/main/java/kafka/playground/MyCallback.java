package kafka.playground;

import org.apache.kafka.clients.producer.RecordMetadata;

public class MyCallback implements org.apache.kafka.clients.producer.Callback {
    @Override
    public void onCompletion(RecordMetadata recordMetadata, Exception e) {
        if(e != null) {
            e.printStackTrace();
        }
        System.out.println(recordMetadata.offset());
        System.out.println(recordMetadata.partition());
        System.out.println("Completed");
    }
}
