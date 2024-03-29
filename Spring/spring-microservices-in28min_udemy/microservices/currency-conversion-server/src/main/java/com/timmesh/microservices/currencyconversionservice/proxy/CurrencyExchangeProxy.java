package com.timmesh.microservices.currencyconversionservice.proxy;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.timmesh.microservices.currencyconversionservice.entity.CurrencyConversion;


//@FeignClient(name="currency-exchange", url="localhost:8001")
@FeignClient(name="currency-exchange")
public interface CurrencyExchangeProxy {
	
	@GetMapping("/currency-exchange/from/{from}/to/{to}")
	public CurrencyConversion retrieveExchangeValue(
			@PathVariable(value = "from") String from, @PathVariable(value = "to") String to);

}
