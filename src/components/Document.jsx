import React from 'react'
import { Link } from 'react-router-dom'

export default class Document extends React.Component {
    render() {
        var files = this.props.item._source.file.url.split('/');
        var filename = files[files.length-1]
        return (
            <Link to={'/note/'+this.props.item._id}>
                <div className="filename">
                    {filename}
                </div>
            </Link>

        )
    }
}