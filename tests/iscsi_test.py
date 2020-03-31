# SPDX-FileCopyrightText: © 2014 The cython-iscsi Authors
# SPDX-License-Identifier: LGPL-2.1+

import unittest

import iscsi


class IscsiTest(unittest.TestCase):
    def test_url_parse(self):
        context = iscsi.Context("foobar")

        url = iscsi.URL(context, "iscsi://localhost/my-target/0")
        self.assertEqual(url.portal, "localhost")

    def test_set_context_params(self):
        context = iscsi.Context("foobar")
        context.set_targetname("my-target")
        context.set_header_digest(iscsi.ISCSI_HEADER_DIGEST_NONE)

    def test_task(self):
        task = iscsi.Task(b"\x12\x00\x00\x00\x60\x00", iscsi.SCSI_XFER_READ, 96)
        self.assertIsNotNone(task)