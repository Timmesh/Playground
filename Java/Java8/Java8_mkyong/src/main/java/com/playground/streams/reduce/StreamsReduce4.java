package com.playground.streams.reduce;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.List;

import com.playground.entities.Invoice;

/**
 * @author USER the Stream.reduce() combine elements of a stream and produces a
 *         single value.
 * 
 */
public class StreamsReduce4 {
	public static void main(String[] args) {

		List<Invoice> invoices = Arrays.asList(new Invoice("A01", BigDecimal.valueOf(9.99), BigDecimal.valueOf(1)),
				new Invoice("A02", BigDecimal.valueOf(19.99), BigDecimal.valueOf(1.5)),
				new Invoice("A03", BigDecimal.valueOf(4.99), BigDecimal.valueOf(2)));

		BigDecimal sum = invoices.stream().map(x -> x.getQty().multiply(x.getPrice())) // map
				.reduce(BigDecimal.ZERO, BigDecimal::add); // reduce

		System.out.println(sum); // 49.955
		System.out.println(sum.setScale(2, RoundingMode.HALF_UP)); // 49.96
	}
}