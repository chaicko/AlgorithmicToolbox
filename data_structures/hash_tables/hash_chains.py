# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self._arr = [[]] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    @staticmethod
    def write_search_result(was_found):
        return 'yes' if was_found else 'no'

    @staticmethod
    def write_chain(chain):
        return ' '.join(chain)

    @staticmethod
    def read_query(query_string):
        return Query(query_string.split())

    def process_query(self, query):
        if query.type == "check" and query.ind < len(self._arr):
            chain = self._arr[query.ind]
            # use reverse order, because we append strings to the end
            return self.write_chain(reversed(chain))
        else:
            # calculate hash for input string
            index = self._hash_func(query.s)
            found = query.s in self._arr[index]
            if query.type == 'find':
                return self.write_search_result(found)
            if query.type == 'add' and not found:
                self._arr[index].append(query.s)
            if query.type == 'del' and found:
                self._arr[index].remove(query.s)

        return None


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    # Process queries
    num_queries = int(input())
    for i in range(num_queries):
        query = proc.read_query(input())
        res = proc.process_query(query)
        if res is not None:
            print(res)

