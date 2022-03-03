package org.timmesh.singleton;

/**
 * <pre>
 * <b>Description : </b>
 * BillPughSingleton. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:19 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class BillPughSingleton {

    /**
     * <pre>
     * <b>Description : </b>
     * BillPughSingleton.
     *
     * </pre>
     */
    private BillPughSingleton() {
    }

    /**
     * <pre>
     * <b>Description : </b>
     * SingletonHelper is loaded on the first execution of SingletongetInstance()
     * or the first access to SingletonHolderINSTANCE
     * not before.
     * 
     * @version $Revision: 001 $ $Date: 2014-12-20 11:55:19 $
     * @author $Author: timmesh.kurmayya $
     * </pre>
     */
    private static class SingletonHelper {
        /**
         * BillPughSingleton INSTANCE.
         */
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'BillPughSingleton' attribute value.
     *
     * @return BillPughSingleton , null if not found
     * </pre>
     */
    public static BillPughSingleton getInstance() {
        System.out.println("Inside " + BillPughSingleton.class);
        return SingletonHelper.INSTANCE;
    }
    
}
