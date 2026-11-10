class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        visited = set()
        q = deque([beginWord])
        visited.add(beginWord)
        res = 0
        while q:
            res += 1
            size = len(q)
            for i in range(size - 1, -1, -1):
                word = q.popleft()
                # print(word)
                visited.add(word)
                for i in range(len(word)):
                    for j in range(0, 26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                        if new_word == endWord:
                            return res + 1
                        if new_word in wordSet and new_word not in visited:
                            q.append(new_word)
                            visited.add(new_word)
        return 0
