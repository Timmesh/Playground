package com.playground.entities;

import java.math.BigDecimal;

public class Invoice {

	String invoiceNo;
	BigDecimal price;
	BigDecimal qty;

	public String getInvoiceNo() {
		return invoiceNo;
	}

	public void setInvoiceNo(String invoiceNo) {
		this.invoiceNo = invoiceNo;
	}

	public BigDecimal getPrice() {
		return price;
	}

	public void setPrice(BigDecimal price) {
		this.price = price;
	}

	public BigDecimal getQty() {
		return qty;
	}

	public void setQty(BigDecimal qty) {
		this.qty = qty;
	}

	public Invoice(String invoiceNo, BigDecimal price, BigDecimal qty) {
		super();
		this.invoiceNo = invoiceNo;
		this.price = price;
		this.qty = qty;
	}

	// getters, stters n constructor
}