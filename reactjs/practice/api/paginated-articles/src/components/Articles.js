import React from 'react';

class Articles extends React.Component {
  constructor() {
    super();

    this.state = {
      totalPages: 0,
      data: [],
    };

    this.showPage(1);
  }

  showPage(pageNum) {
    fetch(`https://jsonmock.hackerrank.com/api/articles?page=${pageNum}`, {
      type: 'GET',
    })
      .then((res) => res.json())
      .then((json) => {
        this.setState({
          totalPages: json.total_pages,
          data: json.data,
        });
      });
  }

  render() {
    return (
      <React.Fragment>
        <div className="pagination">
          {[...Array(this.state.totalPages)].map((e, i) => (
            <button data-testid="page-button" key={`page-button-${i + 1}`} onClick={() => this.showPage(i + 1)}>
              {i + 1}
            </button>
          ))}
        </div>
        <ul className="results">
          {this.state.data.map((a, i) =>
            a.title ? (
              <li data-testid="result-row" key={`title-${i + 1}`}>
                {a.title}
              </li>
            ) : null,
          )}
        </ul>
      </React.Fragment>
    );
  }
}

export default Articles;
