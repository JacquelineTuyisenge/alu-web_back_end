/* eslint-disable */

export default function updateStudentGradeByCity(students, city, newGrade) {
  if (!Array.isArray(newGrade)) {
    return [];
  }

  const updatedStudents = students
    .filter(student => student.location === city)
    .map(student => {
      const foundGrade = newGrade.find(grade => grade.studentId === student.id);
      return {
        ...student,
        grade: foundGrade ? foundGrade.grade : 'N/A'
      };
    });

return updatedStudents;
}
  