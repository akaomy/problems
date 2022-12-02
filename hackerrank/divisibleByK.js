// link to the problem https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=three-month-week-one
// Given an array of integers and a positive integer k,
// determine the number of (i, j) pairs where i<j and ar[i] + ar[j] is divisible by k.

function divisibleSumPairs(n, k, ar) {
    let count = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 1; j < n; j++) {
            if (i < j ) {
                if ((ar[i] + ar[j]) % k == 0) {
                    count += 1
                }
            }
        }
    }
    return count;
}