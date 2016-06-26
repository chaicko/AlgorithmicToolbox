# python3
MAX_NUMBER = 10 ** 7 - 1
MAX_NAME_LEN = 15
MAX_QUERIES = 10 ** 5


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = ["not found"] * (MAX_NUMBER + 1)
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number] = "not found"
        else:
            result.append(contacts[cur_query.number])
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

