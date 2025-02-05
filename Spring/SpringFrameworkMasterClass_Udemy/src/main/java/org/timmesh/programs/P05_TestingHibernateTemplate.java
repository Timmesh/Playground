package org.timmesh.programs;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.orm.hibernate5.HibernateTemplate;
import org.timmesh.config.AppConfig4;
import org.timmesh.entity.Category;


public class P05_TestingHibernateTemplate {

	public static void main(String[] args) {
		AnnotationConfigApplicationContext ctx;
		ctx = new AnnotationConfigApplicationContext(AppConfig4.class);

		HibernateTemplate ht = ctx.getBean(HibernateTemplate.class);
		Category c1 = ht.get(Category.class, 1);
		System.out.println(c1);
		
		ctx.close();
	}

}
