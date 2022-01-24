package org.timmesh.programs;

import java.util.List;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.timmesh.config.AppConfig4;
import org.timmesh.dao.DaoException;
import org.timmesh.dao.ProductDao;
import org.timmesh.entity.Product;

public class P03_TestingJdbcTemplateProductDao {

	public static void main(String[] args) throws DaoException {
		AnnotationConfigApplicationContext ctx;
		ctx = new AnnotationConfigApplicationContext(AppConfig4.class);

		ProductDao dao = ctx.getBean("jtDao", ProductDao.class);

		Product p = dao.getProduct(1);
		System.out.println(p);
		p.setUnitPrice(p.getUnitPrice() + 1);
		dao.updateProduct(p);
		System.out.println("Price updated");

		List<Product> list = dao.getProductsByPriceRange(50.0, 200.0);
		System.out.println("There are " + list.size() + " products between $50 and $200");

		list = dao.getDiscontinuedProducts();
		System.out.println("There are " + list.size() + " discontinued products");
		ctx.close();
	}

}
