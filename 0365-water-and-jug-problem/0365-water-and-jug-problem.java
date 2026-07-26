class Solution {
    public boolean canMeasureWater(int x, int y, int target) {
        if (target > x + y) {
            return false;
        }

        if (target == 0) {
            return true;
        }

        return target % gcd(x, y) == 0;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}