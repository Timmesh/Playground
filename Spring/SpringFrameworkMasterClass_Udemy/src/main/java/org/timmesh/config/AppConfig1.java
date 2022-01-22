package org.timmesh.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;
import org.timmesh.dao.DummyProductDao;
import org.timmesh.dao.JdbcProductDao;

@Configuration
public class AppConfig1 {

	@Bean
	public DummyProductDao dummyDao() {
		System.out.println("AppConfig1.dummyDao() called");
		return new DummyProductDao();
	}

	@Scope("prototype")
	@Bean
	public JdbcProductDao jdbcDao() {
		System.out.println("AppConfig1.jdbcDao() called");
		return new JdbcProductDao();
	}

}
