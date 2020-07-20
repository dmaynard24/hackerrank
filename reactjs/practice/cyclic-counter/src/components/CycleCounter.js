import React from 'react';

class CycleCounter extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      count: 0,
    };

    this.increment = this.increment.bind(this);
  }

  increment() {
    this.setState({
      count: this.state.count + 1 === this.props.cycle ? 0 : this.state.count + 1,
    });
  }

  render() {
    return (
      <button data-testid="cycle-counter" style={{ fontSize: '1rem', width: 120, height: 30 }} onClick={this.increment}>
        {this.state.count}
      </button>
    );
  }
}

export default CycleCounter;
