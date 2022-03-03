package org.timmesh.singleton;

/**
 * <pre>
 * <b>Description : </b>
 * ThreadSafeSingleton. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:20 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class ThreadSafeSingleton {

    /**
     * ThreadSafeSingleton instance.
     */
    private static ThreadSafeSingleton instance;

    /**
     * <pre>
     * <b>Description : </b>
     * ThreadSafeSingleton.
     *
     * </pre>
     */
    private ThreadSafeSingleton() {
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'ThreadSafeSingleton' attribute value.
     *
     * @return ThreadSafeSingleton , null if not found
     * </pre>
     */
	public static synchronized ThreadSafeSingleton getInstance() {
        System.out.println("Inside " + ThreadSafeSingleton.class);
        if (instance == null) {
            instance = new ThreadSafeSingleton();
        }
        return instance;
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'ThreadSafeSingleton' attribute value.
     *
     * @return ThreadSafeSingleton , null if not found
     * </pre>
     */
    public static ThreadSafeSingleton getInstanceUsingDoubleLocking() {
        if (instance == null) { // Single Checked
            System.out.println("Inside " + ThreadSafeSingleton.class);
            synchronized (ThreadSafeSingleton.class) {
                if (instance == null) { // Double checked
                    instance = new ThreadSafeSingleton();
                }
            }
        }
        return instance;
    }

}
