export default function getStudentIdsSum(students) {
  const studentsIdArray = students.map((student) => student.id);

  const sum = studentsIdArray.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  return sum;
}
