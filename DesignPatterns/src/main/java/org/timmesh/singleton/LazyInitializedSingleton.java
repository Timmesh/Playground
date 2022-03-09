package org.timmesh.singleton;

/**
 * <pre>
 * <b>Description : </b>
 * LazyInitializedSingleton. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:19 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class LazyInitializedSingleton {
    /**
     * LazyInitializedSingleton instance.
     */
    private static LazyInitializedSingleton instance;

    /**
     * <pre>
     * <b>Description : </b>
     * LazyInitializedSingleton.
     *
     * </pre>
     */
    private LazyInitializedSingleton() {
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'LazyInitializedSingleton' attribute value.
     *
     * @return LazyInitializedSingleton , null if not found
     * </pre>
     */
    public static LazyInitializedSingleton getInstance() {
        System.out.println("Inside " + LazyInitializedSingleton.class);
        if (instance == null) {
            instance = new LazyInitializedSingleton();
        }
        return instance;
    }
}
