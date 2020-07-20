import React from 'react';

class EmployeesList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      employees: props.employees,
    };

    this.filter = this.filter.bind(this);
  }

  filter(e) {
    let query = e.target.value.toLocaleLowerCase(),
      filteredEmployees = this.props.employees.filter((e) => {
        return e.name.toLocaleLowerCase().indexOf(query) > -1;
      });
    this.setState({
      employees: filteredEmployees,
    });
  }

  render() {
    return (
      <React.Fragment>
        <div className="controls">
          <input type="text" className="filter-input" data-testid="filter-input" onChange={this.filter} />
        </div>
        <ul className="employees-list">
          {this.state.employees.map((employee) => (
            <li key={employee.name} data-testid="employee">
              {employee.name}
            </li>
          ))}
        </ul>
      </React.Fragment>
    );
  }
}

export default EmployeesList;
