package org.timmesh.SnakeAndLadder;

import java.util.Random;

import lombok.AllArgsConstructor;
import lombok.Setter;

@Setter
@AllArgsConstructor
public class Dice {

	int numberOfDice;
	
	public int rollDice() {
		return new Random().ints(numberOfDice, 1, 7).sum();
	}
}
