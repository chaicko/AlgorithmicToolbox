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
        self.elems = []

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
        if query.type == "check":
            # use reverse order, because we append strings to the end
            return self.write_chain(cur for cur in reversed(self.elems)
                                    if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                return self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

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

