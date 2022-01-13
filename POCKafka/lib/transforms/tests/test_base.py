import unittest
from unittest.mock import Mock
import transforms.base as bt


class TestBaseTransforms(unittest.TestCase):
    def test_record_batch_initialize(self):
        records2 = [{"a": 1}, {"a": 2}]
        bt.RecordBatch(records)

    def test_record_batch_apply(self):
        records = [{"a": 1}, {"a": 2}]
        batch = bt.RecordBatch(records)
        mock = Mock(return_value=records)
        batch.apply(mock)
        mock.assert_called_once_with(batch)
