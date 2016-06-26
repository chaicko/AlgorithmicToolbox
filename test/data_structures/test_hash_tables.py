import data_structures.hash_tables.hash_chains as hash_chains
import data_structures.hash_tables.hash_substring as hash_substring
import data_structures.hash_tables.phone_book as phone_book

import pytest


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
