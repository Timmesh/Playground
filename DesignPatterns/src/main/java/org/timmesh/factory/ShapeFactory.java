package org.timmesh.factory;

import org.timmesh.factory.impl.Circle;
import org.timmesh.factory.impl.Rectangle;
import org.timmesh.factory.impl.Square;
import org.timmesh.factory.interfaces.Shape;

/**
 * <pre>
 * <b>Description : </b>
 * ShapeFactory. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-21 01:21:30 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class ShapeFactory {

    // use getShape method to get object of type shape
    /**
     * <pre>
     * <b>Description : </b>
     * getShape.
     *
     * @param shapeType , may be null
     * @return Shape , null if not found
     * </pre>
     */
    public Shape getShape(final String shapeType) {
        if (shapeType == null) {
            return null;
        }
        if (shapeType.equalsIgnoreCase("CIRCLE")) {
            return new Circle();
        }
        else if (shapeType.equalsIgnoreCase("RECTANGLE")) {
            return new Rectangle();
        }
        else if (shapeType.equalsIgnoreCase("SQUARE")) {
            return new Square();
        }
        return null;
    }
}
