/*
 * This code contains copyright information which is the proprietary property
 * of SITA Information Network Computing Limited (SITA). No part of this
 * code may be reproduced, stored or transmitted in any form without the prior
 * written permission of SITA.
 *
 * Copyright (C) SITA Information Network Computing Limited 2011-2012.
 * All rights reserved.
 */
package org.timmesh.factory.impl;

import org.timmesh.factory.interfaces.Shape;

/**
 * <pre>
 * <b>Description : </b>
 * Rectangle. 
 *
 * @version $Revision: 001 $ $Date: 2014-12-21 01:21:30 $
 * @author $Author: timmesh.kurmayya $
 * </pre>
 */
public class Rectangle implements Shape {

    /**
     * <pre>
     * <b>Description : </b>
     * draw.
     *
     * </pre>
     */
    public void draw() {
        System.out.println("Inside Rectangle::draw() method.");
    }
}
