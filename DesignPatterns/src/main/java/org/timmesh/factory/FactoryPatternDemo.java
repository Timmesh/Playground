package org.timmesh.factory;

import org.timmesh.factory.interfaces.Shape;

/**
 * <pre>
 * <b>Description : </b>
 * FactoryPatternDemo. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-21 01:21:30 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class FactoryPatternDemo {

    /**
     * <pre>
     * <b>Description : </b>
     * main.
     *
     * @param args , may be null
     * </pre>
     */
    public static void main(final String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        // get an object of Circle and call its draw method.
        Shape shape1 = shapeFactory.getShape("CIRCLE");

        // call draw method of Circle
        shape1.draw();

        // get an object of Rectangle and call its draw method.
        Shape shape2 = shapeFactory.getShape("RECTANGLE");

        // call draw method of Rectangle
        shape2.draw();

        // get an object of Square and call its draw method.
        Shape shape3 = shapeFactory.getShape("SQUARE");

        // call draw method of circle
        shape3.draw();
    }
}
