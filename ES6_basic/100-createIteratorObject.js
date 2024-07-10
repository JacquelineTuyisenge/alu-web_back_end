/* eslint-disable */

import createReportObject from './12-createReportObject';

export default function createIteratorObject(report) {
  const { allEmployees } = report;

  const employeesArray = [];

  for (const department in allEmployees) {
    for (const employee of allEmployees[department]) {
      employeesArray.push(employee);
    }
  }

  return {
    [Symbol.iterator]: function() {
      let index = 0;
      return {
        next: function() {
          return index < employeesArray.length ?
            { value: employeesArray[index++], done: false } :
            { done: true };
        }
      };
    }
  };
}

const employeesList = {
  'HR': ['Alice', 'Bob'],
  'IT': ['Charlie', 'David', 'Emma'],
  'Finance': ['Frank', 'Grace', 'Henry']
};

const report = createReportObject(employeesList);

const employeeIterator = createIteratorObject(report);

for (const employee of employeeIterator) {
  console.log(employee);
}
