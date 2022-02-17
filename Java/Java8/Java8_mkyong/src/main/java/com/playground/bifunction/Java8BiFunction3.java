package com.playground.bifunction;

import java.util.function.BiFunction;

/**
 * @author USER
 * This example uses BiFunction to create an object, acts as a factory pattern.
 */
public class Java8BiFunction3 {

    public static void main(String[] args) {

        GPS obj = factory("40.741895", "-73.989308", GPS::new);
        System.out.println(obj);

    }

    public static <R extends GPS> R factory(String Latitude, String Longitude,
                                            BiFunction<String, String, R> func) {
        return func.apply(Latitude, Longitude);
    }

}

/**
 * @author USER
 *
 */
class GPS {

    String Latitude;
    String Longitude;

    /**
     * The GPS::new calls the following constructor, which accepts two arguments and return an object (GPS), so it matches with the BiFunction signature.
     * @param latitude
     * @param longitude
     */
    public GPS(String latitude, String longitude) {
        Latitude = latitude;
        Longitude = longitude;
    }

    public String getLatitude() {
        return Latitude;
    }

    public void setLatitude(String latitude) {
        Latitude = latitude;
    }

    public String getLongitude() {
        return Longitude;
    }

    public void setLongitude(String longitude) {
        Longitude = longitude;
    }

    @Override
    public String toString() {
        return "GPS{" +
                "Latitude='" + Latitude + '\'' +
                ", Longitude='" + Longitude + '\'' +
                '}';
    }
}
