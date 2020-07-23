import React from 'react';

class Translator extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      translated: '',
    };

    this.translate = this.translate.bind(this);
  }

  translate(e) {
    const text = e.target.value;

    if (this.props.translations.has(text)) {
      this.setState({
        translated: this.props.translations.get(text),
      });
    } else {
      this.setState({
        translated: '',
      });
    }
  }

  render() {
    return (
      <React.Fragment>
        <div className="controls">
          <div className="input-container">
            <span>input:</span>
            <input type="text" className="text-input" data-testid="text-input" onChange={this.translate} />
          </div>
          <div className="input-container">
            <span>output:</span>
            <input type="text" className="text-output" data-testid="text-output" readOnly value={this.state.translated} />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Translator;
