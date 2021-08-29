package org.khrapov.pegsolitaire.solver;

import java.util.ArrayList;

/**
 * Board represents the geometry of a particular Peg Solitaire board.
 * The representation is a rectangular array X by Y in dimension. The places
 * in the array that have a hole that can by occupied by a peg are marked
 * with 1s and the disallowed positions are marked with 0s.
 */
public final class Board
{
    public final int X;
    public final int Y;
    public final int[] dest;
    
    // symmetry
    final boolean verticalFlip;
    final boolean horizontalFlip;
    final boolean leftDiagonalFlip; // top left to bottom right
    final boolean rightDiagonalFlip; // top right to bottom left
    final boolean rotate90;
    final boolean rotate180;
    final boolean rotate270;

    private final boolean[] holes;


    /**
     * Set the dimensions of the array.
     * @param x - horizontal dimension (changes the fastest)
     * @param y - vertical dimension
     * @param holes - int[], which holes are in play. 1 - in play. 0 - outside of the board.
     */
    public Board(int x, int y, int[] holes, int[] dest) {
        if (x < 1 || y < 1) {
            throw new RuntimeException("Board dimensions may not be smaller than 1x1.");
        }

        if (holes.length != x*y) {
            throw new RuntimeException("array size mismatch");
        }

        X = x;
        Y = y;

        this.holes = new boolean[x * y];
        this.dest = dest;

        for (int i = 0; i < this.holes.length; i++) {
            if (holes[i] == 1) {
                this.holes[i] = true;
            }
        }

        SymmetryHelper h = new SymmetryHelper(X, Y, this.holes);

        verticalFlip = h.equals(h.verticalFlip());
        horizontalFlip = h.equals(h.horizontalFlip());
        rotate180 = h.equals(h.rotate180());

        if(X == Y)
        {
            leftDiagonalFlip = h.equals(h.leftDiagonalFlip());
            rightDiagonalFlip = h.equals(h.rightDiagonalFlip());
            rotate90 = h.equals(h.rotate90());
            rotate270 = h.equals(h.rotate270());
        }
        else
        {
            leftDiagonalFlip = false;
            rightDiagonalFlip = false;
            rotate90 = false;
            rotate270 = false;
        }
    }


    /**
     * Create the initial position of the game by marking the hole that will have no peg.
     * @param x - horizontal coordinate of the hole with no peg.
     * @param y - vertical coordinate of the hole with no peg.
     * @return - Initial Position from which to start the search.
     */
    public Position initialPosition(int[] initialPositions) {
        Position position = new Position(this);
        
        for (int i = 0; i < initialPositions.length -1; i += 2) {
			int x = initialPositions[i];
			int y = initialPositions[i+1];
			position.set(x, y, false);
		}
        return position;
    }


    boolean allowed(int i)
    {
        return holes[i];
    }

    public boolean allowed(int x, int y)
    {
        if(x < 0 || y < 0 || x >= X || y >= Y)
        {
            throw new RuntimeException("array index out of bounds");
        }

        int i = y*X + x;
        return holes[i];
    }
}
