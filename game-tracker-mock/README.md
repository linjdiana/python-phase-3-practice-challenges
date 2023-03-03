# Object Relations Code Challenge - Game Tracker

For this assignment, we'll be working with a game tracking domain.

We have three models: `Game`, `Player`, and `Result`.

For our purposes, a `Game` has many `Result`s, a `Player` has many
`Result`s, and a `Result` belongs to a `Player` and to a `Game`.

`Game` - `Player` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Game

- `Game __init__(self, title)`
  - `Game` is initialized with a title (string)
  - Title **cannot be** changed after the `Game` is initialized
- `Game property title`
  - Returns the `Game`'s title
  - Titles must be strings greater than 0 characters

#### Player

- `Player __init__(self, username)`
  - `Player` is initialized with a username (string)
  - Usernames **can be** changed after the Player is initialized
- `Player property username`
  - Returns the Player's username
  - Usernames must be strings between 2 and 16 characters,
    inclusive

#### Result

- `Result __init__(self, player, game, score)`
  - `Result` is initialized with a `Player` instance, a `Game` instance, and a
    score (number)
- `Result property score`
  - Returns the score for the `Result` instance
  - Scores must be integers between 1 and 5000, inclusive

### Object Relationship Attributes and Properties

#### Result

- `Result property player`
  - Returns the player for the Result
  - Players must be `Player` instances
- `Result property game`
  - Returns the game that was played
  - Games must be `Game` instances

#### Player

- `Player results()`
  - Returns a list of `Result` instances associated with the `Player` instance.
- `Player games_played()`
  - Returns a list of `Game` instances played by the `Player` instance.

#### Game

- `Game results()`
  - Returns a list of all the `Result` instances for the `Game`.
- `Game players()`
  - Returns a list of all of the `Player` instances that played the `Game`.

### Aggregate and Association Methods

#### Player

- `Player played_game(game)`
  - Returns `True` if the `Player` has played this `Game`
   returns `False`
    otherwise
- `Player num_times_played(game)`
  - Returns the number of times the `Player` instance has played the `Game` instance
- `Player add_result(game, score)`
  - A `Game` instance and a score (number) are passed in as arguments
  - This method should create a new `Result` instance with that `Player` instance, `Game` instance, and score

#### Game

- `Game average_score(player)`
  - Returns the average of all the player's scores for the `Game` instance
  - To average scores, add all result scores together for the player and divide by the total number
    of results for the player.

#### Player

- `Player classmethod highest_scored(game)`
  - Returns the `Player` instance with the highest average game score.
  - hint: will need a way to remember all `Player` objects
  - hint: do you have a method to get the average score on a game for a particular player?

### Bonus: For any invalid inputs raise an `Exception`.

Uncomment the following lines in the test files:

#### player_tests.py

- lines 0 - 0

#### game_tests.py

- lines 34 - 38

#### result_tests.py

- lines 0 - 0
