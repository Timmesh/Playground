package org.timmesh.programs;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.jdbc.core.JdbcTemplate;
import org.timmesh.config.AppConfig4;

public class P02_TestingJdbcTemplate {

	static JdbcTemplate template;

	public static void main(String[] args) {

		AnnotationConfigApplicationContext ctx;
		ctx = new AnnotationConfigApplicationContext(AppConfig4.class);
		template = ctx.getBean(JdbcTemplate.class);

//		insertShipper();
//		updateShipperPhone(4, "(973) 142-4784");
//		printProductCount();
		printShipperName(4);
		ctx.close();
	}

	static void printShipperName(int shipperId) {
		String sql = "select company_name from shippers where shipper_id=?";
		String name = template.queryForObject(sql, String.class, shipperId);
		System.out.println("Shipper name = " + name);
	}
	
	static void printProductCount() {
		String sql = "select count(*) from products";
		Integer pc = template.queryForObject(sql, Integer.class);
		System.out.println("There are " + pc + " products.");
	}
	
	static void updateShipperPhone(int id, String phone) {
		String sql = "update shippers set phone=? where shipper_id=?";
		template.update(sql, phone, id);
		System.out.println("Phone updated!");
	}
	
	private static void insertShipper() {
		template.update("insert into shippers values(?,?,?)", 
				4, "KVinod Transports", "9731424784");
		System.out.println("New shipper data inserted!");
	}

}
