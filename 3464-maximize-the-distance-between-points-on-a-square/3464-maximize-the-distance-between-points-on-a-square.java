class Solution {
    record Point(int x, int y, long unRolledDist) {
        public static int dist(Point a, Point b) {
            return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
        }
    }

    /*
     * Unfold the points into a 1D array
     * Sort the array
     * Binary search on res with range [1, side], as there are at least 4 points, the best score can be size.
     *
     * Now for some dist,
     * we need to select k points from the array, where each point has at least dist distance to the previous point.
     * */
    public int maxDistance(int side, int[][] points, int k) {
        Point[] unfoldedArr = new Point[points.length];
        int arrLen = 0;

        for (int[] point : points) {
            int x = point[0];
            int y = point[1];
            long unRolledDist = 0;
            if (x == 0) unRolledDist = y;
            else if (y == side) unRolledDist = (long) side + x;
            else if (x == side) unRolledDist = 3L * side - y;
            else if (y == 0) unRolledDist = 4L * side - x;
            unfoldedArr[arrLen++] = new Point(x, y, unRolledDist);
        }
        Arrays.sort(unfoldedArr, Comparator.comparingLong(Point::unRolledDist));

        int left = 1;
        int right = side;
        while (left < right) {
            int mid = (left + right + 1) >> 1;
            if (isPossible(unfoldedArr, mid, k)) left = mid;
            else right = mid - 1;
        }
        return left;
    }

    private boolean isPossible(Point[] unfoldedArr, int limit, int k) {
        int n = unfoldedArr.length;
        for (int i = 0; i < n; i++)
            if (isPossible(unfoldedArr, i, limit, k)) return true;

        return false;
    }

    private boolean isPossible(Point[] unfoldedArr, int firstIdx, int limit, int k) {
        int n = unfoldedArr.length;
        int prevIdx = firstIdx;
        Point prev = unfoldedArr[prevIdx];
        k--;

        while (k > 0 && prevIdx < n - 1) {
            int nextIdx = lowerBound(unfoldedArr, prev, prevIdx + 1, n - 1, limit);
            if (nextIdx == -1 || (k == 1 && Point.dist(unfoldedArr[firstIdx], unfoldedArr[nextIdx]) < limit)) return false;
            prevIdx = nextIdx;
            prev = unfoldedArr[prevIdx];
            k--;
        }
        return k == 0;
    }

    // finds first point whose dist from prev is as least limit
    private int lowerBound(Point[] unfoldedArr, Point prev, int left, int right, int limit) {
        while (left < right) {
            int mid = (left + right) >> 1;
            if (Point.dist(prev, unfoldedArr[mid]) >= limit) right = mid;
            else left = mid + 1;
        }
        return Point.dist(prev, unfoldedArr[left]) < limit ? -1 : left;
    }
}
