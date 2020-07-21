import React from 'react';

class TextEditor extends React.Component {
  constructor() {
    super();

    this.state = {
      word: '',
      words: [],
    };

    this.setWord = this.setWord.bind(this);
    this.push = this.push.bind(this);
    this.pop = this.pop.bind(this);
  }

  setWord(e) {
    this.setState({
      word: e.target.value,
    });
  }

  push() {
    this.setState({
      word: '',
      words: [...this.state.words, this.state.word],
    });
  }

  pop() {
    this.setState({
      words: this.state.words.slice(0, this.state.words.length - 1),
    });
  }

  render() {
    return (
      <React.Fragment>
        <div className="controls">
          <input className="word-input" type="text" data-testid="word-input" value={this.state.word} onChange={this.setWord} />
          <button data-testid="append-button" disabled={this.state.word.trim() === ''} onClick={this.push}>
            Append
          </button>
          <button data-testid="undo-button" disabled={this.state.words.length === 0} onClick={this.pop}>
            Undo
          </button>
        </div>
        <div className="text-field" data-testid="text-field">
          {this.state.words.join(' ')}
        </div>
      </React.Fragment>
    );
  }
}

export default TextEditor;
