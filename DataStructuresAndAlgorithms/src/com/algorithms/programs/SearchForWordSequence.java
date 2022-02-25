package com.algorithms.programs;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class SearchForWordSequence {

	public static void main(String[] args) {
		System.out.println(getSeqNumber("P"));
		System.out.println(getSeqNumber("PLA"));
		System.out.println(getSeqNumber("PL"));
		System.out.println(getSeqNumber("Z"));
		String lastMatchedSequence = getLastMatchedSequence();
		System.out.println("Length of List" + (lastMatchedSequence != "" ? getSeqNumber(lastMatchedSequence) : 0));

	}

	private static String getLastMatchedSequence() {
		Optional<String> findFirstMatchingChar = Stream.iterate('Z', i -> (char) (i - 1)).limit(26)
				.map(s -> s.toString()).filter(s -> getSeqNumber(s) == 0).findFirst();
		if (!findFirstMatchingChar.isPresent())
			return "";
		Optional<String> findSecondMatchingChar = Stream.iterate('Z', i -> (char) (i - 1)).limit(26)
				.map(s -> findFirstMatchingChar.get() + "" + s.toString()).filter(q -> getSeqNumber(q) == 0)
				.findFirst();
		Optional<String> matchedSequence = Stream.iterate('Z', i -> (char) (i - 1)).limit(26)
				.map(s -> findSecondMatchingChar.get() + "" + s.toString()).filter(q -> getSeqNumber(q) > 0)
				.findFirst();
		return matchedSequence.get();
	}

	private static int getSeqNumber(String seq) {
		List<String> asList = Arrays.asList("ABC","ACA","ACC", "LAA","LAP","MAN","PLA","XYZ");
		Map<String, Map<String, List<String>>> collect = asList.stream()
				.collect(Collectors.teeing(Collectors.groupingBy(r -> ((String) r).substring(0, 1)),
						Collectors.groupingBy(r -> ((String) r).substring(0, 2)), (e1, e2) -> {
							Map<String, Map<String, List<String>>> ma = new HashMap<>();
							ma.put("Single", e1);
							ma.put("Double", e2);
							return ma;
						}));

		Map<String, List<String>> mapOfOneCharacter = collect.get("Single");
		if (mapOfOneCharacter == null || mapOfOneCharacter.isEmpty())
			return -1;
		if (seq.length() == 3) {
			List<String> list = mapOfOneCharacter.get(seq.substring(0, 1));
			if (list == null) {
				return -1;
			} else if (list.contains(seq)) {
				int indexOf = asList.indexOf(seq);
				return indexOf + 1;
			} else if (list != null) {
				return 0;
			}
		} else if (seq.length() == 2) {
			Map<String, List<String>> mapofTwoCharacters = collect.get("Double");
			List<String> list = mapofTwoCharacters.get(seq.substring(0, 2));
			if (list != null) {
				return 0;
			}
		} else {
			List<String> list = mapOfOneCharacter.get(seq.substring(0, 1));
			if (list != null) {
				return 0;
			}
		}
		return -1;
	}

}
