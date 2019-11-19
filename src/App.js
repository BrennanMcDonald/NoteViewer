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

function App() {
  return (
    <div className="App">
      <Router>
      <div style={{display:'grid', gridTemplateColumns: '75px auto'}} id="Header">
        <HomeButton></HomeButton>
        <SearchBar></SearchBar>
      </div>
        <Switch>
          <Route path="/" exact>
            <Home />
          </Route>
          <Route path="/:id" component={View}></Route>
        </Switch>
    </Router>
    </div>
  );
}

export default App;
