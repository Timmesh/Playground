package org.timmesh.singleton;

public class fda {
	private static fda f;

	private fda() {
	}

	public static synchronized fda getInstance() {
		if (f == null) {
			synchronized (fda.class) {
				if (f == null) {
					f = new fda();
				}
			}
		}
		return f;
	}

}
