import React, { Component } from "react"

const ramenItems = [
  {
    id: 1,
    title: "Nature walk in the park",
    videoUrl: "https://www.youtube.com/watch?v=2Fp5kmeZlk4",
  },

  {
    id: 2,
    title: "Visit",
    videoUrl: "https://www.youtube.com/watch?v=2Fp5kmeZlk4",
  },

  {
    id: 3,
    title: "Write",
    videoUrl: "https://www.youtube.com/watch?v=2Fp5kmeZlk4",
  },
];

class App extends Component {
    constructor(props) {
      super(props);
      this.state = {ramenItems};
    };

    render() {
      return (
        <main className="content">
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush">
              {this.state.ramenItems.map(item => (
              <div>
                <h1>{item.title}</h1>
                <span>{item.videoUrl}</span>
              </div>
              ))}
              </ul>
            </div>
          </div>
        </div>
      </main>
      )
    }
  }
  
export default App;