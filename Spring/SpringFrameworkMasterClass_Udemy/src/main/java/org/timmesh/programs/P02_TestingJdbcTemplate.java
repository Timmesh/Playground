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
		updateShipperPhone(4, "(973) 142-4784");
		ctx.close();
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
