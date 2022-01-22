package org.timmesh.programs;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.timmesh.config.AppConfig2;
import org.timmesh.dao.ProductDao;

public class P01_GetProductCount {

	public static void main(String[] args) {
		// a variable representing the spring container
		AnnotationConfigApplicationContext ctx;
		
		// object of spring container
		ctx = new AnnotationConfigApplicationContext(AppConfig2.class);
		System.out.println("---------");
		ProductDao jdbcDao = ctx.getBean("jdbcDao", ProductDao.class);
		
		System.out.println("dao is an instanceof " + jdbcDao.getClass().getName());
		System.out.println("There are " + jdbcDao.count() + " products.");
		
		ctx.close();
	}

}
