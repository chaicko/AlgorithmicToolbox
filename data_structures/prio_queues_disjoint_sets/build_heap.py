# python3


class HeapBuilder:
    def __init__(self, data=()):
        self._swaps = []
        self._data = list(data)

    @property
    def swaps(self):
        return self._swaps

    @property
    def data(self):
        return self._data

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def sift_down(self, i):
        size = len(self.data)
        min_index = i

        l = self.left_child(i)
        if l < size and self.data[l] < self.data[min_index]:
            min_index = l

        r = self.right_child(i)
        if r < size and self.data[r] < self.data[min_index]:
            min_index = r

        if i != min_index:
            self.data[i], self.data[min_index] = self.data[min_index], \
                                                 self.data[i]

        self.sift_down(min_index)

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
