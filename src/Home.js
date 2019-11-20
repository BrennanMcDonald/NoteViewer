import React from 'react'
import Document from './components/Document'
import "./Home.scss"

export default class Home extends React.Component {
    constructor(props) {
        super(props);
    }
    
    render() {
        return (<div>
            {
                Object.keys(this.props.course_buckets).sort().map(x => {
                    if (x.match("[A-Z]{3}[0-9]{4}")) {
                        return (<div className={"course-section"}  key={x}>
                            <div className='course-header'>{x}<hr /></div>
                            <div className='course-grid'>
                                {
                                    this.props.course_buckets[x].map(item => {
                                        var tempSplit = item._source.file.url.split("/");
                                        var filename = tempSplit[tempSplit.length - 1]
                                        return (
                                            <Document key={filename} item={item}></Document>
                                        )
                                    })
                                }
                            </div>
                        </div>)
                    } else {
                        return (<div key={x}></div>)
                    }
                })
            }
        </div>)
    }
}