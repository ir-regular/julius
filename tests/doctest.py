import doctest
import unittest

import julius.source.phrasefile
import julius.source.srs
import julius.voice.say

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(julius.source.phrasefile))
suite.addTest(doctest.DocTestSuite(julius.source.srs))
suite.addTest(doctest.DocTestSuite(julius.voice.say))

runner = unittest.TextTestRunner(verbosity=0)
runner.run(suite)
