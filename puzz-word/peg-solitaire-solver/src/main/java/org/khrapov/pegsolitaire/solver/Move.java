package org.khrapov.pegsolitaire.solver;

public class Move {
	public final int x1;
	public final int y1;
	public final int x2;
	public final int y2;
	public char dir;

	public Move(int x1, int y1, int x2, int y2) {
		this.x1 = x1;
		this.y1 = y1;
		this.x2 = x2;
		this.y2 = y2;

		if (x1 < x2) {
			this.dir = 'v';
		} else if (x1 > x2) {
			this.dir = '^';
		} else if (y1 < y2) {
			this.dir = '>';
		} else if (y1 > y2) {
			this.dir = '<';
		}
	}

	public String toString() {
		return String.format("[%d, %d, \"%c\"]", y1, x1, dir);
	}
}
