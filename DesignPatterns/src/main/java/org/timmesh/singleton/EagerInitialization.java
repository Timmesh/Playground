package org.timmesh.singleton;
/**
 * <pre>
 * <b>Description : </b>
 * EagerInitialization. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:19 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class EagerInitialization {
	/**
	 * EagerInitialization singleInstance.
	 */
	private static EagerInitialization singleInstance = new EagerInitialization();

	/**
	 * <pre>
	 * <b>Description : </b>
	 * EagerInitialization.
	 *
	 * </pre>
	 */
	private EagerInitialization() {
	}

	/**
	 * <pre>
	 * <b>Description : </b>
	 * Get the 'EagerInitialization' attribute value.
	 *
	 * @return EagerInitialization , null if not found
	 * 
	 * </pre>
	 */
	public static EagerInitialization getInstance() {
		System.out.println("Inside" + EagerInitialization.class);
		return singleInstance;
	}
}
