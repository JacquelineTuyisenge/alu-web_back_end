export default function createReportObject(employeesList) {
  const allEmployees = {};

  for (const [department, employees] of Object.entries(employeesList)) {
    allEmployees[department] = [...employees];
  }

  const getNumberOfDepartments = () => Object.keys(employeesList).length;

  return {
    allEmployees,
    getNumberOfDepartments,
  };
}
