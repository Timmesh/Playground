package org.timmesh.singleton;

/**
 * <pre>
 * <b>Description : </b>
 * StaticBlockSingleton. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:20 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class StaticBlockSingleton {
    /**
     * StaticBlockSingleton instance.
     */
    private static StaticBlockSingleton instance;

    /**
     * <pre>
     * <b>Description : </b>
     * StaticBlockSingleton.
     *
     * </pre>
     */
    private StaticBlockSingleton() {
    }

    // static block initialization for exception handling
    static {
        try {
            instance = new StaticBlockSingleton();
        }
        catch (Exception e) {
            throw new RuntimeException("Exception occured in creating singleton instance");
        }
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'StaticBlockSingleton' attribute value.
     *
     * @return StaticBlockSingleton , null if not found
     * </pre>
     */
    public static StaticBlockSingleton getInstance() {
        System.out.println("Inside " + StaticBlockSingleton.class);
        return instance;
    }
}
