package org.timmesh.programs;

import java.util.List;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.timmesh.config.AppConfig4;
import org.timmesh.dao.DaoException;
import org.timmesh.dao.ProductDao;
import org.timmesh.entity.Product;


public class P06_TestingHibernateTempalteProductDao {

	public static void main(String[] args) throws DaoException {
		AnnotationConfigApplicationContext ctx;
		ctx = new AnnotationConfigApplicationContext(AppConfig4.class);
		
		ProductDao dao = ctx.getBean("htDao", ProductDao.class);
		System.out.println("dao is an instance of " + dao.getClass().getName());
		
		List<Product> list = dao.getAllProducts();
		System.out.println("There are " + list.size() + " products.");
		
		Double min = 50.0, max = 200.0;
		list = dao.getProductsByPriceRange(min, max);
		System.out.println("There are " + list.size() + " products between $" + min + " and $" + max);
		
		min = 200.0;
		max = 50.0;
		list = dao.getProductsByPriceRange(min, max);
		System.out.println("There are " + list.size() + " products between $" + min + " and $" + max);
		
		list = dao.getDiscontinuedProducts();
		System.out.println("There are " + list.size() + " discontinued products.");
		
		long pc = dao.count();
		System.out.println("There are " + pc + " products.");
		
		Product p = dao.getProduct(1);
		System.out.println(p.getProductName() + " --> " + p.getUnitPrice());
		
		p.setUnitPrice(p.getUnitPrice() + 1);
		try {
			dao.updateProduct(p);
		}
		catch(DaoException ex) {
			System.out.println("There was an error: " + ex.getMessage());
		}
		
		System.out.println("End of testing.");
		
		ctx.close();
	}

}
