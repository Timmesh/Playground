package org.timmesh.SnakeAndLadder;

import java.io.IOException;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class GameBoard {

	private Dice dice;
	private Map<Integer, Integer> snakes;
	private Map<Integer, Integer> ladders;
	private Queue<Player> players;
	private Map<Player, Integer> playersPosition;

	public void playGame() {
		while (players.size() > 1) {
			Player player = players.poll();
			System.out.println(player.getName() + "Roll Dice");
			int rollDice = dice.rollDice();
			System.out.println("The Dice value is: " + rollDice);
			Integer newPosition = playersPosition.get(player) + rollDice;
			if (newPosition == 100) {
				System.out.println(player + "Won the Game");
			} else if (newPosition > 100) {
				System.out.println("fadf");
				players.offer(player);
			} else {
				// Check if there are any snakes/Ladder
				Integer snakeEndLocation = snakes.get(newPosition);
				Integer ladderEndLocation = ladders.get(newPosition);
				if (snakeEndLocation != null) {
					System.out.println("Snake Bit the Player" + player + "Moved to Postion:" + snakeEndLocation);
					newPosition = snakeEndLocation;
				} else if (ladderEndLocation != null) {
					System.out.println("Ladder Climbed By Player" + player + "Moved to Postion:" + ladderEndLocation);
					newPosition = ladderEndLocation;
				}
				System.out.println("Player New Position is: " + newPosition);
				System.out.println();
				playersPosition.put(player, newPosition);
				players.offer(player);
			}
		}
	}
}
