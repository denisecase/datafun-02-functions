from numeric_series import NumericSeries

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

class NumericMusicStudentGradesSeries(NumericSeries):

    def __init__(self, name, units, data, student_name):
        super().__init__(name, units, data)
        self.student_name = student_name

    def __str__(self):
        str = f"NumericMusicStudentGradesSeries with name={self.name}, units={self.units}, student_name{self.student_name}, and {len(self.data)} data points: {self.data}"
        return str
    
name1 = "Test 1"
units1 = "A, B, C, D, F"
data1 = [68.5, 75.5, 79.5, 85.5, 75.5, 97.5, 95.5]
student_name1= "Johnni"

object1 = NumericMusicStudentGradesSeries(name1, units1, data1, student_name1)

name2 = "Test 2"
units2 = "A, B, C, D, F"
data2 = [72.5, 79.5, 82.5, 87.5, 91.5, 93.5, 96.5]
student_name2= "Millie"

object2 = NumericMusicStudentGradesSeries(name2, units2, data2, student_name2)

data3 = list(range(51, 90))
name3 = "Test 3"
units3 = "A, B, C, D, F"
student_name3= "Carrie"

object3 = NumericMusicStudentGradesSeries(name3, units3, data3, student_name3)

logger.info(f"Created: {object1}")
logger.info(f"Created: {object2}")
logger.info(f"Created: {object3}")

object_list = [object1, object2, object3]

for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")
