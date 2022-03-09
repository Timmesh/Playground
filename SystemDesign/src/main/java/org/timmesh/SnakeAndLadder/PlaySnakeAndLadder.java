package org.timmesh.SnakeAndLadder;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @author timmesh
 *
 */
public class PlaySnakeAndLadder {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
			System.out.println("Enter Number of Players:");
			Scanner in = new Scanner(System.in);
			int playerCount = in.nextInt();
			Map<String, Object> collectPlayerDetails = Stream.iterate(1, i -> i + 1).limit(playerCount)
					.map(playerId -> {
						System.out.println("Enter Player Name:");
						String playerName = in.next();
						return new Player(playerId, playerName);
					}).collect(Collectors.teeing(Collectors.toCollection(LinkedList::new),
							Collectors.toMap(Function.identity(), f -> 0), (e1, e2) -> {
								Map<String, Object> ma = new HashMap<>();
								ma.put("PlayerList", e1);
								ma.put("PlayersPostion", e2);
								return ma;
							}));
			in.close();
			Dice dice = new Dice(1);
			Map<Integer, Integer> snakes = new HashMap<Integer, Integer>();
			snakes.put(30, 11);
			snakes.put(98, 2);
			Map<Integer, Integer> ladders = new HashMap<Integer, Integer>();
			ladders.put(10, 35);
			ladders.put(50, 93);
			GameBoard gameBoard = new GameBoard(dice, snakes, ladders,
					(Queue<Player>) collectPlayerDetails.get("PlayerList"),
					(Map<Player, Integer>) collectPlayerDetails.get("PlayersPostion"));
			gameBoard.playGame();
		}

}
