import React from 'react';
import './App.scss';
import SearchBar from './components/SearchBar';

import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Home from './Home';
import View from './View';

import HomeButton from './components/HomeButton'

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        course_buckets: []
      }

    var data = {
      "aggs": {
        "files": {
          "terms": { "field": "file.url", "size": 10000 }
        }
      },
      "size": 0
    }

    fetch(`https://search-note-search-2-ftoser4h3m5pirtb6zhql6rvfa.ca-central-1.es.amazonaws.com/notes/_search`, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json"
      },
    }).then(x => x.json()).then(x => {
      var course_buckets = x.aggregations.files.buckets.reduce((obj, word) => {
        // Get the length of the world
        var length = word.key.match("[A-Z]{3}[0-9]{4}");

        // If the length doesn't already exist as a key in the object, create it
        if (!obj.hasOwnProperty(length)) {
          obj[length] = [];
        }

        // Push the number to its integer key
        obj[length].push(word);

        // Pass the object on to the next loop
        return obj;
      })
      this.state = {
        course_buckets: course_buckets
      }
    })
  }
  render() {
    return (
      <div className="App">
        <Router>
          <div style={{ display: 'grid', gridTemplateColumns: '75px auto' }} id="Header">
            <HomeButton></HomeButton>
            <SearchBar></SearchBar>
          </div>
          <Switch>
            <Route path="/" exact>
              <Home course_buckets={this.state.course_buckets} />
            </Route>
            <Route path="/note/:id" component={View}></Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
