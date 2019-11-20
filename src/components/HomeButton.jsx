import React from 'react'
import home from '../img/home.png'
import { Link } from 'react-router-dom'
import './HomeButton.scss'

export default function () {
    return (
        <div id="HomeButton">
            <Link to="/">
                <img src={home} alt="Home icon" style={{ width: "100%", filter: "invert(1)" }} />
            </Link>
        </div>
    )
}