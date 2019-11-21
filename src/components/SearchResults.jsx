import React from 'react'
import {Link} from 'react-router-dom'
import "./SearchResults.scss"
export default class SearchResults extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
            results: [],
            prevQuery: ""
        }
    }

    shouldComponentUpdate() {
        this.fetchResults(this.props.query);
        return true;
    }

    fetchResults(query) {
        if (query !== this.state.prevQuery) {
            if (query === "") {
                this.setState({
                    loading: false,
                    results: [],
                    prevQuery: query
                });
            }
            fetch(`https://search-note-search-2-ftoser4h3m5pirtb6zhql6rvfa.ca-central-1.es.amazonaws.com/notes*/_search?q=${query}`)
                .then(x => x.json())
                .then(x => {
                    console.log(this.state.results)
                    this.setState({
                        loading: false,
                        results: x.hits.hits.slice(0, 5),
                        prevQuery: query
                    });
                });
        }
    }
    render() {
        this.state.results.forEach(x => {
            if (x._source.file.url.match("[A-Z]{3}[0-9]{4}") == null) {
                console.log(x._source.file.url)
            }

        })
        if (this.state.loading && this.state.prevQuery !== "") {
            return (
                <div id="SearchResults">
                    Loading
                </div>
            )
        } else {
            return (
                <div id="SearchResults">
                    {
                        this.state.results.map(x => {
                            if (x._source.file.url !== "file:///home/brennan/Takeout/archive_browser.html" && x._source.file.url !== "file:///home/brennan/Takeout/Drive/School/Old Work/Linear Algebra/Untitled document.pdf") {
                                var courseCode = x._source.file.url.match("1[A-Z]{3}[0-9]{4}") || [""];
                                return (
                                    <Link to={'/note/' + x._id} onClick={() => this.setState({results: []})} onBlur={() => this.setState({results: []})}>
                                        <div className="result">
                                            <div className='course'>{courseCode[0]}</div>
                                            <div className='filename'>{x._source.file.filename}</div>
                                            <div className='content'>{x._source.content.substring(0, Math.min(200, x._source.content.length))}...</div>
                                        </div>
                                    </Link>
                                )
                            } else {
                                return (<p></p>);
                            }
                        })
                    }
                </div>
            )
        }
    }
}