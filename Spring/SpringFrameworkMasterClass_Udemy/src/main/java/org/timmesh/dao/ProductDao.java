package org.timmesh.dao;

import java.util.List;

import org.timmesh.entity.Product;

public interface ProductDao {
	// CRUD OPERATIONS

	public default void addProduct(Product product) throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default void updateProduct(Product product) throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default Product getProduct(Integer productId) throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default void deleteProduct(Integer productId) throws DaoException {
		throw new DaoException("Method not implemented");
	}

	// QUERIES
	public default List<Product> getAllProducts() throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default List<Product> getProductsByPriceRange(Double min, Double max) throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default List<Product> getProductsInCategory(Integer categoryId) throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default List<Product> getProductsNotInStock() throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default List<Product> getProductsOnOrder() throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default List<Product> getDiscontinuedProducts() throws DaoException {
		throw new DaoException("Method not implemented");
	}

	public default long count() throws DaoException {
		throw new DaoException("Method not implemented");
	}
}
