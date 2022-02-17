package com.playground.streams.map;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import com.playground.entities.Staff;
import com.playground.entities.StaffPublic;

/**
 * @author USER
 *
 *         List of objects -> List of other objects This example shows you how
 *         to convert a list of staff objects into a list of StaffPublic
 *         objects.
 */
public class StreamsMap3 {
	public static void main(String[] args) {
		List<Staff> staff = Arrays.asList(new Staff("nakul", 30, new BigDecimal(10000)),
				new Staff("jack", 27, new BigDecimal(20000)), new Staff("lawrence", 33, new BigDecimal(30000)));
		List<StaffPublic> result1 = convertToStaffPublic(staff);
		System.out.println(result1);

		// convert inside the map() method directly.
		List<StaffPublic> result2 = staff.stream().map(temp -> {
			StaffPublic obj = new StaffPublic();
			obj.setName(temp.getName());
			obj.setAge(temp.getAge());
			if ("nakul".equals(temp.getName())) {
				obj.setExtra("this field is for nakul only!");
			}
			return obj;
		}).collect(Collectors.toList());
		System.out.println(result2);
	}

	private static List<StaffPublic> convertToStaffPublic(List<Staff> staff) {
		List<StaffPublic> result = new ArrayList<>();
		for (Staff temp : staff) {
			StaffPublic obj = new StaffPublic();
			obj.setName(temp.getName());
			obj.setAge(temp.getAge());
			if ("nakul".equals(temp.getName())) {
				obj.setExtra("this field is for nakul only!");
			}
			result.add(obj);
		}
		return result;
	}
}
