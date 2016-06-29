import data_structures.hash_tables.hash_chains as hash_chains
import data_structures.hash_tables.hash_substring as hash_substring
import data_structures.hash_tables.phone_book as phone_book

import pytest
import random
from faker import Factory
import os

CI = os.environ.get('CI') == 'true'


@pytest.mark.timeout(6)
class TestPhoneBook:
    @pytest.mark.parametrize("test_input,expected", [
        (
            (
                "add 911 police",
                "add 76213 Mom",
                "add 17239 Bob",
                "find 76213",
                "find 910",
                "find 911",
                "del 910",
                "del 911",
                "find 911",
                "find 76213",
                "add 76213 daddy",
                "find 76213"
            ),
            [
                "Mom",
                "not found",
                "police",
                "not found",
                "Mom",
                "daddy"
            ]
        ),
        (
            (
                "find 3839442",
                "add 123456 me",
                "add 0 granny",
                "find 0",
                "find 123456",
                "del 0",
                "del 0",
                "find 0",
            ),
            [
                "not found",
                "granny",
                "me",
                "not found",
            ]
        ),
    ])
    def test_samples(self, test_input, expected):
        queries = [phone_book.Query(q.split()) for q in test_input]
        exp = self.process_queries_dict(queries)
        assert exp == expected
        result = phone_book.process_queries(queries)
        assert result == expected

    def test_one_add(self):
        test_input = ["add 911 police"]
        queries = [phone_book.Query(q.split()) for q in test_input]
        result = phone_book.process_queries(queries)
        assert result == []

    def test_one_del(self):
        test_input = ["del 911"]
        queries = [phone_book.Query(q.split()) for q in test_input]
        result = phone_book.process_queries(queries)
        assert result == []

    def test_one_find(self):
        test_input = ["find 911"]
        queries = [phone_book.Query(q.split()) for q in test_input]
        result = phone_book.process_queries(queries)
        assert result == ["not found"]

    @staticmethod
    def process_queries_dict(queries):
        d = {}
        res = []
        for q in queries:
            if q.type == 'add':
                d[q.number] = q.name
            elif q.type == 'del' and q.number in d:
                del d[q.number]
            elif q.type == 'find':
                res.append(d.get(q.number, 'not found'))

        return res

    def test_worst_case(self):
        n = phone_book.MAX_QUERIES
        contacts = {}
        fake = Factory.create()
        for i in range(phone_book.MAX_NUMBER, phone_book.MAX_NUMBER-(n//2), -1):
            contacts[i] = fake.first_name()[:phone_book.MAX_NAME_LEN]

        numbers = contacts.keys()
        # Create n // 2 add queries
        add_queries = [phone_book.Query(('add', str(num), name))
                       for num, name in contacts.items()]

        # Create n // 4 del queries
        _nums = list(numbers)
        random.shuffle(_nums)
        del_queries = [phone_book.Query(('del', str(num)))
                       for num in _nums[:n // 4]]

        # Create n // 4 find queries
        random.shuffle(_nums)
        find_queries = [phone_book.Query(('find', str(num)))
                        for num in _nums[:n // 4]]

        queries = add_queries + del_queries + find_queries
        random.shuffle(queries)
        expected = self.process_queries_dict(queries)
        result = phone_book.process_queries(queries)
        assert result == expected


@pytest.mark.timeout(7)
class TestHashChains:
    class MyQueryProcessor:
        _multiplier = 263
        _prime = 1000000007

        def __init__(self, bucket_count):
            self.bucket_count = bucket_count
            # store all strings in one list
            self._arr = {}

        def _hash_func(self, s):
            ans = 0
            for c in reversed(s):
                ans = (ans * self._multiplier + ord(c)) % self._prime
            return ans % self.bucket_count

        def process_query(self, query):
            if query.type == "check":
                chain = self._arr.get(query.ind, None)
                if chain is not None:
                    return ' '.join(reversed(chain))
                return ''
            else:
                # calculate hash for input string
                index = self._hash_func(query.s)
                if query.type == 'add':
                    if index in self._arr and query.s not in self._arr[index]:
                        self._arr[index].append(query.s)
                    else:
                        self._arr[index] = [query.s]

                if query.type == 'find':
                    if index in self._arr and query.s in self._arr[index]:
                        return "yes"
                    else:
                        return "no"

                if query.type == 'del' and index in self._arr:
                    try:
                        self._arr[index].remove(query.s)
                    except ValueError:
                        pass

            return None


    @pytest.mark.parametrize("buck_size,test_data", [
        (5, (
                ("add world", None),
                ("add HellO", None),
                ("check 4", "HellO world"),
                ("find World", "no"),
                ("find world", "yes"),
                ("del world", None),
                ("check 4", "HellO"),
                ("del HellO", None),
                ("add luck", None),
                ("add GooD", None),
                ("check 2", "GooD luck"),
                ("del good", None)
        )),
        (4, (
                ("add test", None),
                ("add test", None),
                ("find test", "yes"),
                ("del test", None),
                ("find test", "no"),
                ("find Test", "no"),
                ("add Test", None),
                ("find Test", "yes"),
        )),
    ])
    def test_samples(self, buck_size, test_data):
        proc = hash_chains.QueryProcessor(buck_size)
        my_proc = self.MyQueryProcessor(buck_size)
        for query_str, expected in test_data:
            query = proc.read_query(query_str)
            exp = my_proc.process_query(query)
            assert exp == expected
            res = proc.process_query(query)
            assert res == expected

    def test_repeated_deletion(self):
        proc = hash_chains.QueryProcessor(5)
        queries = ["add test",
                   "add test",
                   "add test",
                   "del test",
                   "del test",
                   "del test",
                   "check 0",
                   "check 1",
                   "check 2",
                   "check 3",
                   "check 4"]
        expected = ['', '', '', '', '']
        for query_str in queries:
            query = proc.read_query(query_str)
            proc.process_query(query)
        assert proc.processed_queries == expected

    def test_repeated_checks(self):
        proc = hash_chains.QueryProcessor(5)
        queries = ["check 0",
                   "add test",
                   "find test",
                   "check 0",
                   "check 1",
                   "check 2",
                   "check 3",
                   "check 4",
                   "add Test",
                   "del test",
                   "find test",
                   "check 0",
                   ]

        for query_str in queries:
            query = proc.read_query(query_str)
            proc.process_query(query)

        pass


@pytest.mark.timeout(5)
class TestHashSubstring:
    @pytest.mark.parametrize("pattern, text, expected", [
        ("aba", "abacaba", [0, 4]),
        ("Test", "testTesttesT", [4]),
        ("aaaaa", "baaaaaaa", [1, 2, 3]),
    ])
    def test_samples(self, pattern, text, expected):
        assert hash_substring.get_occurrences(pattern, text) == expected
        assert hash_substring.rabin_karp(pattern, text) == expected

    def test_worst_case(self):
        text = 'a' * (hash_substring.MAX_TEXT_LEN // 2)
        pattern = 'a' * (len(text) // 2)
        expected = [i for i in range(len(pattern)+1)]
        assert hash_substring.rabin_karp(pattern, text) == expected
