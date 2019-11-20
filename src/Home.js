import React from 'react'

export default class Home extends React.Component {
    render() {
        console.log(this.props.course_buckets)
        return (<div>
            {
                this.props.course_buckets.map(x => {
                    console.log(x)
                    return (<div></div>)
                })
            }
        </div>)
    }
}