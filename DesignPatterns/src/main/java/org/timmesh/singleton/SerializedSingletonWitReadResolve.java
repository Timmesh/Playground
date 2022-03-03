package org.timmesh.singleton;
import java.io.Serializable;

/**
 * <pre>
 * <b>Description : </b>
 * SerializedSingletonWitReadResolve. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-20 11:55:20 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class SerializedSingletonWitReadResolve implements Serializable {

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

    /**
     * <pre>
     * <b>Description : </b>
     * SerializedSingletonWitReadResolve.
     *
     * </pre>
     */
    private SerializedSingletonWitReadResolve() {
    }

    /**
     * <pre>
     * <b>Description : </b>
     * SingletonHelper. 
     *
     * @version $Revision: 001 $ $Date: 2014-12-20 11:55:20 $
     * @author $Author: timmesh.kurmayya $
     * </pre>
     */
    private static class SingletonHelper {
        /**
         * SerializedSingletonWitReadResolve instance.
         */
        private static final SerializedSingletonWitReadResolve instance = new SerializedSingletonWitReadResolve();
    }

    /**
     * <pre>
     * <b>Description : </b>
     * Get the 'SerializedSingletonWitReadResolve' attribute value.
     *
     * @return SerializedSingletonWitReadResolve , null if not found
     * </pre>
     */
    public static SerializedSingletonWitReadResolve getInstance() {
        return SingletonHelper.instance;
    }

    /**
     * <pre>
     * <b>Description : </b>
     * readResolve.
     *
     * @return Object , null if not found
     * </pre>
     */
    protected Object readResolve() {
        return SingletonHelper.instance;
    }

}
