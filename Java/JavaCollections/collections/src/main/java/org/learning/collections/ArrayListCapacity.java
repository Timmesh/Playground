package org.learning.collections;
import java.lang.reflect.Field;
import java.util.ArrayList;

public class ArrayListCapacity {
	public static void main(String[] args) throws Exception {
        ArrayList<Integer> list = new ArrayList<Integer>();
        System.out.format("Size: %2d, Capacity: %2d%n",
                list.size(), getCapacity(list));
        for (int i = 0; i < 25; i++) {
            list.add(i);
            System.out.format("Size: %2d, Capacity: %2d%n",
                              list.size(), getCapacity(list));
        }
    }

    static int getCapacity(ArrayList<?> l) throws Exception {
        Field dataField = ArrayList.class.getDeclaredField("elementData");
        dataField.setAccessible(true);
        return ((Object[]) dataField.get(l)).length;
    }
}
