import React from 'react'
import SearchResults from './SearchResults.jsx'
import "./SearchBar.scss"

export default class SearchBar extends React.Component {

    constructor(props){
        super(props)
        this.state = {
            searchInput: ""
        }
    }

    onSearchChange = (e) => {
        this.setState({
            searchInput: e.target.value
        })
    }

    render() {
        return(
            <div id="SearchBar">
                <input placeholder="Search..." onChange={this.onSearchChange} value={this.state.searchInput} />
                <SearchResults query={this.state.searchInput} />
            </div>
        )
    }
}