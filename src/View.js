import React from 'react'

export default class View extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
            content: ""
        }
        const { match: { params } } = this.props;
        console.log(params)
        fetch("https://search-note-search-2-ftoser4h3m5pirtb6zhql6rvfa.ca-central-1.es.amazonaws.com/notes/_doc/" + params.id)
            .then(x => x.json())
            .then(x => {
                this.setState({
                    loading: false,
                    content: "Test" + x._source.content
                })
                console.log(x._source.content)
            });
    }

    render() {
        return (<div>{this.state.content}</div>)
    }
}