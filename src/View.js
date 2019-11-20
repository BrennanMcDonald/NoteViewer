import React from 'react'
import { pdfjs, Document, Page } from 'react-pdf';

export default class View extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
            content: "",
            pageNumber: 1,
            numPages: 0
        }
        pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;
        const { match: { params } } = this.props;
        fetch("https://search-note-search-2-ftoser4h3m5pirtb6zhql6rvfa.ca-central-1.es.amazonaws.com/notes/_doc/" + params.id)
            .then(x => x.json())
            .then(x => {
                this.setState({
                    loading: false,
                    content: "Test" + x._source.content,
                    file_url: "http://localhost:3000/notes/" + x._source.file.url.replace("file:///home/brennan/Takeout/Drive/School/", "")
                })
            });
    }

    onDocumentLoadSuccess = ({ numPages }) => {
        this.setState({
            numPages: numPages
        })
    }

    decPage = () => {
        const { pageNumber } = this.state;
        if (pageNumber > 1) {
            this.setState({pageNumber: (pageNumber - 1)})
        }
    }

    incPage = () => {
        const { pageNumber, numPages } = this.state;
        if (pageNumber < numPages) {
            this.setState({pageNumber: (pageNumber + 1)})
        }

    }

    render() {
        const { pageNumber, numPages } = this.state;
        console.log(pageNumber)
        return (
            <div id="Viewer">
                    <button onClick={this.decPage}>{"<"}</button>
                    <div>
                <Document
                    file={this.state.file_url}
                    onLoadSuccess={this.onDocumentLoadSuccess}>
                    <Page pageNumber={pageNumber} />
                </Document>
                    <p>Page {pageNumber} of {numPages}</p>
                    </div>
                    <button onClick={this.incPage}>></button>
            </div>
        )
    }
}