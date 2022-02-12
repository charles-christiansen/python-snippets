## Longest Palindromic Substring
## LeetCode: https://leetcode.com/problems/longest-palindromic-substring/
## Given a String, find the longest palindromic sustring in the string
## The solution is an implementation of Manacher's algorithm.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # add center markers to the string
        ns=s.replace("","|")
        radii=[0]*len(ns)
        pals=[""]*len(ns)

        center=0
        radius=0

        # for each center (pipes and characters), calculate the radius of the longest palindrome
        while center < len(ns):
            while center-(radius+1) >= 0 and center+radius+1 < len(ns) and ns[center-(radius+1)] == ns[center+radius+1]:
                radius+=1
            radii[center]=radius
            pals[center]=ns[center-radius:center+radius]

            prevCenter=center
            prevRadius=radius
            center+=1
            radius=0

            # check whether the palindrome at the previous center
            # is part of a larger palindrome. This allows us to
            # potentially skip checking some centers and speeds
            # up the algorithm.
            while center < prevCenter+prevRadius:
                mirroredCenter=prevCenter-(center-prevCenter)
                maxMirroredRadius=prevCenter+prevRadius-center

                if radii[mirroredCenter] < maxMirroredRadius:
                    radii[center]=radii[mirroredCenter]
                    center+=1
                elif radii[mirroredCenter] > maxMirroredRadius:
                    radii[center]=maxMirroredRadius
                    center+=1
                else:
                    radius=maxMirroredRadius
                    break

        idx=radii.index(max(radii))
        pal=pals[idx]
        return pal.replace("|","")

s=Solution()
# returns bab (aba would also be right, but max seems to return the earliest occurrence)
print(s.longestPalindrome("babad"))
# returns bb
print(s.longestPalindrome("cbbd"))
# returns 0dec31dd13ced0
print(s.longestPalindrome("0ea7c027bf0f66a178a409b360dec31dd13ced0403197125e402644"))
