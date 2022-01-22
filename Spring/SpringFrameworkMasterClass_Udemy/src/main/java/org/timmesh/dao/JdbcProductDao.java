package org.timmesh.dao;

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

	@Override
	public long count() {
		return 100;
	}

}
