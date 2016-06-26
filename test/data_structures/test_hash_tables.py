import data_structures.hash_tables.hash_chains as hash_chains
import data_structures.hash_tables.hash_substring as hash_substring
import data_structures.hash_tables.phone_book as phone_book

import pytest
import names
import random


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
        for i in range(phone_book.MAX_NUMBER, phone_book.MAX_NUMBER-(n//2), -1):
            contacts[i] = names.get_last_name()[:phone_book.MAX_NAME_LEN]

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
    def test_sample1(self):
        pass


@pytest.mark.timeout(5)
class TestHashSubstring:
    def test_sample1(self):
        pass
