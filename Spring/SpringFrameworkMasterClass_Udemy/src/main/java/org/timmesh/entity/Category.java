package org.timmesh.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@NoArgsConstructor
@Getter
@Setter
public class Category {
	private Integer categoryId;
	private String categoryName;
	private String description;
	private byte[] picture;
}
