
import p8
import unittest

 
class TestP8(unittest.TestCase):
	def setUp(self):
		self.list=[1,2,3,4,5,6,7,8,9,10]
		self.invalidList=[1,2,3,4,6,233,4,3,5,6,2,"aa",23,45]

	def test_SampleMean(self):
		mean=p8.sampleMean(self.list)
		self.assertEqual(mean,5.5)

	def test_SampleMeanInvalid(self):
		with self.assertRaises(ValueError):
			mean=p8.sampleMean(self.invalidList)

	def test_standardDeviation(self):
		std=p8.standardDeviation(self.list)
		self.assertEqual(round(std,8),2.87228132)

	def test_standardDeviationInvalid(self):
		with self.assertRaises(ValueError):
			std=p8.standardDeviation(self.invalidList)	

	def test_Median(self):
		median=p8.median(self.list)
		self.assertEqual(median,5.5)

	def test_MedianInvalid(self):
		with self.assertRaises(ValueError):
			median=p8.median(self.invalidList)	

	def test_nQuartile(self):
		quartile=p8.nQuartile(self.list,1)
		self.assertEqual(quartile,3)
		quartile=p8.nQuartile(self.list,2)		
		self.assertEqual(quartile,5.5)
		quartile=p8.nQuartile(self.list,3)		
		self.assertEqual(quartile,8)

	def test_nQuartileInvalidList(self):
		with self.assertRaises(ValueError):
			quartile=p8.nQuartile(self.invalidList,1)

	def test_nQuartileInvalidQuartile(self):
		with self.assertRaises(ValueError):
			quartile=p8.nQuartile(self.list,8)

	def test_nPercentile(self):
		percentile=p8.nPercentile(self.list,50)
		self.assertEqual(percentile,5.5)
		percentile=p8.nPercentile(self.list,11)		
		self.assertEqual(percentile,1.99)


	def test_nPercentileInvalidList(self):
		with self.assertRaises(ValueError):
			percentile=p8.nPercentile(self.invalidList,11)

	def test_nPercentileInvalidPercentile(self):
		with self.assertRaises(ValueError):
			percentile=p8.nPercentile(self.list,200)


if __name__ == '__main__':
    unittest.main()
