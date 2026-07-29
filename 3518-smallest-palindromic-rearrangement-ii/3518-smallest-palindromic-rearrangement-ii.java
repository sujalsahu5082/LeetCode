class Solution {
    static final int LIMIT = 1_000_000;
    List<Integer> primes = new ArrayList<>();

    public String smallestPalindrome(String s, int k) {
        int[] freq = new int[26];

        for (char c : s.toCharArray())
            freq[c - 'a']++;

        String mid = "";
        int[] half = new int[26];
        int halfLen = 0;

        for (int i = 0; i < 26; i++) {
            if ((freq[i] & 1) == 1)
                mid = String.valueOf((char) ('a' + i));
            half[i] = freq[i] / 2;
            halfLen += half[i];
        }

        sieve(halfLen);

        if (countWays(half) < k)
            return "";

        StringBuilder left = new StringBuilder();

        for (int pos = 0; pos < halfLen; pos++) {
            for (int c = 0; c < 26; c++) {
                if (half[c] == 0) continue;

                half[c]--;

                long ways = countWays(half);

                if (ways >= k) {
                    left.append((char) ('a' + c));
                    break;
                } else {
                    k -= ways;
                    half[c]++;
                }
            }
        }

        StringBuilder ans = new StringBuilder(left);
        ans.append(mid);
        ans.append(new StringBuilder(left).reverse());

        return ans.toString();
    }

    private void sieve(int n) {
        boolean[] comp = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            if (!comp[i]) {
                primes.add(i);
                if ((long) i * i <= n) {
                    for (int j = i * i; j <= n; j += i)
                        comp[j] = true;
                }
            }
        }
    }

    private int factExp(int n, int p) {
        int res = 0;
        while (n > 0) {
            n /= p;
            res += n;
        }
        return res;
    }

    private long countWays(int[] cnt) {
        int total = 0;
        for (int x : cnt) total += x;

        long ans = 1;

        for (int p : primes) {
            if (p > total) break;

            int exp = factExp(total, p);

            for (int x : cnt)
                exp -= factExp(x, p);

            while (exp-- > 0) {
                ans *= p;
                if (ans > LIMIT)
                    return LIMIT;
            }
        }

        return ans;
    }
}