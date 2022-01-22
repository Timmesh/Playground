package org.timmesh.programs;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.timmesh.config.AppConfig1;
import org.timmesh.dao.ProductDao;

public class P01_GetProductCount {

	public static void main(String[] args) {
		// our dependency
		ProductDao dao;
		
		// a variable representing the spring container
		AnnotationConfigApplicationContext ctx;
		
		// object of spring container
		ctx = new AnnotationConfigApplicationContext(AppConfig1.class);
		
		System.out.println("------------------");
		dao = ctx.getBean("dummyDao", ProductDao.class);
		ProductDao dao2 = ctx.getBean("jdbcDao", ProductDao.class);
		System.out.println("dao is an instanceof " + dao.getClass().getName());
		System.out.println("There are " + dao.count() + " products.");
		
		System.out.println("dao is an instanceof " + dao2.getClass().getName());
		System.out.println("There are " + dao2.count() + " products.");
		
		ctx.close();
	}

}
