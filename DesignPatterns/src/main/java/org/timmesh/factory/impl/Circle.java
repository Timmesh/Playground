package org.timmesh.factory.impl;

import org.timmesh.factory.interfaces.Shape;

/**
 * <pre>
 * <b>Description : </b>
 * Circle. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-21 01:21:30 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class Circle implements Shape {

    /**
     * <pre>
     * <b>Description : </b>
     * draw.
     *
     * </pre>
     */
    public void draw() {
        System.out.println("Inside Circle::draw() method.");
    }
}
