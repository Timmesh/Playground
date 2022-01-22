package org.timmesh.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Lazy;
import org.springframework.context.annotation.Scope;
import org.timmesh.dao.DummyProductDao;
import org.timmesh.dao.JdbcProductDao;

@Configuration
public class AppConfig1 {

	@Lazy
	@Bean
	public DummyProductDao dummyDao() {
		System.out.println("AppConfig1.dummyDao() called");
		return new DummyProductDao();
	}

	@Scope("singleton")
	@Bean
	public JdbcProductDao jdbcDao() {
		System.out.println("AppConfig1.jdbcDao() called");
		JdbcProductDao dao = new JdbcProductDao();
		dao.setDriverClassName("org.h2.Driver");
		dao.setUrl("jdbc:h2:tcp://localhost/~/spring-training");
		dao.setUser("sa");
		dao.setPassword("");
		return dao;
	}

}
