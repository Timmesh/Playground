package org.timmesh.programs;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.timmesh.config.AppConfig1;
import org.timmesh.dao.ProductDao;

public class P01_GetProductCount {

	public static void main(String[] args) {
		// a variable representing the spring container
		AnnotationConfigApplicationContext ctx;
		
		// object of spring container
		ctx = new AnnotationConfigApplicationContext(AppConfig1.class);
		
		ProductDao jdbcDao = ctx.getBean("jdbcDao", ProductDao.class);
		ProductDao jdbcDao2 = ctx.getBean("jdbcDao", ProductDao.class);
		// Singleton Scope(Default) which refers to the same object created in the spring container
		System.out.println("jdbcDao == jdbcDao2 is "+ (jdbcDao == jdbcDao2));
		
		System.out.println("dao is an instanceof " + jdbcDao.getClass().getName());
		System.out.println("There are " + jdbcDao.count() + " products.");
		System.out.println("dao is an instanceof " + jdbcDao2.getClass().getName());
		System.out.println("There are " + jdbcDao2.count() + " products.");
		
		ctx.close();
	}

}
