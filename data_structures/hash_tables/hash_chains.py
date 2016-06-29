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
        self._arr = []
        for _ in range(bucket_count):
            self._arr.append(list())
        self.processed_queries = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    @staticmethod
    def read_query(query_string):
        return Query(query_string.split())

    def process_query(self, query):
        if query.type == "check" and query.ind < len(self._arr):
            chain_l = self._arr[query.ind]
            chain = ' '.join(reversed(chain_l))
            self.processed_queries.append(chain)
            # use reverse order, because we append strings to the end
            return chain
        else:
            # calculate hash for input string
            index = self._hash_func(query.s)
            chain = self._arr[index]
            found = query.s in chain

            if query.type == 'find':
                msg = "yes" if found else "no"
                self.processed_queries.append(msg)
                return msg

            if query.type == 'add' and not found:
                chain.append(query.s)

            if query.type == 'del' and found:
                chain.remove(query.s)

        return None


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    # Process queries
    num_queries = int(input())
    results = []
    for i in range(num_queries):
        query = proc.read_query(input())
        res = proc.process_query(query)
        if res is not None:
            results.append(res)
    for r in results:
        print(r)
