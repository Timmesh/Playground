package org.timmesh.singleton;
import java.io.Serializable;

/**
 * <pre>
 * <b>Description : </b>
 * SerializedSingleton. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:19 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class SerializedSingleton implements Serializable {

    /**
     * long serialVersionUID.
     */
    private static final long serialVersionUID = -7604766932017737115L;

    /**
     * int i.
     */
    private int i = 10;

    /**
     * <pre>
     * <b>Description : </b>
     * SerializedSingleton.
     *
     * </pre>
     */
    private SerializedSingleton() {
    }

    /**
     * <pre>
     * <b>Description : </b>
     * SingletonHelper. 
     *
     * @version $Revision: 001 $ $Date: 2014-12-20 11:55:19 $
     * @author $Author: timmesh.kurmayya $
     * </pre>
     */
    private static class SingletonHelper {
        /**
         * SerializedSingleton instance.
         */
        private static final SerializedSingleton instance = new SerializedSingleton();
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'SerializedSingleton' attribute value.
     *
     * @return SerializedSingleton , null if not found
     * </pre>
     */
    public static SerializedSingleton getInstance() {
        return SingletonHelper.instance;
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'int' attribute value.
     *
     * @return int , null if not found
     * </pre>
     */
    public int getI() {
        return i;
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Set the 'iParam' attribute value.
     *
     * @param iParam , may be null
     * </pre>
     */
    public void setI(final int iParam) {
        this.i = iParam;
    }

}
