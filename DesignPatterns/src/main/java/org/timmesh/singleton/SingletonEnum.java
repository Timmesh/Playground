package org.timmesh.singleton;

import java.util.ArrayList;
import java.util.List;

public enum SingletonEnum {
	INSTACE;

	private List<String> contentList = new ArrayList<String>();

	private SingletonEnum() {
		contentList.add("Item1");
	}

	public List<String> getInstance() {
		return contentList;
	}

	public static void main(String[] args) {
		System.out.println(SingletonEnum.INSTACE.getInstance());

		SingletonEnum INSTACE2 = SingletonEnum.INSTACE;
		INSTACE.getInstance().add("Item2");

		System.out.println(INSTACE.getInstance());

		INSTACE2.getInstance().add("Item3");
		System.out.println(INSTACE2.getInstance());
		System.out.println(SingletonEnum.INSTACE.getInstance());
	}
};
