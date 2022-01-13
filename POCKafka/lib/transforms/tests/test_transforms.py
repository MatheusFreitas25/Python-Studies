#
# Copyright (c) 2020 Team Analytics <analytics@kovi.us>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

from transforms.flat import FlatArray, FlatDict, FlatNumber


class TestFlatNumber:
    def test_flattening_number(self):
        fla = FlatNumber(3)
        expected = {"$": 3}
        assert fla.flattening() == expected


class TestFlatArray:
    def test_flattening_array(self):
        fla = FlatArray([1, 2, 3])
        expected = {"$.[0].value": 1, "$.[1].value": 2, "$.[2].value": 3}
        assert fla.flattening() == expected

    def test_is_nested_false(self):
        fla = FlatArray([1, 2, 3])
        expected = False
        assert fla.is_nested() == expected

    def test_is_nested_true(self):
        fla = FlatArray([[1, 2], [3, 4]])
        expected = True
        assert fla.is_nested() == expected


class TestFlatDict:
    def test_flattening_dict(self):
        fla = FlatDict({"first_name": "Name", "last_name": "LastName"})
        expected = {"$.first_name": "Name", "$.last_name": "LastName"}
        assert fla.flattening() == expected
