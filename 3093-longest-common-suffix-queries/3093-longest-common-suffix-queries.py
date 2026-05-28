class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        # Find smallest word index
        smallest_index = 0

        for i in range(len(wordsContainer)):

            if len(wordsContainer[i]) < len(wordsContainer[smallest_index]):
                smallest_index = i

        # Build Trie using reversed words
        for i, word in enumerate(wordsContainer):

            node = root

            reversed_word = word[::-1]

            # Update root index
            if node.index == -1 or len(word) < len(wordsContainer[node.index]):
                node.index = i

            for ch in reversed_word:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store shortest word index
                if node.index == -1 or len(word) < len(wordsContainer[node.index]):
                    node.index = i

        answer = []

        # Process queries
        for query in wordsQuery:

            node = root

            reversed_query = query[::-1]

            best_index = smallest_index

            for ch in reversed_query:

                if ch not in node.children:
                    break

                node = node.children[ch]
                best_index = node.index

            answer.append(best_index)

        return answer