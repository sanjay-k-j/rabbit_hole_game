# Mr. Bunny's Carrot Quest Game

Welcome to Mr. Bunny's Carrot Quest Game! In this game, you will help Mr. Bunny, our friendly neighborhood rabbit, collect carrots from the yard and deposit them into rabbit holes. Beware of obstacles along the way!

## Game Elements
- **Rabbit**: Mr. Bunny is represented by the character "r" on the game map and "R" when carrying a carrot.
- **Carrot**: Carrots are represented by the character "c." Mr. Bunny's goal is to collect these carrots.
- **Rabbit Hole**: Rabbit holes are represented by the character "O." Mr. Bunny must deposit carrots into these holes.
- **Pathway Stone**: Pathway stones are represented by the character "-." These are the paths on the game map.

## Game Story
Our protagonist, Mr. Bunny, needs your help in gathering carrots and safely storing them in his rabbit holes. Can you guide him through the yard and complete the quest?

## Game Design

### Random Map Generator
- To start the game, we generate a random 2D map of the yard.
- The map contains:
  - One rabbit ("r" or "R").
  - Multiple carrots ("c").
  - Multiple rabbit holes ("O").
  - Pathway stones ("-").
- The map is randomly generated, providing a unique experience each time you play.

### The Game
- You can control Mr. Bunny's movements using the following keys:
  - "a": Move left.
  - "d": Move right.
  - "w": Move up.
  - "s": Move down.
  - Combine these keys for diagonal movement.
- Mr. Bunny cannot move across carrots; he must pick them up using the "p" key.
- When Mr. Bunny picks up a carrot, his character changes from "r" to "R."
- He also cannot move across rabbit holes; he must jump over them using the "j" key. The jump direction depends on his relative position to the hole.
- To deposit a carrot into a hole, position Mr. Bunny adjacent to the hole and press the "p" key. The game concludes when any carrot is deposited into any hole.
- Mr. Bunny can carry only one carrot at a time.
- The entire game map operates on a single grid on the command line, ensuring a seamless gaming experience.

### Winning the Game
- To win the game, Mr. Bunny must deposit at least one carrot into a rabbit hole.
- If he accomplishes this, you will see a "You Win!" message on the screen.

## How to Play
1. Start the game by specifying the map grid size, the number of carrots, and the number of rabbit holes.
2. Use the following keys to control Mr. Bunny:
   - "w": Move up.
   - "a": Move left.
   - "s": Move down.
   - "d": Move right.
   - "p": Pick up a carrot.
   - "j": Jump over rabbit holes.
   - "q": Quit the game.
3. Your goal is to guide Mr. Bunny to deposit at least one carrot into a rabbit hole to win the game.
4. Enjoy the game and help Mr. Bunny complete his Carrot Quest!

Have fun playing Mr. Bunny's Carrot Quest Game!
