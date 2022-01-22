package org.timmesh.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.beans.factory.annotation.Autowired;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@NoArgsConstructor
@Getter
@Setter
public class JdbcProductDao implements ProductDao {

	private String driverClassName;
	private String url;
	private String user;
	private String password;
	@Autowired
	private Connection connection;

	private Connection createConnection() throws ClassNotFoundException, SQLException {
		if (connection != null && connection.isClosed() == false) {
			return connection;
		}
		Class.forName(driverClassName);
		return DriverManager.getConnection(url, user, password);
	}

	@Override
	public long count() {
		try (Connection conn = createConnection();
				PreparedStatement stmt = conn.prepareStatement("select count(*) from products");
				ResultSet rs = stmt.executeQuery();) {
			rs.next();
			return rs.getLong(1);
		} catch (Exception ex) {
			throw new RuntimeException(ex);
		}
	}

}
