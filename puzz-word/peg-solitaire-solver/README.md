# Peg Solitaire Solver

A Java library to solve arbitrary Peg Solitaire boards.

Peg Solitaire is an old and very well known board game for one player.
The board is composed of holes filled in with pegs. The initial position
is one hole without a peg (often in the center of the board, but not necessarily).
A move is for a peg to jump over a neighbouring peg into a hole, horizontally or vertically.
The peg being jumped over is removed from the board. The goal of the game is to remove all
the pegs from the board except one. Ideally the last peg should end up in the same hole
that was originally empty. It is not always possible on all boards.

For more information about Peg Solitaire see [Wikipedia](https://en.wikipedia.org/wiki/Peg_solitaire)
or [this page](http://www.gibell.net/pegsolitaire/).

## Algorithm

This is an extremely fast solver. The English board can be solved in mere milliseconds on a
10 year old desktop computer. This is a result of a clever heuristic that allows for a very
aggressive pruning of the search tree.

The search starts with a list of positions that contains only the initial position. On each
iteration of the search, each member of the list produces children - positions that can be
reached from that member by a single jump of any peg. All these children combined produce
the next generation.

Before this new generation is handed off to the next iteration of the search, it is pruned
to reduce the number of positions that need to be searched.

The first stage in pruning is to eliminate the duplicate positions. Symmetry is considered. Any
position that can be converted into another position via any symmetry operation is considered
a duplicate.

At the second stage, for each remaining member of the new generation, we calculate a heuristic
score that determines how likely this position is to produce a solution to the board. The
members are sorted on this score and only `pruningNumber` of highest scoring members are
allowed into the next iteration of the search. This value can be set by the `prune` method. The
smaller the number, the fewer members are selected for the next iteration, the faster is the
search. In many cases `pruningNumber` less than 50 works well. If the `pruningNumber` is too
aggressive, the algorithm may not find a solution. In this case, increase the `pruningNumber`
and rerun the search.

## Usage

To use this library in your own programs you will need to install it into a local Maven repo.
Source JAR and Javadoc JAR files will be included.

```
git clone https://github.com/mkhrapov/peg-solitaire-solver.git
cd peg-solitaire-solver
git checkout 1.0
mvn install
```

Then add the dependency to the Maven POM file.

```xml
<dependency>
  <groupId>org.khrapov</groupId>
  <artifactId>peg-solitaire-solver</artifactId>
  <version>1.0</version>
</dependency>
```

Java example. More examples are in the unit test files and in the Javadoc. Even more complete
examples are in the visualization package.

```java
// Solve English Peg Solitaire Board
int[] englishBoard = new int[] {
    0, 0, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0,
    1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1,
    0, 0, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0
};

Board b = new Board(7, 7, englishBoard);
Position p = b.initialPosition(3, 3);
PruningSearch pruningSearch = new PruningSearch(p);
pruningSearch.prune(121);
int solutions = pruningSearch.search();
```

Package `org.khrapov.pegsolitaire.javafxviz` contains a JavaFX based visualization of
pegsolitaire solutions. It has only been tested with Java 8. It
uses JavaFX library which has undergone a lot of changes in recent
versions of Java. It will probably not work out-of-box with newer versions
of Java. The easiest way to run it currently is to open it in an IDE and run the
main method of one the classes that solves a particular Peg Solitaire board.

Screenshot of visualization.

![](img/english-board-solution.png)

